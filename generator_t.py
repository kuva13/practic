import random

t = [0] * 9

for i in range(51):
    if i % 5 == 0:
        t.append(random.randint(0, 1))
    else:
        t.append(0)
while len(t) != 256:
    t.append(0)

print(t)
