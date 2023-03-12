# Нахождения файла
file_path = "Work1/work8/fio.txt"

#Создаем меню
def menu(data):
    flag = True
    while flag:
        print("1. Вывести данны на экран")
        print("2. Сохранить данные")
        print("3. Добавить пользователя")
        print("4. Находим всех пользователей с определенной фамилией/имени: ")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        if cmd  == "1":
            screen(data)
        elif cmd == "2":
            write_date(data)
        elif cmd == "3":
            add_user(data)
            while True:
                print("Вы хотите сохранить файл?: ")
                print("1. Да")
                print("2. Нет")
                cmd = input("Выберите пункт: ")
                if cmd  == "1":
                    write_date(data)
                    break
                elif cmd == "2":
                    break
                else:
                    print("Вы ввели не правильное значение")
        elif cmd == "4":
            search(data)
        elif cmd == "0":
            flag = False
        else:
            print("Вы ввели не правильное значение")

#Вывести на экран
def screen(data):
    for elem in data:
        print(elem)

#Записывает данные
def write_date(data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(data)

#Считывает данные
def read_date():
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        return(data)

def change():
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = data.replace("123", "!!!")

# Поиск по справочнику.
def search(data):
    flag = 1
    name = input('имя/фамилия > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')

#Добавляем пользователя
def add_user(data):
    data.append('\n' + input("Добавьте пользователя: "))

def main():
    data = read_date()
    menu(data)

if __name__ == '__main__':
    main()