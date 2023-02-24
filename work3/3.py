def Zadacha3():
    # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

    #Созданм список из нескольких чисел
    list = [1.1, 1.2, 3.1, 5, 10.01]
     #Создаем новый список где будет храниться только дробная часть
    listFraction =[]
    print(f"Список чисел: {list}")
    for i in range(len(list)):
        if round(list[i] - int(list[i]), 2) !=0:
            #listNew.append(list[i]%1)
            listFraction.append(round(list[i] - int(list[i]), 2))
    print(f"Новый список: {listFraction}")
    print(f"Разницу между максимальным и минимальным значением дробной части элементов: {max(listFraction) - min(listFraction)}") 
    
Zadacha3()