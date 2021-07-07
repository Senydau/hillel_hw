my_list = [10, 23, 125, 70, 60, 752]

for element in my_list:
    if element > 100:
        print(element)
    else:
        pass
##################################################################
my_list = [10, 23, 125, 70, 60, 752]
my_result = []
for element in my_list:
    if element > 100:
        my_result.append(element)
    else:
        pass
print(my_result)
##################################################################
# my_list = [1]
# if len(my_list) < 2:
#     my_list.append(0)
# else:
#     pass
# print(my_list)
my_list = [1, 23, 42, 63, 32]
if len(my_list) >= 2:
    my_value_list = my_list[-1] + my_list[-2]
    print(my_value_list)
else:
    my_list.append(0)
    print(my_list)

##################################################################
while True:
    value = input('Введите число с плавающей точкой: ')
    try:
        value = float(value)
        value = value ** -1
        break
    except ValueError:
        print('Вы ввели что-то не так!')
    except ZeroDivisionError:
        print('Введи не ноль!')
print('Ваше число в -1 степени: ' + str(value))
##################################################################
my_string = '0123456789'
result = []

for symb1 in my_string:
    for symb2 in my_string:
        s_res = int(symb1 + symb2)
        result.append(s_res)

print(sorted(result))
