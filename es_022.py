#Attività 1: crea un dizionario
#Inizia creando un dizionario. Questo dizionario dovrebbe rappresentare un libro. Utilizzare tasti come title, author, e year_published, e assegnare loro i valori appropriati.

#Attività 2: aggiungi un articolo
#Aggiungi una nuova coppia chiave-valore al dizionario. La chiave dovrebbe essere genree il valore dovrebbe essere qualsiasi genere di tua scelta.

#Attività 3: modifica un articolo
#Modifica il valore di una delle chiavi esistenti nel dizionario. Ad esempio, potresti modificare il valore della year_publishedchiave in un anno diverso.

#Attività 4: Elimina un elemento
#Rimuovi una coppia chiave-valore dal dizionario. Potresti rimuovere la authorchiave, per esempio.

#Attività 5: scorrere il dizionario
#Scrivi tre cicli separati:

#Uno per stampare tutte le chiavi
#Uno per stampare tutti i valori
#Uno per stampare tutte le coppie chiave-valore (elementi) nel dizionario
#Ricorda, i metodi del dizionario Python keys(), values(), e items()saranno utili in questo compito.






libro = {
"titolo" :"Il signore degli anelli",
"autore":"J.R.R. Tolkien",
"anno_di_pubblicazione":1954
}

libro["genere"] = "Fantasy"

libro["anno_di_pubblicazione"] = 1955

del libro["autore"]

for key in libro.keys():
    print(key)

for value in libro.values():
    print(value)

for key, value in libro.items():
    print(key, ":", value)

