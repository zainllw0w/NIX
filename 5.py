def func(num, myList):
    newList = list()
    if len(myList) < num:
        print('Не может быть разбита больше чем есть в списке!')
    else:
        for i in range(num):
            newList.append([myList[i]])
    return newList


number = int(input('Введите число: '))
myList = [123, 415, 34534]

print(func(number, myList))



