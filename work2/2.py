def Zadacha2():
    #Задача 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    print("Задача 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")
    N = int(input("Введите число N: "))
    sum = 1
    for i in range(1, N + 1):
        sum = sum * i
        print(f"{i}: {sum} ")
    
Zadacha2()