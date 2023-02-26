def Zadacha1():
    # Вычислить число Пи c заданной точностью d
    # Пользуюсь методом Ряд Лейбница
    pi = 0
    counter = 0
    accuracy = int(input("Сколько знаков должно быть после запятой: "))
    number = 100000001
    #Для большой точности чила Пи можно увеличить number
    for i in range(1, number, 2):
        if counter % 2 == 0:
            pi += 4/i
            counter +=1
        else:
            pi -= 4/i
            counter +=1
    print(f'Число x: {str(pi)[:accuracy+2]}')

Zadacha1()