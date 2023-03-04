print("Напишите программу, удаляющую из текста все слова, содержащие ""абв"".")
text = input("Введите текст: ")
del_text = "абв"
lst = [i for i in text.split() if del_text not in i]
print(f'Результат: {" ".join(lst)}')