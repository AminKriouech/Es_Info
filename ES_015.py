#Scrivere un programma che passati in input un numero non definito a priori di voti, ne calcoli la media.
#Il programma terminerà con l'iterazione degli input quando inseriamo un valore <=0.
#Non si  considerino ai fini della media, i voti >10.

num_voti = 0
somma_voti = 0

voto = int(input("Inserisci un voto (Inserisci un valore <= 0 per finire): "))

while voto > 0:
    if voto <= 10:
        num_voti += 1
        somma_voti += voto 
    voto = int(input("Inserisci un voto(Inserisci un valore <= 0 per finire): "))

    if num_voti > 0:
        media_voti = somma_voti / num_voti
        print("La media dei voti è:",media_voti)
    else:
        print("Nessun voto valido inserito.")


