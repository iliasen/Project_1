import random
a=[random.randint(0,9) for i in range(9)]
print(*a)
for i in a:
    my_dict={ i:a.count(i) }
    print(my_dict.items())