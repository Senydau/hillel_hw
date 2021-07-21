my_list = ['qwe', 'qwe', 'qwe', 'qwe']
res = []
for index in range(len(my_list)):
    if not index % 2:
        res = my_list
        res[index] = res[index][::-1]

print(res)
########################################################
my_list = ['Avatar', 'vsdfsdf', 'fsdfg', 'amogus']
new_list = []
for i in my_list:
    my_list.append(i.lower())
    break
for i in my_list:
    if i.startswith('a'):
        new_list.copy()
        new_list.append(i)

print(new_list)
########################################################
my_list = ['clumba', 'lavanda', 'lilia', 'pink', 'blue']
new_list = []
for i in my_list:
    if 'a' in i:
        new_list.copy()
        new_list.append(i)
print(new_list)
########################################################
my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for i in my_list:
    if type(i) == str:
        new_list.copy()
        new_list.append(i)
print(new_list)
########################################################
my_str = 'qwertyqwertyios'
new_list = ''
res = []

for i in range(len(my_str)):
    if not my_str.count(my_str[i]) > 1:
        new_list += my_str[i]

for i in range(len(new_list)):
    res.append(new_list[i:i + 1])
print(res)
print(new_list)
########################################################
my_str_1 = '321qwertyqwertyios1q'
my_str_2 = '321qwertyqwerty'

res = set(my_str_1) & set(my_str_2)
res = sorted(res)

print(res)
########################################################
my_str_1 = "Гарри Поттер и Филосовский камень "
my_str_2 = "Гарри Поттер и Тайная комната"

my_str_1 = my_str_1.lower()
my_str_2 = my_str_2.lower()
print(my_str_1, my_str_2)
res = []
for i in my_str_1:
    k = my_str_1.find(i) - my_str_1.rfind(i)
    if k == 0:
        if i in my_str_2 and my_str_2.find(i) - my_str_2.rfind(i) == 0:
            res.append(i)
print(res)
########################################################
dict = {'first_name': 'Sam',
        'last_name': 'Vaunt',
        'age': '19',
        'place': ['Ukraine', 'Dnepr', 'Smidta'],
        'Job': ['are available', 'Trainee']}
print(dict)
########################################################
cake = {'Составляющие': {
    'Коржи': ['Мука: 200гр', 'Молоко: 150гр', 'Масло: 30гр', 'Яйцо: 1'],
    'Крем': ['Сахар: 150гр', 'Масло: 30гр', 'Ваниль: 15гр', 'Сметана: 100гр'],
    'Глазурь': ['Какао: 50гр', 'Сахар: 100гр', 'Масло: 40гр']
}
}
print(cake)
