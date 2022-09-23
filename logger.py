import logging 
from modules.aritmetika import daugyba

logging.basicConfig(level=logging.DEBUG, filename="problemos.log", format="%(asctime)s:%(levelname)s:%(module)s:%(message)s")

def dalyba(a, b):
    try:
        res = a / b
    except Exception as e:
        # ismetam pranesima, kad ivyko klaida
        logging.error(f"Vykdant funkcija {dalyba.__name__}, ivyko klaida {e.__class__.__name__}: {e}")
        return None
    else:
        logging.info(f"Paleista funkcija {dalyba.__name__}: {a} / {b} = {res}")
        return res

print(dalyba(7, 0))
print(dalyba(7, 3))
print(daugyba(3, 5))