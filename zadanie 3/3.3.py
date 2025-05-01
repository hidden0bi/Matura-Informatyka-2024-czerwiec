file = open('slowa.txt','r')
linijki = file.readlines()

liczydlo = 0
for linijka in linijki:
    slownik = {}
    linijka = linijka.strip()

    for litera in linijka:
        if litera in slownik:
            slownik[litera] += 1
        else:
            slownik[litera]  = 1
    najdluzszy = max(slownik.values())



    if najdluzszy * 2 >= len(linijka):
        print(linijka)