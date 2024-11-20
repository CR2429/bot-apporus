import random
import re
import commande.dice as dice


# Lancer de dés
def _1d9():
    result = dice.d9()
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
    result = dice.d3()
    result_str = {
        1: "Armure",
        2: "Barrière",
        3: "Hybride"
    }.get(result, "")
    return result_str

def _1d20():
    return dice.d20()

def _3d30():
    result = dice.d30()
    result += dice.d30()
    result += dice.d30()
    
    return result

def _5d80():
    result = dice.d80()
    result += dice.d80()
    result += dice.d80()
    result += dice.d80()
    result += dice.d80()
    
    return result

def _8d100():
    result = dice.d100()
    result += dice.d100()
    result += dice.d100()
    result += dice.d100()
    result += dice.d100()
    result += dice.d100()
    result += dice.d100()
    result += dice.d100()

    return result

def _1d10():
    return dice.d10()

def _1d30():
    return dice.d30()

def _1d4():
    result = dice.d4()
    result_str = {
        1: "Feu",
        2: "Eau",
        3: "Vent",
        4: "Terre"
    }.get(result, "")
    return result_str

def _1d5():
    result = dice.d5()
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
    result1 = _1d9()
    result2 = _1d3()
    final = result1

    # Vérifie si l'équipement est une armure
    armure = final in ["Bouclier", "Casque", "Plastron", "Jambière", "Brassard"]
    if armure:
        final += " - " + result2
    return final

# Fonction générique pour le calcul de la statistique hybride
def adjust_stat_for_hybride(stat, str_result):
    if re.search(r'Hybride$', str_result):
        if stat % 2 == 1:
            stat += 1
        stat //= 2
    return stat

# Crystite Blanche
def blanc():
    #generer la crystite
    typeEquipement = debut()
    stat1 = _1d20()

    stat1 = adjust_stat_for_hybride(stat1, typeEquipement)

    #return
    return f" - {typeEquipement} => Statistique principale : {stat1}"

# Crystite Verte
def vert():
    #generer la crystite
    TypeEquipement = debut()
    Stat1 = _3d30()
    Stat2 = _1d10()
    Element = _1d4()

    stat1 = adjust_stat_for_hybride(Stat1, TypeEquipement)
    stat2 = f"+{Stat2} {Element}"
    
    #return
    return f" - {TypeEquipement} => Statistique principale : {stat1}, {stat2}"


# Crystite Bleue
def bleu():
    #generer la crystite
    result1 = debut()
    result2 = _5d80()
    result3 = _1d20()
    result4 = _1d10()
    result5 = _1d4()
    result6 = _1d4()
    result7 = _1d5()
    result8 = dice.d100()

    stat1 = adjust_stat_for_hybride(result2, result1)
    stat2 = f"+{result3} {result5}"
    stat3 = f"+{result4} "
    if (random.randint(0, 1)): stat3 += f"{result6}"
    else: stat3 += f"{result7}"
    if (result8 == 1):
        bonus = bonus_zopu(result1[0])
    else: bonus = ""

    #return
    return f" - {result1} => Statistique principale : {stat1}, {stat2}, {stat3} {bonus}"

# Crystite Orange
def orange():
    #generer la crystite
    result1 = debut()
    result2 = _8d100()
    result3 = _1d30()
    result4 = _1d20()
    result5 = _1d4()
    result6 = _1d4()
    result7 = _1d5()
    result8 = dice.d100()
    result9 = dice.d10()

    stat1 = adjust_stat_for_hybride(result2, result1)
    stat2 = f"+{result3} {result5}"
    stat3 = f"+{result4} "

    if (random.randint(0, 1)): stat3 += f"{result6}"
    else: stat3 += f"{result7}"
    stat4 = f"+{result9} Exaltation"
    if (result8 == 1):
        bonus = bonus_zopu(result1[0])
    else: bonus = ""

    #return
    return f" - {result1} => Statistique principale : {stat1}, {stat2}, {stat3}, {stat4} {bonus}"


