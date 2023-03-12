#Считает количество гласных букв в каждой фразе
def countVowels(text):
    count = 0
    vowels = []
    for i in range(len(text)):
        res = list(text[i])
        for i in range(len(res)):
            if res[i] == "а" or res[i] == "о" or res[i] == "и" or res[i] == "ы" or res[i] == "у" or res[i] == "э" or res[i] == "я" or res[i] == "ю" or res[i] == "ё":
                count +=1 
        vowels.append(count)
        count = 0   
    return vowels

#пара-ра-рам рам-пам-папам па-ра-па-дам"
data = input("Введите стихотворение: ")
data = list(data.split())
countVowels(data)
vowels_res = countVowels(data)
print(f"Количество гласных букв: {vowels_res}")
res = all(x == vowels_res[0] for x in vowels_res)
if res == True:
    print("Парам пам-пам")
else:
    print("Пам парам")

