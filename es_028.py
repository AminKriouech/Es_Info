def calcola_superbollo(kW: int, immatricolazione: int) -> float:
    anni = 2022 - immatricolazione

    if anni <= 5:
        superbollo = max(kW - 185, 0) * 20
    elif anni <= 10:
        superbollo = max(kW - 185, 0) * 12
    elif anni <= 15:
        superbollo = max(kW - 185, 0) * 6
    elif anni <= 20:
        superbollo = max(kW - 185, 0) * 3
    else:
        superbollo = 0

    return superbollo


def calcola_bollo(classe_ambientale: int, kW: int, immatricolazione: int) -> list[float] or None:
    if classe_ambientale < 0 or kW < 0 or immatricolazione < 0:
        return None

    if classe_ambientale == 0:
        bollo = min(kW, 100) * 3 + max(kW - 100, 0) * 4.5
    elif classe_ambientale == 1:
        bollo = min(kW, 100) * 2.9 + max(kW - 100, 0) * 4.35
    elif classe_ambientale == 2:
        bollo = min(kW, 100) * 2.8 + max(kW - 100, 0) * 4.2
    elif classe_ambientale == 3:
        bollo = min(kW, 100) * 2.7 + max(kW - 100, 0) * 4.05
    elif classe_ambientale >= 4:
        bollo = min(kW, 100) * 2.58 + max(kW - 100, 0) * 3.87

    superbollo = calcola_superbollo(kW, immatricolazione)

    if superbollo > 0:
        return [bollo, superbollo]
    else:
        return [bollo, None]

classe_ambientale = 3
kW = 120
immatricolazione = 2015
bollo, superbollo = calcola_bollo(classe_ambientale, kW, immatricolazione)
print("Bollo auto: ", bollo)
if superbollo is not None:
    print("Superbollo: ", superbollo)
else:
    print("Superbollo non previsto")
es_28.py
Visualizzazione di es_28.py.
Esercizio 28
Armando Mancini
•
9 gen
Consegna: 11 gen, 23:59
Scrivere una funzione che passati come parametro la classe ambientale (euro 0, euro1,...., euro6), i kW e gli anni passati dall'immatricolazione di un autoveicolo, calcoli il bollo auto e l'eventuale superbollo. Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma di esempio.

N.B.
Creare una funzione specifica per il superbollo da usare nella funzione principale.
es.
def calcola_superbollo (kW:int, immatricolazione: int) ->float: ....

Signature metodo principale:
def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None: ....
N.B.
La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None


utilizzo:
bollo, superbollo = calcola_bollo (.......................................

Calcolo bollo:
Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Calcolo superbollo:
Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
Dopo i 20 anni non pagano il superbollo
Commenti sul corso