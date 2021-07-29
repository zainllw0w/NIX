def newRound(count):
    for num in count:
        if num.is_integer():
            print(num, ' -> ', round(num))
        else:
            print(num, ' -> ', round(num, 2))


myList = [22.32131, 58.60125, 34.0]


newRound(myList)