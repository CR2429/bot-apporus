import discord

#recuper le token
contenu = ''
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()
print(contenu)

#run le bot
client = discord.Client()
client.run(contenu)