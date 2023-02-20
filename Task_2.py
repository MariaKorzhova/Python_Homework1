# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите трёхзначное число: ")
number = input()
if len(number) == 3:
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    sum = a + b + c
    print(sum)
else:
    print("Введено нетрёхзначное число")