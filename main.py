import discord

#propriete
contenu = ''
intents = discord.Intents.default()
client = discord.Client(intents=intents)

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()

#log
@client.event
async def on_ready():
    print("Le bot est prêt !")


#commande
@client.event
async def on_message(message):
    print(message)


#run le bot
client.run(contenu)