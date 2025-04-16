from kolcsonzo import auto_kolcsonzo
from berles import eddigi_berlesek, auto_berlese, berles_lemondas, elerheto_szemelyautok, elerheto_teherautok


def menu():
    while True:
        print("\n=== Autókölcsönző Menü ===")
        print("1. Autóink listája")
        print("2. Autó Bérlése")
        print("3. Bérlés lemondássa")
        print("4. Bérlések listázása")
        print("5. Kilépés")

        valasztas = input("Válassz egy lehetőséget (1-5): ")

        if valasztas == "1":
            auto_kolcsonzo.listaz_autok()

        elif valasztas == "2":
            print("\nMilyen típusú autót szeretnél bérelni?")

            print("1. Személyautó")

            print("2. Teherautó")

            tipus_valasztas = input("Választás (1-2): ")

            if tipus_valasztas == "1":

                szemelyautok = elerheto_szemelyautok()

                if not szemelyautok:

                    print("Jelenleg nincs elérhető személyautó.")

                else:

                    print("\nElérhető személyautók:")

                    for auto in szemelyautok:
                        print(auto.info())

                    rendszam = input("Írd be a kiválasztott autó rendszámát: ").strip().upper()

                    valasztott = next((a for a in szemelyautok if a.rendszam == rendszam), None)

                    if valasztott:

                        auto_berlese(valasztott)

                    else:

                        print("Nincs ilyen elérhető személyautó.")

            elif tipus_valasztas == "2":
                teherautok = elerheto_teherautok()

                if not teherautok:

                    print("Jelenleg nincs elérhető teherautó.")

                else:

                    print("\nElérhető teherautók:")

                    for auto in teherautok:
                        print(auto.info())

                    rendszam = input("Írd be a kiválasztott autó rendszámát: ").strip().upper()

                    valasztott = next((a for a in teherautok if a.rendszam == rendszam), None)

                    if valasztott:

                        auto_berlese(valasztott)

                    else:

                        print("Nincs ilyen elérhető teherautó.")
            else:
                print("Érvénytelen választás.")

        elif valasztas == "3":
            berles_lemondas()
        elif valasztas == "4":
            eddigi_berlesek()
        elif valasztas == "5":
            print("\nKilépés a programból. Köszönjük, hogy minket választottál!")
            break
        else:
            print("Hibás választás, próbáld újra!")


# Program indítása
if __name__ == "__main__":
    print(f"\nÜdvözlünk a(z) {auto_kolcsonzo.nev} rendszerében!")
    menu()
