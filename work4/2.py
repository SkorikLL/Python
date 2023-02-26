def Zadacha2():
    # Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
    n = int(input("Введите натуральное число: "))
    givenNaturalNumber = n
    my_set = set()
    i = 2
    while(int(n) > 1):
        if n % i == 0:
            n /= i
            my_set.add(i)
            i = 2
        else:
            i +=1  
    print(f"Cписок простых множителей {givenNaturalNumber}: {my_set}")

Zadacha2()