class Auto:
    def __init__(self, marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero):
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilindrata
        self.potenza_kw = potenza_kw
        self.anno_immatricolazione = anno_immatricolazione
        self.costo_gestione = costo_gestione
        self.giorni_affitto = giorni_affitto
        self.prezzo_giornaliero = prezzo_giornaliero

        parco_auto = []
        
        def aggiungi_auto():
            marca = input("Inserisci la marca dell'auto: ")
            modello = input("Inserisci il modello dell'auto: ")
            cilindrata = int(input("Inserisci la cilindrata dell'auto: "))
            potenza_kw = int(input("Inserisci la potenza in kW dell'auto: "))
            anno_immatricolazione = int(input("Inserisci l'anno di immatricolazione dell'auto: "))
            costo_gestione = float(input("Inserisci il costo di gestione dell'auto: "))
            giorni_affitto = int(input("Inserisci i giorni di affitto dell'auto: "))
            prezzo_giornaliero = float(input("Inserisci il prezzo giornaliero dell'auto: "))
            
            nuova_auto = Auto(marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero)
            parco_auto.append(nuova_auto)
            print("Auto aggiunta con successo al parco auto.")
        
        def rimuovi_auto():
            marca = input("Inserisci la marca dell'auto da rimuovere: ")
            modello = input("Inserisci il modello dell'auto da rimuovere: ")
            
            for auto in parco_auto:
                if auto.marca == marca and auto.modello == modello:
                    parco_auto.remove(auto)
                    print("Auto rimossa con successo dal parco auto.")
                    return
            
            print("Nessuna auto corrispondente trovata nel parco auto.")
        
        def calcola_bollo(indice_auto):
            auto = parco_auto[indice_auto]
            
            if auto.potenza_kw <= 100:
                bollo = auto.potenza_kw * 2.58
            elif auto.potenza_kw > 185:
                bollo = 185 * 2.58 + (auto.potenza_kw - 185) * 3.87 + 20
            else:
                bollo = auto.potenza_kw * 3.87
            
            print("Il bollo dell'auto è:", bollo, "euro.")
        
        def calcola_profitto(indice_auto):
            auto = parco_auto[indice_auto]
            
            profitto = auto.giorni_affitto * (auto.prezzo_giornaliero - auto.costo_gestione - calcola_bollo(indice_auto))
            
            print("Il profitto dell'auto è:", profitto, "euro al giorno.")
        
        def calcola_profitto_totale():
            profitto_totale = 0
            
            for i in range(len(parco_auto)):
                profitto_totale += calcola_profitto(i)
            
            print("Il profitto totale del parco auto è:", profitto_totale, "euro prima delle tasse.")
        
        def visualizza_menu():
            print("Menu:")
            print("1) Aggiungi un veicolo")
            print("2) Rimuovi un veicolo")
            print("3) Calcola il bollo di un veicolo")
            print("4) Calcola il profitto di un veicolo")
            print("5) Calcola il profitto totale del parco auto")
            print("6) Esci")
            
            scelta = input("Seleziona un'opzione: ")
            
            if scelta == "1":
                aggiungi_auto()
            elif scelta == "2":
                rimuovi_auto()
            elif scelta == "3":
                indice_auto = int(input("Inserisci l'indice dell'auto nel parco auto: "))
                calcola_bollo(indice_auto)
            elif scelta == "4":
                indice_auto = int(input("Inserisci l'indice dell'auto nel parco auto: "))
                calcola_profitto(indice_auto)
            elif scelta == "5":
                calcola_profitto_totale()
            elif scelta == "6":
                print("Grazie per aver utilizzato l'applicativo. Arrivederci!")
            else:
                print("Opzione non valida. Riprova.")
                visualizza_menu()
        