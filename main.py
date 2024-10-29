import discord
from discord.ext import commands
from commande.d100 import run as d100
from commande.roll import run as roll

#propriete
contenu = ''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
GUILD_IDS = [587086433970552840,1183006208869797898]

#recuper le token
with open('token.txt', 'r') as fichier:
    contenu = fichier.read()

#commande
@bot.slash_command(name = "allo", description="Un simple Hello World!", GUILD_IDS=GUILD_IDS)
async def allo(interaction):
    await interaction.response.send_message("Hello World!")

@bot.slash_command(name="d100", description="lance un 1d100", GUILD_IDS=GUILD_IDS)
async def command_d100(interaction):
    await d100(interaction)

@bot.slash_command(name="r", description="Lance des des. Exemple : 25d100", GUILD_IDS=GUILD_IDS)
async def command_roll(interaction, dice: str):
    await roll(interaction,dice)


#log
@bot.event
async def on_ready():
    print("Le bot est prêt !")

#run le bot
bot.run(contenu)