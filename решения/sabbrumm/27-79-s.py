file = open('../../задачи/27/27data/29/27-29b.txt')
n = int(file.readline())
summ = 0
max_crat = 9999999999
for i in range(n):
    a,b,c = map(int, file.readline().split())
    summ+= max(a+b, b+c, a+c)
    if abs(a-b)%5 != 0:
        max_crat = min(max_crat, abs(a-b))
    if abs(a-c)%5 != 0:
        max_crat = min(max_crat, abs(a-c))
    if abs(b-c)%5 != 0:
        max_crat = min(max_crat, abs(b-c))
if summ%5 == 0:
    print(summ-max_crat)
else:
    print(summ)
