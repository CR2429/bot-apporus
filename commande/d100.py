import random

async def run(ctx):
    #chjoix du chiffre random
    result = random.randint(1,100)

    #message different celon le chiffre
    if result == 1:
        message = (
            '```\n'
            '╔══════════════════════╗\n'
            '║    Jet d\'un d100     ║\n'  
            '╟──────────────────────╢\n'
            '║ CRITIQUE ABSOLUE (1) ║\n'
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
    
    await ctx.respond(message)