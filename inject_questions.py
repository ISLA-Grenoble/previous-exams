import os
import json
import re
import glob

def parse_questions_md(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('\r\n', '\n')
    
    header_pattern = r'^##\s+(?:Part|Exercise)\s+(\d+)'
    headers = list(re.finditer(header_pattern, content, re.MULTILINE))
    
    parts = {}
    if headers:
        for i in range(len(headers)):
            part_num = int(headers[i].group(1))
            start = headers[i].end()
            end = headers[i+1].start() if i+1 < len(headers) else len(content)
            part_content = content[start:end]
            
            # Extract questions
            q_pattern = r'\n(\*\*(?:Q\d+|(?:\([a-z]\))|Q\d+\s+—).*?\*\*)'
            q_starts = list(re.finditer(q_pattern, part_content, re.DOTALL))
            
            if not q_starts:
                q_pattern = r'\n(\*\*?\([a-z]\)\*\*?)'
                q_starts = list(re.finditer(q_pattern, part_content))
            
            questions = []
            if q_starts:
                for j in range(len(q_starts)):
                    q_start = q_starts[j].start()
                    q_end = q_starts[j+1].start() if j+1 < len(q_starts) else len(part_content)
                    q_text = part_content[q_start:q_end].strip()
                    questions.append(q_text)
            
            parts[part_num] = questions
    return parts

def inject_into_notebook(nb_path, parts_dict, target_part=None):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    updated_cells = []
    injected_questions = set()
    
    # Pre-parse parts and their questions
    all_questions = []
    if target_part:
        if target_part in parts_dict:
            all_questions = [(target_part, q) for q in parts_dict[target_part]]
    else:
        for p in sorted(parts_dict.keys()):
            all_questions.extend([(p, q) for q in parts_dict[p]])

    q_idx = 0
    current_nb_part = None

    for cell in nb['cells']:
        cell_text = "".join(cell['source']).lower()
        
        # Identify current part in notebook
        part_m = re.search(r'(?:part|exercise)\s+(\d+)', cell_text)
        if part_m and ('#' in cell_text or 'part' in cell_text):
            current_nb_part = int(part_m.group(1))

        # If we have questions left
        if q_idx < len(all_questions):
            matched_indices = []
            for i in range(q_idx, len(all_questions)):
                p_num, q_text = all_questions[i]
                
                # If we're in a multi-part notebook, only match questions for the current part
                if not target_part and current_nb_part is not None and p_num != current_nb_part:
                    continue
                
                m = re.search(r'(Q(\d+)|(?:\(([a-z])\)))', q_text)
                if m:
                    marker_type = 'Q' if m.group(2) else 'letter'
                    marker_val = m.group(2) or m.group(3)
                    
                    patterns = []
                    if marker_type == 'Q':
                        patterns = [f'q{marker_val}', f'question {marker_val}']
                    else:
                        patterns = [f'({marker_val})', f'question ({marker_val})']
                    
                    if any(p in cell_text for p in patterns) and (
                        'question' in cell_text or 
                        '##' in cell_text or 
                        '**' in cell_text or 
                        (len(cell_text.strip()) < 60 and any(p in cell_text.strip() for p in patterns))
                    ):
                        matched_indices.append(i)
            
            if matched_indices:
                # We should only inject questions that belong to the current part (if known)
                # or questions that were skipped because they had no anchor but now we found an anchor for a later question in the same part.
                
                last_matched_idx = max(matched_indices)
                # Inject all questions from q_idx to last_matched_idx that belong to the SAME part as the matched one
                # or if we don't care about parts (single part notebook)
                
                target_p_num = all_questions[last_matched_idx][0]
                
                for k in range(q_idx, last_matched_idx + 1):
                    p_k, q_k = all_questions[k]
                    if q_k not in injected_questions:
                        # Only inject if it's the right part
                        if target_part or p_k == target_p_num:
                            new_q_cell = {
                                "cell_type": "markdown",
                                "metadata": {},
                                "source": [q_k + "\n"]
                            }
                            updated_cells.append(new_q_cell)
                            injected_questions.add(q_k)
                
                # Update q_idx to the next question that hasn't been processed
                # This is tricky. Let's just advance it if we've reached it.
                if q_idx <= last_matched_idx:
                     q_idx = last_matched_idx + 1

        updated_cells.append(cell)
    
    nb['cells'] = updated_cells
    
    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

def process_exam_dir(exam_dir):
    md_path = os.path.join(exam_dir, 'QUESTIONS.md')
    if not os.path.exists(md_path):
        return f"Skipping {exam_dir}: QUESTIONS.md not found"
    
    parts = parse_questions_md(md_path)
    python_dir = os.path.join(exam_dir, 'python')
    if not os.path.exists(python_dir):
        return f"Skipping {exam_dir}: python/ directory not found"
    
    notebooks = glob.glob(os.path.join(python_dir, '*.ipynb'))
    results = []
    
    for nb_path in notebooks:
        nb_name = os.path.basename(nb_path)
        m = re.search(r'Part(\d+)', nb_name)
        if m:
            part_num = int(m.group(1))
            inject_into_notebook(nb_path, parts, part_num)
            results.append(f"Updated {nb_name} with Part {part_num} questions")
        else:
            # Handle correction.ipynb or other single notebooks
            inject_into_notebook(nb_path, parts)
            results.append(f"Updated {nb_name} with relevant questions")
            
    return "\n".join(results)

if __name__ == "__main__":
    exam_dirs = [
        'exam-2018', 'exam-2019-1', 'exam-2019-2', 'exam-2022',
        'exam-2023-1', 'exam-2023-2', 'exam-2024', 'exam-2025'
    ]
    base_dir = '/home/justin/OneDrive/Université/H26/ISLA/previous-exams'
    for d in exam_dirs:
        full_path = os.path.join(base_dir, d)
        print(f"--- Processing {d} ---")
        print(process_exam_dir(full_path))
