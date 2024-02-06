import random

def genera_cartella(id):
    cartella = {}

    for riga in range(3):
        for colonna in range(9):
            decina = colonna * 10 + 1

            numero = random.randint(decina, decina + 9)

            cartella[(riga, colonna)] = numero

    return cartella

def estrai_numero(numeri_estratti):
    numero = random.randint(1, 90)

    while numero in numeri_estratti:
        numero = random.randint(1, 90)

    numeri_estratti.append(numero)

    return numero

def controlla_cartella(cartella, numeri_estratti):
    stato_cartella = [False] * 5

    for riga in range(3):
        numeri_riga = [cartella[(riga, colonna)] for colonna in range(9)]
        numeri_riga_estratti = set(numeri_riga).intersection(set(numeri_estratti))

        if len(numeri_riga_estratti) >= 2:
            stato_cartella[0] = True

        if len(numeri_riga_estratti) >= 3:
            stato_cartella[1] = True

        if len(numeri_riga_estratti) >= 4:
            stato_cartella[2] = True

        if len(numeri_riga_estratti) == 15:
            stato_cartella[3] = True

    return stato_cartella

cartelle = []
numeri_estratti = []
stato_gioco = [False] * 4

for i in range(5):
    cartella = genera_cartella(i)
    cartelle.append(cartella)

while 90 not in numeri_estratti and not stato_gioco[3]:
    numero = estrai_numero(numeri_estratti)
    print("Numero estratto:", numero)

    for i in range(5):
        stato_cartella = controlla_cartella(cartelle[i], numeri_estratti)

        for j in range(4):
            stato_gioco[j] = stato_gioco[j] or stato_cartella[j]

        print("Stato cartella", i+1, ":", stato_cartella)

if 90 in numeri_estratti:
    print("Numero 90 estratto! Il gioco è finito.")
elif stato_gioco[3]:
    print("Tombola! Il gioco è finito.")
