class Clovek:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f'{self.jmeno.title()}   {self.prijmeni.title()}   {self.vek}   {self.telefon}'
