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
    bonus = bonus(str_result[0]) if random.randint(1, 100) == 1 else ""
    return f" - {str_result} => Statistique principale : {stat1}, {stat2}, {stat3} {bonus}"

# Crystite Orange
def orange():
    str_result = debut()
    stat1 = adjust_stat_for_hybride(_8d100(), str_result)
    stat2 = f"+{_1d30()} {_1d4()}"
    stat3 = f"+{_1d20()} {_1d4()}" if random.randint(0, 1) else f"+{_1d20()} {_1d5()}"
    stat4 = f"+{_1d10()} Exaltation"
    bonus = bonus(str_result[0]) if random.randint(1, 100) <= 5 else ""
    return f" - {str_result} => Statistique principale : {stat1}, {stat2}, {stat3}, {stat4} {bonus}"

# Bonus zopu
def bonus(type):
    #valeur utile
    reroll = 1
    listBonus = []
    isArmure = true

    if type == "A" : isArmure = False

    #boucle de reroll
    while reroll > 0:
        result = random.randint(1,100)
        
        match result:
            case 1 | 2 | 3 | 4 | 5:
                #lancer un autre D
                result2 = random.randint(1,3)

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1 : listBonus.append("Suprême")
                if result2 == 2 : listBonus.append("Indestructibilité")
                if result2 == 3 : reroll += 2

            case 6 | 7 | 8 | 9 | 10:
                #lancer un autre D
                result2 = random.randint(1,2)

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1 : listBonus.append("Résistance")
                if result2 == 2 : listBonus.append("Que de générosité")

            case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20:
                #bonus
                reroll -= 1
                listBonus.append("Légèreté")

            case 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30:
                #bonus
                reroll -= 1
                listBonus.append("Econome")

            case 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40:
                #bonus
                reroll -= 1
                if (isArmure): listBonus.append("REPLI !!!")
                if (not isArmure): listBonus.append("Fantôme")

            case 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60:
                #heu... faut relancer a priorie
                reroll -= 1
                reroll += 1

            case 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70:
                #bonus
                reroll -= 1
                if (isArmure): listBonus.append("Gruyère")
                if (not isArmure): listBonus.append("I'm stuck Step-Monster")

            case 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80:
                #bonus
                reroll -= 1
                listBonus.append("Rapiat")

            case 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90:
                #bonus
                reroll -= 1
                listBonus.append("Lourdeur")

            case 91 | 92 | 93 | 94 | 95:
                #lancer un autre D
                result2 = random.randint(1,2)

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1 : listBonus.append("Fragilité")
                if result2 == 2 : listBonus.append("Connard")

            case 96 | 97 | 98 | 99 | 100:
                #lancer un autre D
                result2 = 0
                if (isArmure): result2 = random.randint(1,2)
                if (not isArmure): result2 = random.randint(1,3)

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1 : listBonus.append("Inutile")
                if result2 == 2 : listBonus.append("Maudit")
                if result2 == 3 : listBonus.append("Machette ornithologique")

    #formatage du string
    reponse = "["
    for i in range(len(listBonus)):
        if i > 0: reponse += ", "
        reponse += listBonus[i]
    reponse += "]"

    return reponse


        