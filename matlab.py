import numpy as np
from numpy import *

def rref(A, tol=1.0e-12):
    m, n = A.shape
    i, j = 0, 0
    jb = []

    while i < m and j < n:
        # Find value and index of largest element in the remainder of column j
        k = np.argmax(np.abs(A[i:m, j])) + i
        p = np.abs(A[k, j])
        if p <= tol:
            # The column is negligible, zero it out
            A[i:m, j] = 0 
            j += 1
        else:
            # Remember the column index
            jb.append(j)
            if i != k:
                # Swap the i-th and k-th rows
                A[[i, k], j:n] = A[[k, i], j:n] 
            # Divide the pivot row i by the pivot element A[i, j]
            A[i, j:n] = (A[i, j:n] / A[i, j]) 
            # Subtract multiples of the pivot row from all the other rows
            for k in range(m):
                if k != i:
                    A[k, j:n] -= (A[k, j] * A[i, j:n]) 
            i += 1
            j += 1
    # Finished
    return A, jb


text = open('ldpc_reg6.txt', 'r').readlines()
lines = []
for line in text:
    lines.append(line.split())

for i in lines:
    for ind, j in enumerate(i):
        i[ind] = int(j)

H = np.array(lines)
idx = list(range(int(np.shape(H)[1] / 2), np.shape(H)[1])) + list(range(0, int(np.shape(H)[1] / 2)))
print(idx)

Areduced, jb = rref(H)


Areduced_mod = []
for row in range(len(Areduced)):
    temp = []
    for elem in Areduced[row]:
        temp.append(elem % 2)
    Areduced_mod.append(temp)

with open('arreduced_mod.txt', 'wb') as f:
    np.savetxt(f, Areduced_mod, fmt='%d')
    print("Arreduced matrix in arreduced_mod.txt file")

Areduced_mod = np.array(Areduced_mod)
Hstd = Areduced_mod[:, idx]

M = np.shape(H)[0]  # N-K
N = np.shape(H)[1]
K = N - M

G = np.concatenate([np.eye(K), ((-1)*Hstd[:, :K].T % 2)], axis=1)

text = open('message.txt', 'r').readlines()
message = list(text[0])  # сообщение вида ['0', '1', '0', '0', '1', ...]
message = [int(item) for item in message]

x = np.array(message) @ G % 2
