value = int(input('Введите целое число: '))
new_value = (value / 2) if value < 100 else (value * (-1))
print(new_value)
##########################################################################
value = int(input('Введите целое число: '))
new_value = 1 if value < 100 else 0
print(new_value)
##########################################################################
value = int(input('Введите целое число: '))
new_value = True if value < 100 else False
print(new_value)
##########################################################################
my_str = input('Введите строку и она будет написана большими буквами: ')
my_str = my_str.upper()
print(my_str)
##########################################################################
my_str = input('Введите строку и она будет написана маленькими буквами: ')
my_str = my_str.lower()
print(my_str)
##########################################################################
my_str = input('Введите любую строку: ')
my_str = my_str + my_str if len(my_str) < 5 else my_str
print(my_str)
##########################################################################
my_str = input('Введите любую строку: ')
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)