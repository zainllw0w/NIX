def the_filter(list_name):
    """
    Меняет существующий список
    """
    list_name[:] = [elem for elem in list_name if elem['name'][0] == 'A' and 18 <= elem['age'] <= 30]


list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]


the_filter(list_)
print(list_)

