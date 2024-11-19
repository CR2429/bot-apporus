import discord
from discord.ext import commands
from commande.d100 import run as d100
from commande.roll import run as roll
from commande.casino import run as casino
import json
from commande.crystite import orange, bleu, vert, blanc, bonus_zopu

#propriete
contenu = ''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
GUILD_IDS = [587086433970552840,1183006208869797898] #les ids de mon serveur et du serveur du JDR
GUILD_ADMIN = [587086433970552840]

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()

def main():
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

    @bot.slash_command(name='crystite',description='Ouvrir les crystites',GUILD_IDS=GUILD_IDS)
    async def crystite_command(ctx, couleur: discord.Option(str, "La couleur de la crystite", choices=["Blanc","Vert","Bleu","Orange"]), nombre:str):
        try:
            #recuperer le nombre
            nombre = int(nombre)
            if nombre <= 0:
                raise ValueError

            #recuperer la reponse necessaire
            reponses = []
            for i in range(nombre):

                if (couleur == "Blanc"):
                    reponses.append(blanc())
                if (couleur == "Vert"):
                    reponses.append(vert())
                if (couleur == "Bleu"):
                    reponses.append(bleu())
                if (couleur == "Orange"):
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

    #commande pour avoir des effets
    @bot.slash_command(name='effet_zopu', description='Effet pour armes ou armures.', GUILD_IDS=GUILD_IDS)
    async def effet_zopu_command(ctx, option: discord.Option(str, "Arme ou Armure?", choices=["Arme", "Armure"]), nombre: str):
        try :
            #recupere le nombre
            nombre = int(nombre)
            if nombre <= 0:
                raise ValueError
            if nombre > 30:
                raise ValueError
            

            #executer la commande
            reponse = ""
            if option == "Arme":
                reponse = '**Voici les differents effet pour tes armes :**\n'
                for i in range(nombre):
                    reponse += f' - L\'arme nº {i+1} a comme bonus : {bonus_zopu("A")}\n'

            elif option == "Armure":
                reponse = '**Voici les differents effet pour tes armures :**\n'
                for i in range(nombre):
                    reponse += f' - La piece d\'armure nº {i+1} a comme bonus : {bonus_zopu("B")}\n'

            else: #nan mais faut vraiment etre cave si tu fait n'importe quoi
                raise ValueError

            #Envoyer la reponse
            await ctx.respond(reponse)
        except ValueError:
            await ctx.respond(f"Je ne comprends pas se que tu me veux... Je suis pas ta pute donc ecrit ta commande correctement, putin... (j'ai une limite de 30 item a la fois)")
            

    #kill bot
    @bot.slash_command(name='kill', description='arreter le bot' , GUILD_IDS=GUILD_IDS)
    async def kill(ctx):
        if ctx.author.id == 537398938102398998:
            #kill
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

if __name__ == "__main__":
    main()