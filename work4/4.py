import random
from random import randint

def Zadacha4():
    # Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать 
    # в файл многочлен степени k.

    k = int(input("Введите натуральное число: "))
    list = []
    plusMinus = ["+", "-"]
    stroka = str()
    counter = k
    randomNumber = 0
    for i in range(k):
        randomNumber = randint(0, 100)
        list.append(randomNumber)

    for i in range(len(list)):
        if list[i] == 0:
            stroka += str(list[i])
            counter -= 1
        elif counter == 1:
            stroka += str(list[i])
            counter = int(counter) 
            counter -= 1                 
        else:
            stroka += str(list[i]) + "x^" + str(counter)+ plusMinus[randint(0, 1)] 
            counter = int(counter) 
            counter -= 1           
    print(stroka) 



Zadacha4()