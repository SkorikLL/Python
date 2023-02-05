def Zadacha1():
    #Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    print("Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
    number = float(input("Введите число: "))
    sum = 0
    number = str(number)
    for i in range(len(number)):
        if number[i] !=  ".": 
            sum = sum + int(number[i])
    
    print(f"{number} = {sum}")

Zadacha1()