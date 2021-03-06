'''
Автор: Л. Шастин

Дана последовательность из N натуральных чисел. Рассматриваются все её непрерывные подпоследовательности, начальное число
в которых делится на 21 и является квадратом конечного числа. Найдите среди них подпоследовательность с максимальной длиной.
Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N (2 ≤ N ≤ 10^8).
Каждая из следующих N строк содержит натуральное число, не превышающее 10000.
Пример входного файла:
7
441
1764
21
19
17
42
95
В этом наборе можно выбрать последовательности (441-21) и (1764-42), длина первой = 3, второй = 5. Ответ: 5.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
'''

f = open('27-79b.txt')
n = int(f.readline())
nums = [0]*(10**5)
lens = [0]*(10**5)
lmax = -1
for j in range (n):
    x = int(f.readline())
    if x % 21 == 0:
        if nums[x] == 0:
            nums[x] = x
            lens[x] = j - 1
        if x**2 < 10001:
            if nums[x**2] != 0:
                l = j - lens[x**2]
                lmax = max(l, lmax)
print(lmax)

#Ответ: А) 337 ; Б) 148613
