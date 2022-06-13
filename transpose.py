import numpy as np
from numpy import *

# text = open('ldpc_reg6.txt', 'r').readlines()
# lines = []
# for line in text:
#     lines.append(line.split())

# for i in lines:
#     for ind, j in enumerate(i):
#         i[ind] = int(j)

# H = np.array(lines)
# H = np.array([[1, 1, 0, 1, 1, 0, 0, 1, 0, 0], 
#               [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
#               [0, 0, 0, 1, 0, 0, 0, 1, 1, 1], 
#               [1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
#               [0, 0, 1, 0, 0, 1, 0, 1, 0, 1]])

G = np.array([[1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 0, 1],
                [0, 0, 1, 0, 0, 1, 1],
                [0, 0, 0, 1, 1, 1, 1]])

S = np.array([[1, 1, 0, 1],
                 [1, 0, 0, 1],
                 [0, 1, 1, 1],
                 [1, 1, 0, 0]])

H = np.array([[0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0]])

matrix = np.dot(S, G) % 2

G = np.dot(matrix, H) % 2

# text = open('arreduced_mod.txt', 'r').readlines()
# lines = []
# for line in text:
#     lines.append(line.split())

# for i in lines:
#     for ind, j in enumerate(i):
#         i[ind] = int(j)

# G = np.array(lines)

G_t = np.transpose(G)

multiply = np.dot(H, G_t) % 2

with open('multiply.txt', 'w') as f:
    np.savetxt(f, multiply, fmt='%d')
    print("Multiply matrix in multiply.txt file")
    
#print(np.linalg.det(multiply))