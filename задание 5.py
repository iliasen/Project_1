import os
my_dict = {
'Шины':['Беларусь', '5000', '8'],
'Корбюратор':['Бельгия', '15000', '5'],
'Двигатели V6 Mersedes-Benz W130':['Германия', '200000', '2']
}

def menu():
    print(
        "\tЧисто Армянский Вася магазин 'Автозапчасти от Хача'\n 1. Просмотр описания:\n 2. Просмотр цены: \n 3. Просмотр количества: \n 4. Вся информация\n 5. Покупка\n 6. Пока дорогой ! ")
    choice = int(input("Ваш выбор: "))
    return choice

while 1:
    choice = menu()
    if choice == 1:
        print("\033[H\033[J")
        print("-" * 55)
        print("|-----------------Название---------------|---Страна---|")
        print("-" * 55)
        for key, value in my_dict.items():
            print(f"|{key:<40}|{value[0]:<12}|")
            print("-" * 55)

    elif choice == 2:
        print("-" * 55)
        print("|-----------------Название---------------|----Цена----|")
        print("-" * 55)
        for key, value in my_dict.items():
            print(f"|{key:<40}|{value[1]:<12}|")
            print("-" * 55)

    elif choice == 3:
        print("-" * 55)
        print("|-----------------Название---------------|---Кол-во---|")
        print("-" * 55)
        for key, value in my_dict.items():
            print(f"|{key:<40}|{value[2]:<12}|")
            print("-" * 55, )


    elif choice == 4:
        print("-" * 78)
        print("|-----------------Название---------------|---Страна---|---Цена---|---Кол-во---|")
        print("-" * 78)
        for key, value in my_dict.items():
            print(f"|{key:<40}|{value[0]:<12}|{value[1]:<12}|{value[2]:<10}|")
            print("-" * 78)

    elif choice == 5:
        sum = 0
        count = 0
        flag = True
        flag1 = True
        while flag:
            name_product = input("Введите название продукта: ")
            amount = int(input("Введите кол-во: "))
            for key, value in my_dict.items():
                if name_product == key:
                    if amount > int(value[2]):
                        print(f"Такого количества товара нет на складе. В наличии {value[2]}. Просим прощения)")
                        flag1 = False
                    else:
                        sum += int(value[1]) * amount
                        break
                else:
                    count += 1
            if count == len(my_dict): print("Введенный товар не найден( ")
            print("Стоимость выбранных комплектующих = ", sum)
            while 1:
                ch = int(input("Выберите один из пунктов\n1. Добавить еще один товар в корзину\n2. Подтвердить покупку\n3. Отмена\n"))
                if ch == 1:
                    value[2] =int(value[2]) - amount
                    break
                elif ch == 2:
                    if flag1 == True:
                        print("Поздравляем с покупкой :)")
                        value[2] =int(value[2]) - amount
                        flag=False
                        break
                elif ch == 3:
                    flag = False
                    break
                else:
                    print("Введите пункт от 1 до 3:")
    elif choice == 6:
        break
    else:
        print("Ошибка ввода!\n")