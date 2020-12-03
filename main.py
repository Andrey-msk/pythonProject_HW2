# 1
my_list = ["Bmw", 7, None, True, 55.8, ('x','5','6'), {'Apple': 'Iphone'}]
for i in my_list:
    print(f'{i} is {type(i)}')

# 2
el_count = int(input("Введите количество элементов "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for element in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

# 3
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])

# 3.1
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))

# 4
my_str = input("Введите несколько слов через пробел: ")
a = my_str.split(" ")
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

# 5
number = int(input("Введите номер: "))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

# 6
goods = []
features = {'Название товара': '', 'Цена': '', 'Колличество': '', 'Еденица измерения': ''}
analytics = {'Название товара': [], 'Цена': [], 'Колличество': [], 'Еденица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Чтобы продолжить нажмите 'Enter', Для Аналитики нажмите 'A'").upper()
    num += 1
    if control == 'A':
        print(f'\n Данная Аналитика \n ')
        for key, value in analytics.items():
            print(f'{key[:55]:>20}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите "{f}"')
        features[f] = int(feature_) if (f == 'Ценна' or f == 'Количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
