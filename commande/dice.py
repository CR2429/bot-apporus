import random

def d2(poids):
    return lancer_de(2, poids)

def d3(poids):
    return lancer_de(3, poids)

def d4(poids):
    return lancer_de(4, poids)

def d5(poids):
    return lancer_de(5, poids)

def d9(poids):
    return lancer_de(9, poids)

def d10(poids):
    return lancer_de(10, poids)

def d20(poids):
    return lancer_de(20, poids)

def d30(poids):
    return lancer_de(30, poids)

def d80(poids):
    return lancer_de(80, poids)

def d100(poids):
    return lancer_de(100, poids)

def lancer_de(sides, poids):
    """
    Lancer un dé avec un nombre de côtés spécifié, mettre à jour les poids et les retourner.
    """
    # Obtenir un nombre aléatoire basé sur les poids
    numbers = list(range(1, sides + 1))
    r = random.choices(numbers, weights=poids, k=1)[0]

    # Mettre à jour les poids
    for i in range(sides):
        if i + 1 == r:
            poids[i] -= sides
        else:
            poids[i] += 1

        # Limiter les poids
        poids[i] = max(1, min(poids[i], sides*2))

    return [r, poids]