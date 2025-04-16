from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, szallithato_szemelyek: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.szallithato_szemelyek = szallithato_szemelyek

    def info(self):
        return (
            f"Személyautó\n"
            f"  Rendszám: {self.rendszam}\n"
            f"  Típus: {self.tipus}\n"
            f"  Szállítható személyek száma: {self.szallithato_szemelyek}\n"
            f"  Bérleti díj: {self.berleti_dij} Ft/nap"
            f"\n"
        )