a, n = int(input("Введите начало диапазона: ")), int(input("Введите кацец диапазона: "))
flag = 0
for i in range(a,n):
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i, end=' ')
        flag = 1
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i, end=' ')
        flag = 1
if flag == 0:
    print("Простых чисел в данном диапозоне нет")
