import itertools
file = open('../../задачи/27/27data/55/27-55b.txt')
spis = sorted(map(int, file.read().split('\n')[1:]))
spis = spis[:100]
minsumm = 1e10
for i in itertools.combinations(spis, 4):
    if (i[0]+i[1]+i[2]+i[3]) %4 == 0:
        minsumm = min(i[0]+i[1]+i[2]+i[3], minsumm)
print(minsumm)