def Zadacha3():
    # Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
    list = input("Введите числа через пробел: ")
    print(f"Список чисел: {list}")
    # Списке где будут хранится неповторяющихся элементов 
    my_set = set(list)
    print(f"Список неповторяющихся элементов: {my_set}")

Zadacha3()