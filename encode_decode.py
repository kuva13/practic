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

res = np.dot(message, G) % 2
print(res)
