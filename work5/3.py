#Печатаем игровое поле
def printPlayingField(list):
	for i in range(len(list)-2):
		if i == 0 or i == 3 or i == 6:
		    print(f"| {list[i]} | {list[i+1]} | {list[i+2]} |")
		

def replacement(list, imputPlayer, player):
    if player == 1:
        for index, item in enumerate(list):
            if item == imputPlayer:
                list[index] = "X"
        player +=1
    elif player == 2:
        for index, item in enumerate(list):
            if item == imputPlayer:
                list[index] = "O"
        player -=1

def examinationPrint(list, player):
    if list[0] == list[3] == list[6] or list[0+1] == list[3+1] == list[6+1] or list[0+2] == list[3+2] == list[6+2]:
        print(f"Выйграл игрок №{player}")
    elif list[0] == list[1] == list[2] or list[3] == list[4] == list[5]  or list[6] == list[7] == list[8]:
        print(f"Выйграл игрок №{player}")
    elif list[0] == list[4] == list[8] or list[2] == list[4] == list[6]:
        print(f"Выйграл игрок №{player}")

def examination(list, player):
    if list[0] == list[3] == list[6] or list[0+1] == list[3+1] == list[6+1] or list[0+2] == list[3+2] == list[6+2]:
        return 99
    elif list[0] == list[1] == list[2] or list[3] == list[4] == list[5]  or list[6] == list[7] == list[8]:
        return 99
    elif list[0] == list[4] == list[8] or list[2] == list[4] == list[6]:
        return 99           
	
      
print("Сыграем в игру крестики-нолики")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
printPlayingField(list)
counter = 1
player = 1
flag = True
while (flag):
    imputPlayer = int(input("Введите номер поля (от 1 до 9): "))
    while imputPlayer < 10 and flag:   
        replacement(list, imputPlayer, player)
        if player == 1:
            examinationPrint(list, player)
            if examination(list, player) == 99:
                flag = False
            player+=1
            if counter == 9:
                print('Ничья')
                flag = False
            counter +=1
        else:
            examinationPrint(list, player)
            if examination(list, player) == 99:
                flag = False
            player-=1
            if counter == 3:
                print('Ничья')
                flag = False
            counter +=1
        printPlayingField(list)
        break
    else:
        imputPlayer = int(input("!Введите номер поля (от 1 до 9): "))

        





