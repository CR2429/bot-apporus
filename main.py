import discord
from discord.ext import commands
from commande.d100 import run as d100
from commande.roll import run as roll
from commande.casino import run as casino
from commande.crystite import orange, bleu, blanc, vert

#propriete
contenu = ''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
GUILD_IDS = [587086433970552840,1183006208869797898] #les ids de mon serveur et du serveur du JDR

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()


#commande hello world
@bot.slash_command(name = "allo", description="Un simple Hello World!", GUILD_IDS=GUILD_IDS)
async def allo(ctx):
    await ctx.respond("Hello World!")
    #await casino(ctx)

#commande pour faire 1d100 rapidement
@bot.slash_command(name="d100", description="lance un 1d100", GUILD_IDS=GUILD_IDS)
async def command_d100(ctx):
    await d100(ctx)

#commande pour faire un jet de des custom
@bot.slash_command(name="r", description="Lance des des. Exemple : 25d100", GUILD_IDS=GUILD_IDS)
async def command_roll(ctx, dice: str):
    await roll(ctx,dice)

#commande pour la roue de l'infortune
@bot.slash_command(name='casino', description='amuse toi hovars', GUILD_IDS=GUILD_IDS)
async def casino_command(ctx):
    await casino(ctx)

#commande pour ouvrir les crystites orange
@bot.slash_command(name='crystite_orange', description='permet d\'ouvrir 1 ou plusieur crystite orange')
async def crystite_orange_command(ctx, nombre: str):
    try:
        #recuperer le nombre
        nombre = int(nombre)
        if nombre <= 0:
            raise ValueError

        #recuperer la reponse necessaire
        reponses = []
        for i in range(nombre):
            reponses.append(orange())
        reponses = [reponses[i:i+10] for i in range(0, len(reponses), 10)]

        #Envoyer les reponses
        await ctx.respond("Voici vos crystites :")
        for reponse in reponses:
            reponse = '\n'.join(reponse)
            await ctx.send(reponse)

    #ceci est un message d'erreur si on ecrit n'importe quoi
    except ValueError:
        await ctx.respond(f"Heu tu te moque de moi? ``{nombre}`` n")

#commande pour ouvrir les crystites bleu
@bot.slash_command(name='crystite_bleu', description='permet d\'ouvrir 1 ou plusieur crystite bleu')
async def crystite_bleu_command(ctx, nombre: str):
    try:
        #recuperer le nombre
        nombre = int(nombre)
        if nombre <= 0:
            raise ValueError

        #recuperer la reponse necessaire
        reponses = []
        for i in range(nombre):
            reponses.append(bleu())
        reponses = [reponses[i:i+10] for i in range(0, len(reponses), 10)]

        #Envoyer les reponses
        await ctx.respond("Voici vos crystites :")
        for reponse in reponses:
            reponse = '\n'.join(reponse)
            await ctx.send(reponse)

    #ceci est un message d'erreur si on ecrit n'importe quoi
    except ValueError:
        await ctx.respond(f"Heu tu te moque de moi? ``{nombre}`` n")

#commande pour ouvrir les crystites vert
@bot.slash_command(name='crystite_vert', description='permet d\'ouvrir 1 ou plusieur crystite vert')
async def crystite_vert_command(ctx, nombre: str):
    try:
        #recuperer le nombre
        nombre = int(nombre)
        if nombre <= 0:
            raise ValueError

        #recuperer la reponse necessaire
        reponses = []
        for i in range(nombre):
            reponse = '\n'.join(reponse)
            reponses.append(vert())
        reponses = [reponses[i:i+10] for i in range(0, len(reponses), 10)]

        #Envoyer les reponses
        await ctx.respond("Voici vos crystites :")
        for reponse in reponses:
            await ctx.send(reponse)

    #ceci est un message d'erreur si on ecrit n'importe quoi
    except ValueError:
        await ctx.respond(f"Heu tu te moque de moi? ``{nombre}`` n")

#commande pour ouvrir les crystites blanc
@bot.slash_command(name='crystite_blanc', description='permet d\'ouvrir 1 ou plusieur crystite blanc')
async def crystite_blanc_command(ctx, nombre: str):
    try:
        #recuperer le nombre
        nombre = int(nombre)
        if nombre <= 0:
            raise ValueError

        #recuperer la reponse necessaire
        reponses = []
        for i in range(nombre):
            reponses.append(blanc())
        reponses = [reponses[i:i+10] for i in range(0, len(reponses), 10)]

        #Envoyer les reponses
        await ctx.respond("Voici vos crystites :")
        for reponse in reponses:
            reponse = '\n'.join(reponse)
            await ctx.send(reponse)

    #ceci est un message d'erreur si on ecrit n'importe quoi
    except ValueError:
        await ctx.respond(f"Heu tu te moque de moi? ``{nombre}`` n")

#kill bot
@bot.slash_command(name='kill', description='arreter le bot')
async def kill(ctx):
    if ctx.author.id == 537398938102398998:
        await ctx.respond("Le bot est kill")
        await bot.close()
        sys.exit()
    else :
        #insulte pour le pirate
        await ctx.respond(":middle_finger: :middle_finger: :middle_finger:")

        #message priver pour moi
        owner = await bot.fetch_user(537398938102398998)
        await owner.send(
            f"🚨 Tentative non autorisée de tuer le bot !\n"
            f"Utilisateur : {ctx.author} (ID: {ctx.author.id})\n"
            f"Serveur : {ctx.guild.name} (ID: {ctx.guild.id})\n"
        )


#log pour savoir si le bot est en marche ou pas
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.CustomActivity(name="lancer les des (PUTIN J'AI FAIT UN 100)", emoji='🎲'))
    print("Le bot est prêt !")

#run le bot
bot.run(contenu)