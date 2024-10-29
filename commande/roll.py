import random
import asyncio

async def run(ctx, dice:str):
    try:
        #separation des chiffres
        nombre_des, nombre_faces = map(int, dice.split('d'))
        
        #check
        if nombre_des <= 0 or nombre_faces <= 0 :
            raise ValueError
        
        #lancer de des
        rolls = [random.randint(1,nombre_faces) for _ in range(nombre_des)]
        total = sum(rolls)

        #reponse
        reponse = (
            f'Jet de {dice} :\n'
            '=====\n'
            f'{rolls}\n'
            '=====\n'
            f'total : {total}'
            )
        
        #un ou plusieur message
        if len(reponse) <= 2000 : 
            await ctx.respond(reponse)
        else :
            await ctx.respond('Sa va prendre 5 seconde a cause de la taille du message')
            await asyncio.sleep(5)
            parts = [reponse[i:i+2000] for i in range(0, len(reponse), 2000)]
            await ctx.send(parts[0])
            
            for part in parts[1:]:
                await ctx.send(part)

    except ValueError:
        await ctx.respond(f"Hey c'est quoi ce dé: ``{dice}``. Tu vas me reecrire ta commande ||connard|| ")