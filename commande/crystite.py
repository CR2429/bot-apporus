import random
import re

# Lancer de dés
def _1d9():
    result = random.randint(1, 9)
    result_str = {
        1: "Arme 1 main tranchante",
        2: "Arme 2 main tranchante",
        3: "Arme 1 main contondante",
        4: "Arme 2 main contondante",
        5: "Bouclier",
        6: "Casque",
        7: "Plastron",
        8: "Brassard",
        9: "Jambière"
    }.get(result, "")
    return result_str

def _1d3():
    result = random.randint(1, 3)
    result_str = {
        1: "Armure",
        2: "Barrière",
        3: "Hybride"
    }.get(result, "")
    return result_str

def _1d20():
    return random.randint(1, 20)

def _3d30():
    return sum(random.randint(1, 30) for _ in range(3))

def _5d80():
    return sum(random.randint(1, 80) for _ in range(5))

def _8d100():
    return sum(random.randint(1, 100) for _ in range(8))

def _1d10():
    return random.randint(1, 10)

def _1d30():
    return random.randint(1, 30)

def _1d4():
    result = random.randint(1, 4)
    result_str = {
        1: "Feu",
        2: "Eau",
        3: "Vent",
        4: "Terre"
    }.get(result, "")
    return result_str

def _1d5():
    result = random.randint(1, 5)
    result_str = {
        1: "Force",
        2: "Agilité",
        3: "Discrétion",
        4: "Constitution",
        5: "Charisme"
    }.get(result, "")
    return result_str

# Ouverture de crystite
def debut():
    str_result = _1d9()
    # Vérifie si l'équipement est une armure
    armure = str_result in ["Bouclier", "Casque", "Plastron", "Jambière", "Brassard"]
    if armure:
        str_result += " - " + _1d3()
    return str_result

# Fonction générique pour le calcul de la statistique hybride
def adjust_stat_for_hybride(stat, str_result):
    if re.search(r'Hybride$', str_result):
        if stat % 2 == 1:
            stat += 1
        stat //= 2
    return stat

# Crystite Blanche
def blanc():
    str_result = debut()
    stat1 = adjust_stat_for_hybride(_1d20(), str_result)
    return f" - {str_result} => Statistique principale : {stat1}"

# Crystite Verte
def vert():
    str_result = debut()
    stat1 = adjust_stat_for_hybride(_3d30(), str_result)
    stat2 = f"+{_1d10()} {_1d4()}"
    return f" - {str_result} => Statistique principale : {stat1}, {stat2}"

# Crystite Bleue
def bleu():
    str_result = debut()
    stat1 = adjust_stat_for_hybride(_5d80(), str_result)
    stat2 = f"+{_1d20()} {_1d4()}"
    stat3 = f"+{_1d10()} {_1d4()}" if random.randint(0, 1) else f"+{_1d10()} {_1d5()}"
    bonus = ", bonus zopu :)" if random.randint(1, 100) == 1 else ""
    return f" - {str_result} => Statistique principale : {stat1}, {stat2}, {stat3}{bonus}"

# Crystite Orange
def orange():
    str_result = debut()
    stat1 = adjust_stat_for_hybride(_8d100(), str_result)
    stat2 = f"+{_1d30()} {_1d4()}"
    stat3 = f"+{_1d20()} {_1d4()}" if random.randint(0, 1) else f"+{_1d20()} {_1d5()}"
    stat4 = f"+{_1d10()} Exaltation"
    bonus = ", bonus zopu :)" if random.randint(1, 100) <= 5 else ""
    return f" - {str_result} => Statistique principale : {stat1}, {stat2}, {stat3}, {stat4}{bonus}"

# Bonus zopu
def bonus(type):
    reroll = 1