def Zadacha2():
    # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    #Созданм список из нескольких чисел
    list = [2, 3, 4, 5, 6]
    print(f"Список чисел: {list}")
    #Список где будут хранится произведение пар чисел списка list.
    listNew = []
    sumList = int(0)
    #Пробегаем по всему списку
    if len(list) % 2 == 0:
        for i in range(int(len(list) / 2)):
            sumList = list[i] * list[-1 - i]
            listNew.append(sumList)
    else:
        for i in range(int(len(list) / 2 + 1)):
            if list[i] == list[-1 - i]:
                listNew.append(list[i] * list[i])
            else:    
                sumList = list[i] * list[-1 - i]
                listNew.append(sumList)
    
    print(f"Произведение пар чисел из списка: {listNew}")
    
Zadacha2()