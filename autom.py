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
    print( auto_lista[0].gyartasi_ev)
    print(auto_lista[1])
    print(auto_lista[0])

file_beolvas()