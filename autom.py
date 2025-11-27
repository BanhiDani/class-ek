from Auto import Auto

def file_beolvas():

    auto_lista = []

    f=open("auto.txt", "r", encoding="utf-8")
    f.readline()
    autok = f.readlines()
    f.close()
    
    i = 0
    while i < len(autok):
        sor = autok[i].strip().split("$")
        auto=Auto(sor[0],int(sor[1]))
        i += 1
        auto_lista.append(auto)
    """print( auto_lista[0].gyartasi_ev)
    print(auto_lista[1])
    print(auto_lista[0])"""
    return auto_lista

file_beolvas()

def flotta(auto_lista):
    autok_szama = len(auto_lista)
    print (f"Autók száma: {autok_szama}")

def legfiatalabb(auto_lista):
    i = 0
    fiatal = 0
    melyik = ""
    while i < len(auto_lista):
        if auto_lista[i].gyartasi_ev > fiatal:
            fiatal = auto_lista[i].gyartasi_ev
            melyik =auto_lista[i].nev
        i += 1
    print (f"A legfiatalabb autó: {melyik}({fiatal})")

def atlagolas(auto_lista):
    i = 0
    valtozo = 0
    while i < len(auto_lista):
        valtozo +=  auto_lista[i].gyartasi_ev
        i += 1
    atlag = valtozo / len(auto_lista)
    eredmeny = int(2025 - atlag)
    print (f"Az autók átlagos kora: {eredmeny} év")
