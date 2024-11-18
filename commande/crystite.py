import random
import re
import commande.dice as dice
from main import json_data

# Lancer de dés
def _1d9(poids):
    result = dice.d9(poids)
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
    }.get(result[0], "")
    return [result_str,result[1]]

def _1d3(poids):
    result = dice.d3(poids)
    result_str = {
        1: "Armure",
        2: "Barrière",
        3: "Hybride"
    }.get(result[0], "")
    return [result_str,result[1]]

def _1d20(poids):
    return dice.d20(poids)

def _3d30(poids):
    result1 = dice.d30(poids)
    result2 = dice.d30(result1[1])
    result3 = dice.d30(result2[1])
    result_final = result1[0]+result2[0]+result3[0]
    return [result_final,result3[1]]

def _5d80(poids):
    result1 = dice.d80(poids)
    result2 = dice.d80(result1[1])
    result3 = dice.d80(result2[1])
    result4 = dice.d80(result3[1])
    result5 = dice.d80(result4[1])
    result_final = result1[0]+result2[0]+result3[0]+result4[0]+result5[0]
    return [result_final,result5[1]]

def _8d100(poids):
    result1 = dice.d80(poids)
    result2 = dice.d80(result1[1])
    result3 = dice.d80(result2[1])
    result4 = dice.d80(result3[1])
    result5 = dice.d80(result4[1])
    result6 = dice.d80(result5[1])
    result7 = dice.d80(result6[1])
    result8 = dice.d80(result7[1])
    result_final = result1[0]+result2[0]+result3[0]+result4[0]+result5[0]+result6[0]+result7[0]+result8[0]
    return [result_final,result8[1]]

def _1d10(poids):
    return dice.d10(poids)

def _1d30(poids):
    return dice.d30(poids)

def _1d4(poids):
    result = dice.d4(poids)
    result_str = {
        1: "Feu",
        2: "Eau",
        3: "Vent",
        4: "Terre"
    }.get(result[0], "")
    return [result_str,result[1]]

def _1d5(poids):
    result = dice.d5(poids)
    result_str = {
        1: "Force",
        2: "Agilité",
        3: "Discrétion",
        4: "Constitution",
        5: "Charisme"
    }.get(result[0], "")
    return [result_str,result[1]]

# Ouverture de crystite
def debut(poids9, poids3):
    result1 = _1d9(poids9)
    result2 = _1d3(poids3)
    final = result1[0]

    # Vérifie si l'équipement est une armure
    armure = final in ["Bouclier", "Casque", "Plastron", "Jambière", "Brassard"]
    if armure:
        final += " - " + result2[0]
    return [final,result1[1],result2[1]]

# Fonction générique pour le calcul de la statistique hybride
def adjust_stat_for_hybride(stat, str_result):
    if re.search(r'Hybride$', str_result):
        if stat % 2 == 1:
            stat += 1
        stat //= 2
    return stat

# Crystite Blanche
def blanc():
    global json_data
    #generer la crystite
    result1 = debut(json_data['d9'], json_data['d3'])
    result2 = _1d20(json_data['d20'])

    stat1 = adjust_stat_for_hybride(result2[0], result1[0])

    #modifier le json
    json_data['d9'] = result1[1]
    json_data['d3'] = result1[2]
    json_data['d20'] = result2[1]

    #return
    return f" - {result1[0]} => Statistique principale : {stat1}"


# Crystite Verte
def vert():
    global json_data
    #generer la crystite
    result1 = debut(json_data['d9'], json_data['d3'])
    result2 = _3d30(json_data['d30'])
    result3 = _1d10(json_data['d10'])
    result4 = _1d4(json_data['d4'])

    stat1 = adjust_stat_for_hybride(result2[0], result1[0])
    stat2 = f"+{result3[0]} {result4[0]}"

    #modifier le json
    json_data['d9'] = result1[1]
    json_data['d3'] = result1[2]
    json_data['d30'] = result2[1]
    json_data['d10'] = result3[1]
    json_data['d4'] = result4[1]
    
    #return
    return f" - {result1[0]} => Statistique principale : {stat1}, {stat2}"


# Crystite Bleue
def bleu():
    global json_data
    #generer la crystite
    result1 = debut(json_data['d9'], json_data['d3'])
    json_data['d3'] = result1[2]
    result2 = _5d80(json_data['d80'])
    result3 = _1d20(json_data['d20'])
    result4 = _1d10(json_data['d10'])
    result5 = _1d4(json_data['d4'])
    result6 = _1d4(result5[1])
    result7 = _1d5(json_data['d5'])
    result8 = dice.d100(json_data['d100'])

    stat1 = adjust_stat_for_hybride(result2[0], result1[0])
    stat2 = f"+{result3[0]} {result5[0]}"
    stat3 = f"+{result4[0]} "
    if (random.randint(0, 1)): stat3 += f"{result6[0]}"
    else: stat3 += f"{result7[0]}"
    if (result8[0] == 1):
        json_data['d100'] = result8[1]
        bonus = bonus_zopu(result1[0][0])
    else: bonus = ""

    #modifier le json
    json_data['d9'] = result1[1]
    json_data['d80'] = result2[1]
    json_data['d20'] = result3[1]
    json_data['d10'] = result4[1]
    json_data['d4'] = result6[1]
    json_data['d5'] = result7[1]

    #return
    return f" - {result1[0]} => Statistique principale : {stat1}, {stat2}, {stat3} {bonus}"

