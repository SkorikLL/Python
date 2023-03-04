number = int(input("Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.\n1 - реализуйте модуль сжатия\n2 - восстановления данных\nВведите число 1 или 2: "))
compressed = str()


if number == 1:
    text = str(input("Введите текст где будет реализуйте модуль сжатия: "))
    cout = 1
    for i in range(len(text)-1):
        if i <=len(text):
            if text[i] == text[i + 1]:
                cout += 1
            else:
                compressed = compressed + str(cout) + text[i]
                cout = 1
    compressed = compressed + str(cout) + text[i]
    print (compressed)
elif number == 2:
    cout = ''
    text = str(input("Введите текст где будет восстановления данных: "))
    for i in range(len(text)):
        if text[i].isdigit():
            cout += text[i]
        else:
            cout = int(cout)
            compressed += cout * text[i]
            cout = ''
    print (compressed)