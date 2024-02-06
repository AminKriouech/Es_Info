# Scrivere un programma che passati in input n valori popoli una lista e la ristampi a video scorrendola con un for.

valori = int(input("Inserisci i valori da mettere nella lista:"))

lista = []

for i in range(valori):
    n = input("Inserisci un valore:")
    lista.append(valori)
    
    print("La lista inserita è:")
    for valori in lista:
        print(valori)