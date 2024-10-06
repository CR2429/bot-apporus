import discord

#recuper le token
contenu = ''
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()
print(contenu)

#run le bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)
client.run(contenu)