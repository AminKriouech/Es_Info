# Scrivere un programma che permetta la gestione di una lista della spesa. Esso deve prevedere un menu così formato:


#Scegliere l'opzione desiderata:
#1) Visualizza lista
#2) Aggiungi item e quantità
#3) Modifica quantità di un item
#4) Rimuovi item
#5) Esci
#Scelta:_

#Per la lista della spesa si consiglia l'utilizzo di due liste, una per gli elementi una per le quantità


lista_spesa = []
quantita = []

while True:
    print("""
    Scegliere l'opzione desiderata:
    1) Visualizza lista
    2) Aggiungi item e quantità
    3) Modifica quantità di un item
    4) Rimuovi item
    5) Esci
    """)
    scelta = input("Scelta: ")

    if scelta == "1":
        print("Lista della spesa:")
        for i in range (len(lista_spesa)):
            print(f"{lista_spesa[i]} - Quantità: {quantita[i]}")

    elif  scelta == "2":
        item = input("Inserisci item da aggiungere: ")
        quant = input("Inserisci quantità: ")

        lista_spesa.append(item)
        quantita.append(quant)
 
        print("Item aggiunto alla spesa.")

    elif scelta == "3":
        item = input("Inserisci item di cui modificare la quantità: ")
        new_qty = input("Inserisci la nuova quantità: ")

        if item in lista_spesa:
            index = lista_spesa.index(item)
            quantita[index] = new_qty
            print("Quantità modificata con successo.")
        else:
            print("Item non trovato nella lista.")

    elif scelta == "4":
        item = input("Inserisci item da rimuovere: ")

        if item in lista_spesa:
            index = lista_spesa.index(item)
            lista_spesa.remove(item)
            quantita.pop(index)
            print("Item rimosso dalla lista della spesa.")
        else:
            print("Item non trovato nella lista.")

    elif scelta == "5":
        print("Arrivederci!")
        break

    else:
        print("Scelta non valida. Riprova.")