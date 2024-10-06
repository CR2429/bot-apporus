import discord
from discord import app_commands

#propriete
contenu = ''
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=bot)

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()

#log
@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=587086433970552840))
    print("Le bot est prêt !")


#message 
@bot.event
async def on_message(message: discord.Message):
    print(message.guild.id)

#commande
@tree.command(name = "allo", description="Un simple Hello World!",guild=discord.Object(id=587086433970552840))
async def allo(interaction):
    await interaction.response.send_message("Hello World!")


#run le bot
bot.run(contenu)