import random

def lotto():
    x = 0
    lista = []
    for x in range(0, 5, 1):
        lista.append(random.randint(1,90))
    print(f"{lista[0]}; {lista[1]}; {lista[2]}; {lista[3]}; {lista[4]}")
    return lista

def egyjegyuek_szama(lista):
    cv = 0
    szamolo = 0
    while cv < len(lista):
        if lista[cv] < 10:
            szamolo += 1
        cv += 1
    return szamolo

def konzol_kiir(egyjegyuek):
    print (f"Az egyjegyűek száma: {egyjegyuek}")

def file_kiir(egyjegyuek):
    with open("szamok.txt", "a", encoding="utf-8") as f:
        f.write (f"Az egyjegyűek száma: {egyjegyuek}")