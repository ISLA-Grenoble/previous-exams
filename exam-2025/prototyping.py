import numpy as np
import matplotlib.pyplot as plt

def read_adjacency_matrix(file_path):

    with open(file_path) as f:
        l = [line.rstrip() for line in f]

    A = np.zeros((34, 34))
    for li in l:
        li = li.split('] [')
        for lij in li:
            lij_int = [int(x) for x in lij.strip('[]').split()]
            if len(lij_int) == 2:
                A[lij_int[0]-1, lij_int[1]-1] = 1
                A[lij_int[1]-1, lij_int[0]-1] = 1  
    
    return A

file_path = './karate_graph.txt'
A = read_adjacency_matrix(file_path)
D = np.sum(A, axis=1)
F = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
m = np.sum(A) / 2

S = 2 * (F - 1) - 1
B = A - np.outer(D, D) / (2 * m)
Q = S.T @ B @ S
print(Q)

w, v = np.linalg.eig(B)
idx = np.argsort(w)[::-1]
w = w[idx]
v = v[:, idx]
v1 = np.real(v[:, 0])
S1 = -1*np.sign(v1)

Q = S1.T @ B @ S1
print(Q)