import random

async def run(ctx):
    # Premier message pour savoir se qui se passe
    await ctx.respond(f"Utilisation de 1 000 000 pièces dans la roue de l'infortune pour <@{ctx.author.id}>")

    # creation des chiffre random (lancer de 100d100)
    result = [random.randint(1, 100) for _ in range(100)]
    r = [result[i:i+10] for i in range(0, len(result), 10)]

    # Écrire la réponse qui contient tout les chiffres obtenues
    message = "```\n"
    message += f"╔{'═'*36}╗\n"
    roue = "Roue de l'infortune"
    message += f"║ {roue:^34} ║\n"
    message += f"╟{'─'*36}╢\n"
    for rr in r[0:]:
        formatted_row = " ".join(map(str, rr))
        message += f"║ {formatted_row:^34} ║\n"
    
    message += f"╚{'═'*36}╝\n```"

    #envoyer message sur le serveur
    await ctx.send(message)

    #calculer les crystites generer
    orange = 0
    bleu = 0
    vert = 0
    blanche = 0
    violette = 0
    rouge = 0

    #regarder chaque chiffre et savoir se que cela fait
    for i in result:
        if i == 1:
            orange += 4
        elif 2 <= i <= 5:
            orange += 2
        elif 6 <= i <= 15:
            orange += 1
        elif 16 <= i <= 50:
            bleu += 1
        elif 51 <= i <= 75:
            vert += 1
        elif 76 <= i <= 95:
            blanche += 1
        elif 96 <= i <= 99:
            violette += 1
        else:
            rouge += 1
    
    #message a envoyer sur le serveur
    await ctx.send(
        f'**Vous avez recu ces cristytes :**\n'
        f' - {orange} crystite orange\n'
        f' - {bleu} crystite bleu\n'
        f' - {vert} crystite verte\n'
        f' - {blanche} crystite blanche\n'
        f' - {violette} crystite violette\n'
        f' - {rouge} crystite rouge\n'
    )

