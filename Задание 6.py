from  random import random, randint
a=tuple([randint(-9,9)+ round(random(),2) for i in range(20)])
print(a)
k=0
for i in a:
    if i<0:
        break
    k+=1
print("Индекс отрицательного эллемента: ",k)