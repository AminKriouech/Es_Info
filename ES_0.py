#Scrivere un programma che passati in input un numero non definito a priori di voti, ne calcoli la media.
#Il programma terminerà con l'iterazione degli input quando inseriamo un valore <=0.
#Non si  considerino ai fini della media, i voti >10.

voti = 0
voto = int(input("Inserisci il voto:"))

if voto > 10:
    voto = 0 

media = voto + voti


while voto <= 0:
    voto += 1

print(media)



