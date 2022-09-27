str = input("Введите строку: ")
str = str.lower()
n = len(str)
glas = "аоеёюяиыэ"
sogl = "йцкнгшщзхъфвпрлджчсмтьб"
words = " "
g = 0
s = 0
w = 1
for i in str:
    if i in glas:
        g += 1
    if i in sogl:
        s += 1
    if i == " ":
        w += 1
print("Гласных букв: ", g)
print("Согласных букв: ", s)
print("Количество слов: ", w)
