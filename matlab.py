import numpy as np


def decryptSuccess(plaintext, decryptedText):  # возвращает 1 если откр текст == расшифр текст, иначе 0
    status = np.array_equal(plaintext, decryptedText)

    return status


def genRandomVector(k, t):  # k - размерность вектора, t - вес хэмминга вектора => случайный вектор wth=t, size = k
    randomVector = np.zeros(k, dtype=np.int32)

    # pick t random positions out of k positions
    randomPositions = np.random.choice(k, t, replace=False)

    # assign the random positions the value 1
    for j in randomPositions:
        randomVector[j] = 1

    return randomVector


def convertBinary(v):  # на входе целоч массив v, на выходе v mod 2
    for i in range(len(v)):
        v[i] = v[i] % 2

    return v


def encryptMcEliece(G, m, e):  # получение зашифрованного сообщения
    rows, cols = G.shape
    n = cols
    r = cols - rows

    # encryption follows research paper, ciphertext = m*G + e
    ciphertext = np.copy(np.add(np.matmul(m, G), e))

    ciphertext = convertBinary(ciphertext)

    return ciphertext


def demo(H, y):  # выводит расшифрованный текст y'
    r, n = H.shape
    w = sum(H[0, :] == 1)
    d = w // 2
    iteration = 1
    flipped = 1

    s = convertBinary(np.matmul(y, np.transpose(H)))

    while (np.count_nonzero(s) > 0 and flipped == 1):
        flipped = 0
        # syndrome weight
        T = 1

        for j in range(n):
            if (sum((s + H[:, j]) == 2)) >= T * d:
                y[j] = y[j] ^ 1
                s = convertBinary(np.matmul(y, np.transpose(H)))
                flipped = 1

        iteration += 1

        # syndrome
        s = np.matmul(y, np.transpose(H))
        s = convertBinary(s)

    if (sum(s == 1) == 0):
        return y[0: n - r]
    else:
        return 0


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

    return A, jb


text = open('ldpc_reg5.txt', 'r').readlines()
lines = []
for line in text:
    lines.append(line.split())

for i in lines:
    for ind, j in enumerate(i):
        i[ind] = int(j)

H = np.array(lines)
idx = list(range(int(np.shape(H)[1] / 2), np.shape(H)[1])) + list(range(0, int(np.shape(H)[1] / 2)))

Areduced, jb = rref(H)

Areduced_mod = []
for row in range(len(Areduced)):
    temp = []
    for elem in Areduced[row]:
        temp.append(elem % 2)
    Areduced_mod.append(temp)

Areduced_mod = np.array(Areduced_mod)
Hstd = Areduced_mod[:, idx]

M = np.shape(H)[0]  # N-K
N = np.shape(H)[1]
K = N - M

G = np.concatenate([np.eye(K), ((-1)*Hstd[:, :K].T % 2)], axis=1)
G = G.astype("int")

m = genRandomVector(len(lines), len(lines) // 2)  # открытый текст

success = 0
fails = 0

for i in range(5):
    e = genRandomVector(256, 2)  # второе значение - количество ошибок

    # encrypt the message m
    y = encryptMcEliece(G, m, e)

    # decrypt the ciphertext
    decryptedText = demo(Hstd, y)

    # check if decryption is correct
    if decryptSuccess(m, decryptedText):
        success += 1
    else:
        fails += 1
print('Number of successes: {} & fails: {} & {} %'.format(success, fails, 100*success/(success+fails)))
