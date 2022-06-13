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


with open('ldpc_reg5.txt', 'r') as f:
    A = [[int(num) for num in line.split(',')] for line in f]

A = np.array(A)

#print(A)
Areduced, jb = rref(A)
print(f"The matrix as rank {len(jb)}")
with open('arreduced.txt', 'wb') as f:
    np.savetxt(f, Areduced, fmt='%d')
    print("Arreduced matrix in arreduced.txt file")

Areduced_mod = []
for row in range(len(Areduced)):
    temp = []
    for elem in Areduced[row]:
        temp.append(elem % 2)
    Areduced_mod.append(temp)

with open('arreduced_mod.txt', 'wb') as f:
    np.savetxt(f, Areduced_mod, fmt='%d')
    print("Arreduced matrix in arreduced_mod.txt file")