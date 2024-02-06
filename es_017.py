# Scrivere un programma che passati in input n valori popoli una lista.
# In seguito chiede all'utente di inserire un valore in modo tale da verificare che esso sia presente nella lista. Stampare a video ("Valore presente"/"Valore non presente").

valori = int(input("Inserisci i valori della lista:"))

lista = []

for i in range(valori):
    n = input("Inserisci un valore:")
    lista.append(valori)
    
valore_verifica = int(input("Inserisci il valore da verificare:"))

if valore_verifica in range(valori):
    print("Valore presente.")
else:
    valore_verifica not in range(valori)
    print("Valore non presente")

