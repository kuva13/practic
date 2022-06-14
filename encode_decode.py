import numpy as np

text = open('message.txt', 'r').readlines()
message = list(text[0])  # сообщение вида ['0', '1', '0', '0', '1', ...]
message = [int(item) for item in message]


text = open('arreduced_mod.txt', 'r').readlines()
lines = []
for line in text:
    lines.append(line.split())

for i in lines:
    for ind, j in enumerate(i):
        i[ind] = int(j)

G = np.array(lines)

text = open('ldpc_reg6.txt', 'r').readlines()
lines = []
for line in text:
    lines.append(line.split())

for i in lines:
    for ind, j in enumerate(i):
        i[ind] = int(j)
 
H = np.array(lines)       
        
cipher = np.dot(message, G) % 2
print(cipher)

H_1 = np.linalg.pinv(H) % 2

decode = np.dot(cipher, H_1) % 2
print(decode)

P =     np.array([[0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0]])

P_1 = np.linalg.inv(P) % 2
P_2 = np.linalg.inv(P_1) % 2
print(P_1)
print(P_2)
C =     np.array([[0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0]])

C_1 = np.linalg.pinv(C) % 2
C_2 = np.linalg.pinv(C_1) % 2
print(C_1)
print(C_2)