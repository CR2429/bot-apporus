import discord
from discord.ext import commands
from discord.ui import Button,View

class Bouton(View):
    def __init__(self, bot):
        super().__init__()

        # Ajouter un bouton à la vue
        self.bot = bot
        self.add_item(Button(label="Cliquez la", style=discord.ButtonStyle.primary))

    @discord.ui.button(label="Cliquez ici", style=discord.ButtonStyle.primary)
    async def button_click(self, button: Button, interaction: discord.Interaction):
        try:
            # Envoyer un message dans un autre serveur
            other_channel = self.bot.get_channel(1183006208869797901)
            if other_channel:
                await other_channel.send("Le bot est en vie, vous pouvez utiliser ses commandes.")
                await interaction.response.send_message("Message envoyé sur un autre serveur.", ephemeral=True)
            else:
                await interaction.response.send_message("Erreur : Canal non trouvé.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Erreur : {e}", ephemeral=True)