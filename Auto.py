class Auto:
    def __init__(self,nev:str,gyartasi_ev:int):
        self.nev=nev
        self.gyartasi_ev=gyartasi_ev

    def __str__(self):
        return f"{self.nev}, {self.gyartasi_ev}"