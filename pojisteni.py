class Pojisteni:
    def __init__(self):
        self.pojisteny = []

    def add_pojisteny(self, clovek):
        self.pojisteny.append(clovek)

    def vyhledat_pojisteny_by_jmeno(self, jmeno, prijmeni):
        for clovek in self.pojisteny:
            if clovek.jmeno == jmeno and clovek.prijmeni == prijmeni:
                return clovek
            return None

    def __str__(self):
        return "\n".join([str(clovek) for clovek in self.pojisteny])
