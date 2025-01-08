from datetime import datetime
import textwrap
import time
import discord
import commande.dice as dice
import os

async def run(ctx,taille):
    # Premier message pour savoir se qui se passe
    pieces = 10000*taille
    formatted_pieces = "{:,}".format(pieces).replace(",", " ")
    await ctx.respond(f"Utilisation de {formatted_pieces} pièces dans la roue de l'infortune pour <@{ctx.author.id}>")

    #reglage de la taille
    width = 0
    match taille:
        case 100:
            width = 36
        case 1000:
            width = 65
        case 10000:
            width = 100
    width2 = width-2
    
    # creation des chiffre random (lancer de 100d100)
    result_str = ""
    result_int = []
    for i in range(taille):
        resultat = dice.d100()
        result_int.append(resultat)
        result_str += f"{resultat} "

    # Écrire la réponse qui contient tout les chiffres obtenues
    message = f"╔{'═'*width}╗\n"
    roue = "Roue de l'infortune"
    message += f"║ {roue:^{width2}} ║\n"
    message += f"╟{'─'*width}╢\n"
    
    wrapped = textwrap.wrap(result_str, width2)
    for line in wrapped:
        message += f"║ {line.ljust(width2)} ║\n"
    
    message += f"╚{'═'*width}╝\n"

    #creer un fichier
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    file_path = f"casino_{timestamp}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(message)
    
    #envoyer le fichier
    await ctx.send(file=discord.File(file_path))

    #calculer les crystites generer
    orange = 0
    bleu = 0
    vert = 0
    blanche = 0
    violette = 0
    rouge = 0

    #regarder chaque chiffre et savoir se que cela fait
    for i in result_int:
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
    
    #suppression du fichier apres quelque secondes (au cas ou sa prendr du temps a envoyer le fichier)
    time.sleep(10)
    os.remove(file_path)
