def refactor(l1, l2):
    return [x for x in l1 if x not in l2]


list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4]

print(refactor(list1,list2))