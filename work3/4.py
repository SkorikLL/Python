import math

def Zadacha4():
    # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    decimalNumber = int(input("Введите десятичное число: "))
    binaryNumber = str()
    rezult = decimalNumber
    while(rezult > 0 ):
        if rezult == 1:
            binaryNumber += "1"
            rezult = int(rezult / 2)   
        elif int(rezult) % 2 == 0:
            binaryNumber += "0"
            rezult = int(rezult / 2)
        elif int(rezult) % 2 != 0:
            binaryNumber += "1"
            rezult = int(rezult / 2)

    print (f"{decimalNumber} = {binaryNumber[::-1]}")
Zadacha4()