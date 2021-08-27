my_list =  [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]

my_list.sort(key=lambda a: a['age'])

print(my_list)