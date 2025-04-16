from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, max_teher: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.max_teher = max_teher

    def info(self):
        return (
            f"Teherautó\n"
            f"  Rendszám: {self.rendszam}\n"
            f"  Típus: {self.tipus}\n"
            f"  Maximális teherbírás: {self.max_teher} kg\n"
            f"  Bérleti díj: {self.berleti_dij} Ft/nap"
            f"\n"
        )
