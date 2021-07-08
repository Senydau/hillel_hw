# my_list = ['qwe', 'qwe', 'qwe', 'qwe']
# for i in range(len(my_list)):
#   if not i % 2:
#       my_list[i] = my_list[i][::-1]
#
# print(my_list)
########################################################
# my_list = ['Avatar', 'vsdfsdf', 'fsdfg', 'amogus']
# new_list = []
# for i in my_list:
#     my_list.append(i.lower())
#     break
# for i in my_list:
#     if i.startswith('a'):
#         new_list.copy()
#         new_list.append(i)
#
# print(new_list)
########################################################
# my_list = ['clumba', 'lavanda', 'lilia', 'pink', 'blue']
# new_list = []
# for i in my_list:
#     if 'a' in i:
#         new_list.copy()
#         new_list.append(i)
# print(new_list)
########################################################
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for i in my_list:
#     if type(i) == str:
#         new_list.copy()
#         new_list.append(i)
# print(new_list)
########################################################
my_str = 'qwertyuiopasdfghjlqwertyukzxcvbmzxcvbmmn'
new_list = list(my_str)
for i in new_list:
    if i == i:
        res = i + i
        new_list.append(res)
print(new_list)
