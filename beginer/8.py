import random


good = True
for _ in range(100):
    n = random.randint(1,1000)
    if n == 777:
        print('Ура все случилось на попытке №', _)
        good = False
        break
    else:
        print(f'выпало число {n}')

if good:
    print('Сорри бро но чсло 777 из 100 попыток так и не выпало!')
