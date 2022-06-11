file = open('../../задачи/27/27data/1/27-1b.txt')

maxim = 0
maxim_rzn = 999999999
n = int(file.readline())
for i in range(n):
    a, b = map(int, file.readline().split())
    maxim += min(a, b)
    if abs(a-b)%3 != 0:
        maxim_rzn = min(maxim_rzn, abs(a-b))

if maxim%3==0:
    print(maxim+maxim_rzn)
else:
    print(maxim)