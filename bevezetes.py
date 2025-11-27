
def auto_allapota():
    auto_neve = str(input("Auto neve:"))
    gyartas_eve = int(input("Gyártási dátum:"))
    szoveg = str(f"Ez az {auto_neve}")
    
    if gyartas_eve == 2025:
        print(f"{szoveg} friss gyártású!")
    elif gyartas_eve < 2000:
        print(f"{szoveg} öreg autó!")
    else:
        print(f"{szoveg} átlagos korú!")