import discord

#propriete
contenu = ''
prefix = '!'
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()

#log
@bot.event
async def on_ready():
    print("Le bot est prêt !")


#commande
@bot.event
async def on_message(message: discord.Message):
    print(message.content)


#run le bot
bot.run(contenu)