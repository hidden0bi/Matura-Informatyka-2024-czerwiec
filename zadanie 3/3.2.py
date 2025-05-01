file = open('slowa.txt','r')
linijki = file.readlines()
alphabet = [chr(i) for i in range(97,123)]
#print(alphabet)
alphabet = [i for i in range(97,123)]
#print(alphabet)

def kodowane(slowo):
    lista = []
    slowo = str(slowo)
    for n in slowo:
        ansii = ord(n)
        if ansii + 13 >= 123:
            nowy_przesuniety = ansii + 13 -123 + 97
        else:
            nowy_przesuniety = ansii + 13
        nowa_litera = chr(nowy_przesuniety)

        lista.append(nowa_litera)
    return "".join(lista)

def odwrotnie(slowo):
    lista = []
    slowo = str(slowo)
    for literka in slowo:
        lista.append(literka)
    lista.reverse()
    return "".join(lista)

licznik = 0
slownik = {}
for linijka in linijki:
    linijka = linijka.strip()
    kod = kodowane(linijka)
    odwrotny = odwrotnie(linijka)
    if kod == odwrotny:
        slownik[linijka] = len(linijka)
        licznik += 1

posortowane = dict(sorted(slownik.items(), key=lambda item: item[1],reverse=True)) #ten  key=lambda item: item[1] odpowiada za to ktory item wybierze, bo [0] to klucz, a [1] to wartosc
tekst = 'aren'

for i in posortowane.items():
    najdluzszy = i[0]
    break
print(licznik, najdluzszy)