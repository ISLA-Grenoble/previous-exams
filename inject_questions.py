import os
import json
import re
import glob

def parse_questions_md(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Normalize line endings
    content = content.replace('\r\n', '\n')
    
    # Split by headers like ## Part X or ## Exercise X
    # Use a lookahead/lookbehind or just find all headers and split
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
            # We look for markers: **Q1.**, **(a)**, **Q1 — Title**, etc.
            # We'll use a regex that looks for bold text at the start of a line or after some whitespace
            q_pattern = r'\n(\*\*(?:Q\d+|(?:\([a-z]\))|Q\d+\s+—).*?\*\*)'
            q_starts = list(re.finditer(q_pattern, part_content, re.DOTALL))
            
            if not q_starts:
                # Try another pattern for (a), (b), (c)
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

def inject_into_notebook(nb_path, questions):
    if not questions:
        return
        
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    updated_cells = []
    q_idx = 0
    
    # Keep track of which questions we've already injected to avoid duplicates
    injected_questions = set()

    for cell in nb['cells']:
        cell_text = "".join(cell['source']).lower()
        
        # If we have questions left
        if q_idx < len(questions):
            # We might have multiple questions matching one cell (e.g. if questions are grouped)
            # or we might have one question matching multiple cells.
            
            # Find the best match
            matched = False
            for i in range(q_idx, len(questions)):
                q_text = questions[i]
                m = re.search(r'(Q\d+|(?:\([a-z]\)))', q_text)
                if m:
                    marker = m.group(1).lower()
                    # Check if cell contains the marker and looks like a question header
                    if marker in cell_text and (
                        'question' in cell_text or 
                        '##' in cell_text or 
                        '**' in cell_text or 
                        (len(cell_text.strip()) < 50 and marker in cell_text.strip())
                    ):
                        # Inject all questions from q_idx to i
                        for k in range(q_idx, i + 1):
                            if questions[k] not in injected_questions:
                                new_q_cell = {
                                    "cell_type": "markdown",
                                    "metadata": {},
                                    "source": [questions[k] + "\n"]
                                }
                                updated_cells.append(new_q_cell)
                                injected_questions.add(questions[k])
                        q_idx = i + 1
                        matched = True
                        break
        
        updated_cells.append(cell)
    
    # If some questions were not matched, maybe they belong to the end?
    # Or we failed to find anchors.
    # The instruction says "use the code content to infer where the question belongs" if no anchors.
    # This is harder. For now, let's see how the anchor-based works.
    
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
        # Try to map nb_name to part_num
        m = re.search(r'Part(\d+)', nb_name)
        if m:
            part_num = int(m.group(1))
            if part_num in parts:
                inject_into_notebook(nb_path, parts[part_num])
                results.append(f"Updated {nb_name} with Part {part_num} questions")
            else:
                results.append(f"No questions found for Part {part_num} in {nb_name}")
        elif nb_name == 'correction.ipynb':
             # For correction.ipynb, it often contains all parts
             all_qs = []
             for p in sorted(parts.keys()):
                 all_qs.extend(parts[p])
             inject_into_notebook(nb_path, all_qs)
             results.append(f"Updated {nb_name} with all questions")
        elif len(notebooks) == 1:
             # If it's the only notebook, it might be Part 1 or all parts
             all_qs = []
             for p in sorted(parts.keys()):
                 all_qs.extend(parts[p])
             inject_into_notebook(nb_path, all_qs)
             results.append(f"Updated {nb_name} with all questions")
        else:
            results.append(f"Skipping {nb_name}: could not map to a part")
            
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
