def finder(file):
    catches_list = []
    for line in file:
        if 'catch me' in line:
            print(line)
            catches_list.append(line)
    return f' количество отловленных строк: {len(catches_list)}'


file = open('text.txt', 'r')

print(finder(file))
file.close()