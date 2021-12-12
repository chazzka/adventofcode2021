import numpy as np

input = np.genfromtxt('inputs/3.txt', delimiter=1, dtype=int)
ins = input.T

gamma = []
eps = []
for row in ins:
    unique, counts = np.unique(row, return_counts=True)
    dii = dict(zip(unique, counts))
    gamma.append(max(dii, key=dii.get))
    eps.append(min(dii, key=dii.get))

gamma = int("".join(str(x) for x in gamma), 2)
eps = int("".join(str(x) for x in eps), 2)


def getIndexesWithMajor(row, indexes):
    zeroIndexes = []
    oneIndexes = []
    for i in indexes:
        if row[i] == 0:
            zeroIndexes.append(i)
        else:
            oneIndexes.append(i)

    if len(zeroIndexes) > len(oneIndexes):
        return zeroIndexes
    else:
        return oneIndexes


def getIndexesWithMinor(row, indexes):
    zeroIndexes = []
    oneIndexes = []
    for i in indexes:
        if row[i] == 0:
            zeroIndexes.append(i)
        else:
            oneIndexes.append(i)

    if len(zeroIndexes) <= len(oneIndexes):
        return zeroIndexes
    else:
        return oneIndexes


# 2
indexes = range(len(ins[0]))
for row in ins:
    if len(indexes) == 1:
        break
    indexes = getIndexesWithMajor(row, indexes)

r = ins.T[indexes[0]]

result1 = int("".join(str(i) for i in r), 2)

indexes = range(len(ins[0]))
for row in ins:
    if len(indexes) == 1:
        break
    indexes = getIndexesWithMinor(row, indexes)

r = ins.T[indexes[0]]

result2 = int("".join(str(i) for i in r), 2)

print(result1 * result2)
