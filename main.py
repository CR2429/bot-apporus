import discord
from discord import app_commands
from discord.ext import commands
from commande.d100 import run as d100

#propriete
contenu = ''
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=bot)
bot.tree = tree

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()

#log
@bot.event
async def on_ready():
    GUILD_IDS = [587086433970552840,1183006208869797898]
    for guild_id in GUILD_IDS:
        guild = discord.Object(id=guild_id)
        await tree.sync(guild=guild)
    print("Le bot est prêt !")

#commande
@bot.tree.command(name = "allo", description="Un simple Hello World!",)
async def allo(interaction):
    await interaction.response.send_message("Hello World!")

@bot.tree.command(name="d100", description="lance un 1d100")
async def command_d100(interaction):
    await d100(interaction)

#run le bot
bot.run(contenu)