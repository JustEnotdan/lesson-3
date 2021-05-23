def thesaurus(*name):
    dct1 = {}
    for i in sorted(name):
        a = i[0]
        if a in dct1:
            dct1[a] += [i]
        else:
            dct1[a] = [i]
    return dct1


dct = {}
n1 = input("Введите имя:  ")
n2 = input("Введите второе имя:  ")
n3 = input("Третье имя:  ")
n4 = input("И четвертое:  ")
n5 = input("Ну и пятое:  ")
dct.update(thesaurus(n1, n2, n3, n4, n5))
print(dct)
