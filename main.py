'''
2.3 Feladat
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!

A felhasználónak többször is legyen lehetősége újabb tippet megadnia. A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).
'''


szo = "piton"
print(szo)

l = []
jo_lista = []
rossz_lista = []

while True:
  betu = input("Kérek egy betűt:")
  if betu == "":
    break
  else:
    l.append(betu)
    if betu in szo:
      jo_lista.append(betu)
    else:
      rossz_lista.append(betu)

print(f'Jó tippek: {jo_lista}')
print(f'Rossz tippek: {rossz_lista}')
      

eredmeny = False
index = 0
while index < len(szo) and not eredmeny:
	      if szo[index] == betu :
		        eredmeny = True
	      index = index + 1




