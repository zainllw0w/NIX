def reg(myList):
    return [x.upper() if x.find('price') >= 0 else x for x in myList]


myList = ['asdasd', 'asdpriceasd', 'price', 'asd price asda']


print(reg(myList))




