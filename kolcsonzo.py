from szemelyauto import Szemelyauto
from teherauto import Teherauto


class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev  # kölcsönző neve
        self.autok = []

    def auto_hozzaad(self, auto):
        self.autok.append(auto)

    def listaz_autok(self):
        print(f"\n{self.nev} autói:")
        for auto in self.autok:
            print(auto.info())

    def keres_rendszam(self, rendszam: str):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return auto


# A Kölcsönző
auto_kolcsonzo = Autokolcsonzo("Express Autókölcsönző")

# autók példányosítása
auto1 = Szemelyauto("ABC123", "Opel Astra", 8000, 5)
auto2 = Teherauto("XYZ456", "Ford Transit", 12000, 1500)
auto3 = Szemelyauto("LMN789", "Suzuki Swift", 7000, 4)

# autók hozzáadása
auto_kolcsonzo.auto_hozzaad(auto1)
auto_kolcsonzo.auto_hozzaad(auto2)
auto_kolcsonzo.auto_hozzaad(auto3)
