def calcola_importo(fatture: list[dict]) -> list[float] | None:
    if not fatture:  # Controllo se la lista delle fatture è vuota
        return None

    totale_importo = 0  # Variabile per calcolare il totale degli importi
    totale_importo_scontato = 0  # Variabile per calcolare il totale degli importi scontati

    for fattura in fatture:
        importo = fattura["importo"]  # Prendo l'importo dalla fattura
        sconto = fattura["sconto_fattura"]  # Prendo lo sconto dalla fattura

        importo_scontato = importo - (importo * sconto / 100)  # Calcolo l'importo scontato

        fattura["importo_scontato"] = importo_scontato  # Aggiungo la chiave "importo_scontato" alla fattura

        totale_importo += importo  # Aggiorno il totale degli importi
        totale_importo_scontato += importo_scontato  # Aggiorno il totale degli importi scontati

    return [totale_importo, totale_importo_scontato]  # Restituisco una lista con i totali

fatture = [
    {"id":"Monticelli", "importo":245.78, "sconto_fattura":10},
    {"id":"Kola", "importo":325.71, "sconto_fattura":12},
    {"id":"Romagna", "importo":245.78, "sconto_fattura":8},
    {"id":"Bilancioni", "importo":245.78, "sconto_fattura":15},
    {"id":"Sanchi", "importo":245.78, "sconto_fattura":5},
    {"id":"Pontellini", "importo":245.78, "sconto_fattura":18},
    {"id":"Clementi", "importo":245.78, "sconto_fattura":20},
    {"id":"Arlotti", "importo":245.78, "sconto_fattura":19},
    {"id":"Nedria", "importo":245.78, "sconto_fattura":7},
    {"id":"Santini", "importo":245.78, "sconto_fattura":22},
]

risultato = calcola_importo(fatture)
print(risultato)
