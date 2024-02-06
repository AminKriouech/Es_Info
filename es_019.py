n = int(input("Inserire numero di bit: "))
decimale = int(input("Inserire numero:"))
lista = []
bin = 2**(n-1)
i = 0
while i < n:
    if decimale - bin >= 0:
        decimale -= bin
        lista.append(1)
    elif decimale - bin < 0:
        lista.append(0)        
    bin /= 2
    i += 1
print(lista)