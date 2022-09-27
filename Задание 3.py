print('Вводите значения, нажимайте enter')
print('для окончания ввода просто нажмите enter')
a = int(input('-->> '))
words = []
while True:
    try:
        words.append(a)
        a = int(input('-->> '))
    except:
        break
print(words)

store = 0
for k in range(0, max(words)+1):
    m=0
    for i in words:
        if k == i:
            m+=1
    print("Чисел",k,"в ряду:",m)
    for i in range(m//2):
        store += 1
print("Пар: ", store)
