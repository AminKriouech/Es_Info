lista_frutta = [   "Mela",
                   "Banana",
                   "Uva",
                   "Anguria",    ]
for i in range(1):
    print(lista_frutta)
lista_frutta.append (input("Aggiungi un frutto:"))
for i in range(1):
    print(lista_frutta)
lista_frutta.remove("Banana")
for i in range(1):
    print(lista_frutta)
print(lista_frutta[2])