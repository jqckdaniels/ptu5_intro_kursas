import logging

logging.basicConfig(
    filename="asmenys.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(modules)s:%(funcName)s:%{lineno}s:%{message}s")

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self,pavarde = pavarde
        logging.info(f"Sukurtas klases {self.__class__.__name__} objektas {vardas} {pavarde}")

ingrida = Asmuo("Ingrida", "Vaitkuviene")
darius = Asmuo("Darius", "Vasionis")