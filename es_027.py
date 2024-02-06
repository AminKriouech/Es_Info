#Funzione 1 :
def input_n() -> list[int]:
    n = int(input("Inserisci il numero di valori: "))
    values = []
    
    for i in range(n):
        value = int(input("Inserisci il valore {}: ".format(i+1)))
        values.append(value)
    
    return values

lista_valori = input_n()
print(lista_valori)

#Funzione 2 :
def is_pari(num: int) -> bool:
    if num % 2 == 0:  # se il numero è divisibile per 2
        return True  # restituisci True
    else:  # altrimenti
        return False  # restituisci False

#Funzione 3 :
def somma_quadrati(lista_valori: list[int]) -> int:
    somma = 0
    for numero in lista_valori:
        if numero % 2 == 0:
            somma += numero ** 2
    return somma
