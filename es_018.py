# Scrivere un programma che passati in input n valori popoli una lista.
#In seguito scorre lista con un for e ne calcola il valore medio, il massimo e il minimo.

valori = int(input("Inserisci i valori della lista:"))

lista = []

for i in range(valori):
    n = input("Inserisci un valore:")
    lista.append(valori)
    
media = lista / n

minimo = min(lista)

massimo = max(lista)

print = ("Il valore massimo della lista è:", massimo)
print = ("Il valore minimo della lista è:", minimo)
print = ("Il valore medio della lista è:", media)