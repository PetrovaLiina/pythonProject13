a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
a += a % 2 + 1
b += b % 2 - 1
for i in range(a, b+1, 2):
    print(i)
