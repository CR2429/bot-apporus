import random
import asyncio

async def run(ctx, dice:str):
    try:
        #separation des chiffres pour savoir combien j'ai de face et combien j'ai de dee
        nombre_des, nombre_faces = map(int, dice.split('d'))
        
        #verification que tout est correct dans les chiffre
        if nombre_des <= 0 or nombre_faces <= 0 :
            raise ValueError
        
        #lancer de des
        rolls = [random.randint(1,nombre_faces) for _ in range(nombre_des)]
        total = sum(rolls)

        #creation du mesage de reponse
        reponse = (
            f'Jet de {dice} :\n'
            '=====\n'
            f'{rolls}\n'
            '=====\n'
            f'total : {total}'
            )
        
        #savoir si je dois ecrire plusieur message ou pas
        if len(reponse) <= 2000 : 
            await ctx.respond(reponse)
        else : #comme il y a plu s de 2000 charactere je dois diviser mon message en plusieur partie
            await ctx.respond('Sa va prendre 5 seconde a cause de la taille du message')
            await asyncio.sleep(5)
            parts = [reponse[i:i+2000] for i in range(0, len(reponse), 2000)]
            await ctx.send(parts[0])
            
            for part in parts[1:]:
                await ctx.send(part)

    #ceci est un message d'erreur si on ecrit n'importe quoi
    except ValueError:
        await ctx.respond(f"Hey c'est quoi ce dé: ``{dice}``. Tu vas me reecrire ta commande ||connard|| ")