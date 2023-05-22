from clovek import Clovek
from pojisteni import Pojisteni

pojisteni = Pojisteni()

while True:
    print("-----------------------------""\n Evidence pojištěných""\n-----------------------------""\n"
          "Vyberte si akci:"
          "\n1 - Přidat nového pojištěného"
          "\n2 - Vypsat všechny pojištěné"
          "\n3 - Vyhledat pojištěného"
          "\n4 - Konec")

    volba = input()

    if volba == "1":
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        vek = input("Zadejte věk:\n")
        telefon = input("Zadejte telefonní číslo:\n")
        clovek = Clovek(jmeno, prijmeni, vek, telefon)
        pojisteni.add_pojisteny(clovek)
        print("Data byla uložena.Pokračujte libovolnou klávesou...")
        input()

    elif volba == "2":
        print(pojisteni)
        print("Pokračujte libovolnou klávesou...")
        input()

    elif volba == "3":
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        clovek = pojisteni.vyhledat_pojisteny_by_jmeno(jmeno, prijmeni)
        if clovek:
            print(clovek)
        else:
            print("Pojištěnec není v databázi")
        print("Pokračujte libovolnou klávesou...")
        input()

    elif volba == "4":
        print("Děkujeme za použití aplikace.")
        break

    else:
        print("Neplatná volba. Zkuste znovu.")
