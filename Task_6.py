# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

print("Введите шестизначное число: ")
number = input()
if len(number) == 6:
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    d = int(number[3])
    e = int(number[4])
    f = int(number[5])
    sum1 = a + b + c
    sum2 = d + e + f
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
else:
    print("Введено не шестизначное число")
