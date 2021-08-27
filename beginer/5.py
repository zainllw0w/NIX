def func(num, myList):
    newList = list()
    y = 0

    if len(myList) == 0:
        print('Нет элементов')
    elif len(myList) < num:
        print('Количество элементов в списке меньше указанного')

    else:
        for i in range(num):
            newList.append([])
        for i in myList:
            if y == num:
                y = 0
            newList[y].append(i)
            y += 1
    return newList


number = int(input('Введите число: '))
myList = [1, 2, 3]

print(func(number, myList))
