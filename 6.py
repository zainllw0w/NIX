striings = 'Денис, Олег, Вася, Петя,Дима,Женя'
newstr = ''
myList = []

for i in striings:
    if i.isalpha():
        newstr += i
    else:
        if newstr != '':
            myList.append(newstr)
        newstr = ''



print(myList)