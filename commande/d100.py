import commande.dice as dice

async def run(ctx):
    #choix du chiffre random
    result = dice.d100(ctx)

    #message different celon le chiffre
    if result == 1:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            '║  SUCCÈS ABSOLUE (1)  ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    elif 2 <= result <= 5:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            f'║ SUCCÈS CRITIQUE ({result})  ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    elif 96 <= result <= 99:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            f'║ ÉCHEC CRITIQUE ({result})  ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    elif result == 100:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            '║ ÉCHEC ABSOLU (100)   ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    elif result == 69:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            '║ Résultat : 69 (nice) ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    elif 6 <= result <= 9:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            f'║     Résultat : {result}     ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    else:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'
            '╟──────────────────────╢\n'
            f'║    Résultat : {result}     ║\n'
            '╚══════════════════════╝\n'
            '```'
        )
    
    #envoyer le message sur le serveur
    await ctx.respond(message)