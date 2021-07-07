my_number = input()
print(my_number.count('0'))
##########################################################
str_number = my_number
zero_count = len(str_number) - len(str_number.rstrip('0'))
print(zero_count)
##########################################################