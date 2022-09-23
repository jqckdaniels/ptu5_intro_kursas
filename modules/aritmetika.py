import logging

def daugyba(a, b):

    try:
        res = a * b
    except Exception as e:
        # ismetam pranesima, kad ivyko klaida
        logging.error(f"Vykdant funkcija {daugyba.__name__}, ivyko klaida {e.__class__.__name__}: {e}")
        return None
    else:
        logging.info(f"Paleista funkcija {daugyba.__name__}: {a} * {b} = {res}")
        return res

print(daugyba(2, 2))
