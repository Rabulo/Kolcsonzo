from kolcsonzo import auto1, auto2, auto3, auto_kolcsonzo
from datetime import datetime, timedelta
from teherauto import Teherauto
from szemelyauto import Szemelyauto


class Berles:

    def __init__(self, auto, napok_szama: int, kezdes_datum: str, azonosito: str):
        self.auto = auto
        self.napok_szama = napok_szama
        self.kezdes_datum = datetime.strptime(kezdes_datum, "%Y.%m.%d")
        self.azonosito = azonosito

    def osszeg(self):
        return self.napok_szama * self.auto.berleti_dij

    def lejarati_datum(self):
        return self.kezdes_datum + timedelta(days=self.napok_szama)

    def aktiv_e(self):
        return datetime.now() < self.lejarati_datum()


# bérlés azonosító számláló
berles_azonosito_counter = 1

# bérlések listája
berlesek = [
    Berles(auto1, 3, "2023.10.01", "bZ1"),
    Berles(auto2, 10, "2023.10.05", "bZ2"),
    Berles(auto3, 5, "2023.10.10", "bz3"),
    Berles(auto1, 2, "2023.10.15", "bZ4"),
]


# Eddigi bérlések felvitele
def eddigi_berlesek():
    print("\nEddigi Bérlések:")
    for i, berles in enumerate(berlesek, 1):
        print(
            f"{i}. {berles.auto.tipus} ({berles.auto.rendszam}) - {berles.napok_szama}"
            f" nap - Összeg: {berles.osszeg()} Ft")


def auto_berlese(valasztott):
    global berles_azonosito_counter
    print("\n---Autó bérlés---")
    # rendszam = input("Add meg az autó rendszámát: ").strip().upper()
    # auto = auto_kolcsonzo.keres_rendszam(rendszam)
    napok_szama = int(input("Add meg a bérlés napjainak számát: "))

    # Dátum bekérése és ellenőrzés
    while True:
        datum = input("Add meg a bérlés kezdő dátumát (ÉÉÉÉ.HH.NN): ")
        if len(datum) == 8 and datum.isdigit():
            datum = f"{datum[:4]}.{datum[4:6]}.{datum[6:]}"

        try:
            berles_datum = datetime.strptime(datum, "%Y.%m.%d")
            if berles_datum.date() < datetime.today().date():
                print("A bérlés dátuma nem lehet múltbéli! Próbáld újra.")
            else:
                berles_datum_str = berles_datum.strftime("%Y.%m.%d")
                break
        except ValueError:
            print("Érvénytelen dátum formátum. Használj ÉÉÉÉ.HH.NN formátumot.")

    # Azonosító generálása
    azonosito = f"Az{berles_azonosito_counter:03d}"
    berles_azonosito_counter += 1

    # Bérlés létrehozása
    uj_berles = Berles(valasztott, napok_szama, berles_datum_str, azonosito)
    berlesek.append(uj_berles)

    print(f"Sikeres bérlés!")
    print(f"  Azonosítód: {azonosito}")
    print(f"  Rendszám: {valasztott.rendszam}")
    print(f"  Bérlés összege: {uj_berles.osszeg()} Ft")


def elerheto_autok():
    foglalt_autok = {berles.auto for berles in berlesek if berles.aktiv_e()}
    return [auto for auto in auto_kolcsonzo.autok if auto not in foglalt_autok]


def elerheto_szemelyautok():
    return [auto for auto in elerheto_autok() if isinstance(auto, Szemelyauto)]


def elerheto_teherautok():
    return [auto for auto in elerheto_autok() if isinstance(auto, Teherauto)]


# Bérlés lemondása
def berles_lemondas():
    print("\n   Bérlések lemondása    ")

    aktiv_berlesek = [b for b in berlesek if b.aktiv_e()]

    if not aktiv_berlesek:
        print("Nincs aktív bérlés.")
        return

    # Aktív bérlések listázása (azonosító NÉLKÜL)
    print("\nAktív bérlések:")
    for berles in aktiv_berlesek:
        print(
            f"{berles.auto.tipus} ({berles.auto.rendszam}) - {berles.napok_szama} nap - Kezdés: {berles.kezdes_datum.strftime('%Y.%m.%d')}")

    # Azonosító bekérése
    azonosito = input("\nAdd meg a lemondani kívánt bérlés azonosítóját: ").strip()

    # Bérlés keresése azonosító alapján
    berles = next((b for b in aktiv_berlesek if b.azonosito.lower() == azonosito.lower()), None)

    if berles:
        megerosites = input(f"Biztosan törölni szeretnéd a(z) {berles.auto.rendszam} bérlést? (i/n): ").strip().lower()
        if megerosites == "i":
            berlesek.remove(berles)
            print("A bérlés sikeresen törölve lett.")
        else:
            print("A bérlés törlése megszakítva.")
    else:
        print("Nincs ilyen azonosítójú aktív bérlés.")
