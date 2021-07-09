my_number = input()
print(my_number.count('0'))
####################################################################
str_number = my_number
zero_count = len(str_number) - len(str_number.rstrip('0'))
print(zero_count)
####################################################################
my_list_1 = [1, 3, 5, 7]
my_list_2 = [2, 4, 6, 8]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)
####################################################################
my_list = [1, 2, 3, 4]
my_list_ind = [my_list[0]]
new_list = my_list[1::] + my_list_ind
print(new_list)
####################################################################
my_list = [1, 2, 3, 4]
print(id(my_list))
my_list.append(my_list.pop(0))
print(id(my_list), my_list)
####################################################################
my_str = '32 больше чем 12 но меньше чем 95'
elem_my_str = my_str.split()
my_numb = []
for sub_num in elem_my_str:
    if sub_num.isdigit():
        my_numb.append(int(sub_num))
sum_num = sum(my_numb)
print(sum_num)
####################################################################
my_str = "My long string"
l_limit = "o"
r_limit = "g"
ind_l = my_str.find(l_limit)
ind_r = my_str.rfind(r_limit)
sub_str = my_str[ind_l + 1:ind_r]
print(sub_str)
####################################################################
my_str = input('Введите строку: ')
my_str = my_str.replace(' ', '')
par_str = []
if len(my_str) != 0 and len(my_str) % 2:
    my_str += '_'
else:
    print('Вы ввели что-то не так')
for index in range(0, len(my_str), 2):
    par_str.append(my_str[index:index+2])
print(par_str)
####################################################################
list_num = [2, 4, 1, 5, 3, 9, 0, 7]
res_list = []
for index in range(1, len(list_num) - 1):
    if list_num[index] > list_num[index - 1] + list_num[index + 1]:
        res_list.append(list_num[index])
res = len(res_list)
print(res)
