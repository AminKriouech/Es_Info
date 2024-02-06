dipendenti = [
    {"nome": "Mario Lupo", "ruolo": "Programmatore", "stipendio_iniziale": 2000},
    {"nome": "Gaia Bianchi", "ruolo": "Influencer", "stipendio_iniziale": 2500},
    {"nome": "Luigi Verdi", "ruolo": "Imprenditore", "stipendio_iniziale": 2200}
]

print("Lista dipendenti:")
for dipendente in dipendenti:
    print(dipendente)

progetti = [
    {"nome": "Progetto A", "budget": 10000, "costo_orario": 50, "ore_lavorate": 0},
    {"nome": "Progetto B", "budget": 5000, "costo_orario": 40, "ore_lavorate": 0}
]

for dipendente in dipendenti:
    ore_lavorate = int(input(f"Inserisci le ore lavorate da {dipendente['nome']} sul nuovo progetto: "))
    compenso = dipendente["stipendio_iniziale"] + (ore_lavorate * progetti[0]["costo_orario"])
    dipendente["stipendio_totale"] = compenso
    dipendente["ore_lavorate"] = ore_lavorate
    progetti[0]["budget"] -= (ore_lavorate * progetti[0]["costo_orario"])
    progetti[0]["ore_lavorate"] += ore_lavorate

print("\nLista dipendenti con stipendi e ore lavorate sul nuovo progetto:")
for dipendente in dipendenti:
    print(f"Nome: {dipendente['nome']}, Ruolo: {dipendente['ruolo']}, Stipendio totale: {dipendente['stipendio_totale']}, Ore lavorate: {dipendente['ore_lavorate']}")

print("\nRiepilogo progetti:")
for progetto in progetti:
    print(f"Nome progetto: {progetto['nome']}, Ore totali lavorate: {progetto['ore_lavorate']}, Budget rimanente: {progetto['budget']}")