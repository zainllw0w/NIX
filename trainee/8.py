def my_generator(start, end):
    for elem in range(start, end + 1):
        yield elem


for i in my_generator(1, 3):
    print(i)