# Crystite Orange
def orange():
    global json_data
    #generer la crystite
    result1 = debut(json_data['d9'], json_data['d3'])
    json_data['d3'] = result1[2]
    result2 = _8d100(json_data['d100'])
    result3 = _1d30(json_data['d30'])
    result4 = _1d20(json_data['d20'])
    result5 = _1d4(json_data['d4'])
    result6 = _1d4(result5[1])
    result7 = _1d5(json_data['d5'])
    result8 = dice.d100(result2[1])
    result9 = dice.d10(json_data['d10'])

    stat1 = adjust_stat_for_hybride(result2[0], result1[0])
    stat2 = f"+{result3[0]} {result5[0]}"
    stat3 = f"+{result4[0]} "
    if (random.randint(0, 1)): stat3 += f"{result6[0]}"
    else: stat3 += f"{result7[0]}"
    stat4 = f"+{result9[0]} Exaltation"
    if (result8[0] == 1):
        json_data['d100'] = result8[1]
        bonus = bonus_zopu(result1[0][0])
    else: bonus = ""

    #modifier le json
    json_data['d9'] = result1[1]
    json_data['d30'] = result3[1]
    json_data['d20'] = result4[1]
    json_data['d4'] = result6[1]
    json_data['d5'] = result7[1]
    json_data['d10'] = result9[1]

    #generer la crystite
    result1 = debut(json_data['d9'], json_data['d3'])
    stat1 = adjust_stat_for_hybride(_8d100(), result1[0])
    stat2 = f"+{_1d30()} {_1d4()}"
    stat3 = f"+{_1d20()} {_1d4()}" if random.randint(0, 1) else f"+{_1d20()} {_1d5()}"
    stat4 = f"+{_1d10()} Exaltation"
    bonus = bonus_zopu(result1[0][0]) if random.randint(1, 100) <= 5 else ""

    return f" - {result1[0]} => Statistique principale : {stat1}, {stat2}, {stat3}, {stat4} {bonus}"


# Bonus zopu
def bonus_zopu(type):
    global json_data
    #valeur utile
    reroll = 1
    listBonus = []
    isArmure = True

    if type == "A":
        isArmure = False

    #boucle de reroll
    while reroll > 0:
        result = dice.d100(json_data['d100'])
        json_data['d100'] = result[1]
        
        match result[0]:
            case 1 | 2 | 3 | 4 | 5:
                #lancer un autre D
                result2 = dice.d3(json_data['d3'])
                json_data['d3'] = result2[1]

                #ajouter le bon bonus
                reroll -= 1
                if result2[0] == 1: listBonus.append("Suprême")
                if result2[0] == 2: listBonus.append("Indestructibilité")
                if result2[0] == 3: reroll += 2

            case 6 | 7 | 8 | 9 | 10:
                #lancer un autre D
                result2 = dice.d2(json_data['d2'])
                json_data['d2'] = result2[1]

                #ajouter le bon bonus
                reroll -= 1
                if result2[0] == 1: listBonus.append("Résistance")
                if result2[0] == 2: listBonus.append("Que de générosité")

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
                if isArmure:
                    listBonus.append("REPLI !!!")
                else:
                    listBonus.append("Fantôme")

            case 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60:
                #heu... faut relancer a priorie
                reroll -= 1
                reroll += 1

            case 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70:
                #bonus
                reroll -= 1
                if isArmure:
                    listBonus.append("Gruyère")
                else:
                    listBonus.append("I'm stuck Step-Monster")

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
                result2 = dice.d2(json_data['d2'])
                json_data['d2'] = result2[1]

                #ajouter le bon bonus
                reroll -= 1
                if result2[0] == 1: listBonus.append("Fragilité")
                if result2[0] == 2: listBonus.append("Connard")

            case 96 | 97 | 98 | 99 | 100:
                #lancer un autre D
                result2 = []
                if isArmure: result2 = dice.d2(json_data['d2'])
                if not isArmure: result2 = dice.d3(json_data['d3'])

                #ajouter le bon bonus
                reroll -= 1
                if result2[0] == 1: listBonus.append("Inutile")
                if result2[0] == 2: listBonus.append("Maudit")
                if result2[0] == 3: listBonus.append("Machette ornithologique")

                #update json
                if isArmure: json_data['d2'] = result2[1]
                else: json_data['d3'] = result2[1]

    #formatage du string
    reponse = "["
    for i in range(len(listBonus)):
        if i > 0:
            reponse += ", "
        reponse += listBonus[i]
    reponse += "]"

    return reponse



        