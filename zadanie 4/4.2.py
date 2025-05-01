file = open('odbiorcy.txt','r')
linijki = file.readlines()
lista=[]
licznik = 0 #nigdy nie ma 1

for i in range(1,len(linijki)+1):
    lista.append(i)
for linijka in linijki:
    linijka = int(linijka.strip())

    if linijka in lista:
        lista.remove(linijka) #trzeba usuwać to co juz jest nie potrzebne
    else:
        licznik += 1


print(licznik)