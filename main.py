import bevezetes
import sorozat
import autom

print ("****** 1. Feladat ******")
bevezetes.auto_allapota()

print ("****** 2. Feladat ******")
szamok = sorozat.lotto()
egyjegyuek = sorozat.egyjegyuek_szama(szamok)
sorozat.konzol_kiir(egyjegyuek)
sorozat.file_kiir(egyjegyuek)

print("****** 3. Feladat ******")

auto_lista = autom.file_beolvas()
autom.flotta(auto_lista)
autom.legfiatalabb(auto_lista)
autom.atlagolas(auto_lista)