# Bonus zopu
def bonus_zopu(type):
    #valeur utile
    reroll = 1
    listBonus = []
    isArmure = True

    if type == "A":
        isArmure = False

    #boucle de reroll
    while reroll > 0:
        result = dice.d100()
        
        match result:
            case 1 | 2 | 3 | 4 | 5:
                #lancer un autre D
                result2 = dice.d3()

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1: listBonus.append("Suprême")
                if result2 == 2: listBonus.append("Indestructibilité")
                if result2 == 3: reroll += 2

            case 6 | 7 | 8 | 9 | 10:
                #lancer un autre D
                result2 = dice.d2()

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1: listBonus.append("Résistance")
                if result2 == 2: listBonus.append("Que de générosité")

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
                result2 = dice.d2()

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1: listBonus.append("Fragilité")
                if result2 == 2: listBonus.append("Connard")

            case 96 | 97 | 98 | 99 | 100:
                #lancer un autre D
                result2 = []
                if isArmure: result2 = dice.d2()
                if not isArmure: result2 = dice.d3()

                #ajouter le bon bonus
                reroll -= 1
                if result2 == 1: listBonus.append("Inutile")
                if result2 == 2: listBonus.append("Maudit")
                if result2 == 3: listBonus.append("Machette ornithologique")

    #retrait bonus en cas de maudit
    if "Maudit" in listBonus:
        listBonus = ["Maudit"]

    #formatage du string
    reponse = "["
    for i in range(len(listBonus)):
        if i > 0:
            reponse += ", "
        reponse += listBonus[i]
    reponse += "]"

    return reponse

# Grosse Crystite Orange
def big_orange():
    #generer la crystite
    typeArmure = _1d3()
    typeArme = dice.d4()
    statsPrincipale = _8d100()
    statsElementaire = _1d30()
    typeElement = _1d4()
    statsSecondaire = _1d20()
    typeSecondaire = ""
    if (random.randint(0,1)) :
        typeSecondaire = _1d4()
    else :
        typeSecondaire = _1d5()
    statsExaltation = _1d10()
    BonusZopu = bonus_zopu("A")

    #changer le type Arme pour la bonne chose
    if (typeArme == 1):
        typeArme == "Arme 1 main tranchante"
    if (typeArme == 2):
        typeArme == "Arme 1 main contondante"
    if (typeArme == 3):
        typeArme == "Arme 2 main tranchante"
    if (typeArme == 4):
        typeArme == "Arme 2 main contondante"

    #changer le bonus zopu
    BonusZopuArmure = []
    BonusZopu2 = BonusZopu.strip("[]").split(", ")
    for i in range(len(BonusZopu2)):
        if (BonusZopu2[i]=="Machette ornithologique"):
            BonusZopuArmure.append("Inutile")
        elif (BonusZopu2[i]=="I'm stuck Step-Monster"):
            BonusZopuArmure.append("Gruyère")
        elif (BonusZopu2[i]=="Fantôme"):
            BonusZopuArmure.append("REPLI !!!")
        else:
            BonusZopuArmure.append(BonusZopu2[i])
    
    #formatage du string
    reponse = "["
    for i in range(len(BonusZopuArmure)):
        if i > 0:
            reponse += ", "
        reponse += BonusZopuArmure[i]
    reponse += "]"
    BonusZopuArmure = reponse

    #En cas hybridation
    IsHybride = adjust_stat_for_hybride(statsPrincipale, typeArmure)

    #formatage de la reponse
    reponse = (
        f"\n"
        f"\nVous avez un set d'armure complete avec une arme"
        f"\n- Stat de l'armure: {IsHybride} {typeArmure}"
        f"\n- Bonus de l'armure : {BonusZopuArmure}"
        f"\n- Stat de l'arme: {statsPrincipale}"
        f"\n- Bonus de l'arme: {BonusZopu}"
        f"\n- Stat Elementaire 1: {statsElementaire} {typeElement}"
        f"\n- Stat Elementaire 2: {statsSecondaire} {typeSecondaire}"
        f"\n- Exaltation: {statsExaltation}"
    )
    return reponse