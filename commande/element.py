import discord
import mysql.connector
import textwrap  # Pour gérer les descriptions multi-lignes
import locale

# Récupérer le mot de passe
motdepasse = ""
with open('passwordSQL.txt', 'r') as fichier:
    motdepasse = fichier.read().strip()
    
# Définir la locale pour le tri insensible aux accents (en français par exemple)
locale.setlocale(locale.LC_COLLATE, 'fr_FR.UTF-8')


class ElementDropdown(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.ElementList = []
        self.elements = []
        self.levels = {}
        connection = None
        
        # Connexion à la base de données
        try:
            print("Connexion a la base de donne")
            connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='apporus',
                password=motdepasse,
                database='apporus'
            )
            print("connection reussite")
            
            # Utilisation explicite du curseur
            cursor = connection.cursor()
            try:
                # Charger les éléments
                cursor.execute("SELECT name, level, description FROM elements")
                rows = cursor.fetchall()
                print(f"{len(rows)} éléments récupérés.")

                self.elements = [{'name': row[0], 'level': row[1], 'description': row[2]} for row in rows]
                self.ElementList = sorted([row['name'] for row in self.elements], key=locale.strxfrm)
                print(f"{len(self.ElementList)} éléments ajoutés à la liste.")

                # Charger les niveaux
                cursor.execute("SELECT level, roll_pattern FROM levels")
                self.levels = {str(level): roll_pattern for level, roll_pattern in cursor.fetchall()}
                print(f"{len(self.levels)} niveaux récupérés.")
            finally:
                cursor.close()
        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")
        finally:
            if connection:
                connection.close()
                print("Connexion à la base de données fermée.")
            

        self.current_page = 0
        self.total_pages = (len(self.ElementList) - 1) // 25 + 1
        self.update_components()

    def get_current_page_options(self):
        start = self.current_page * 25
        end = start + 25
        return self.ElementList[start:end]

    def edit_message(self):
        #savoir les elements a afficher
        page_elements = self.get_current_page_options()
        first_element = page_elements[0] if page_elements else "N/A"
        last_element = page_elements[-1] if page_elements else "N/A"
        
        #message
        update_message = f"Choisisser un élément dans la liste : {first_element} à {last_element}"
        
        return update_message
    
    async def refresh_view(self, interaction: discord.Interaction):
        self.update_components()
        await interaction.response.edit_message(content = self.edit_message(), view=self)

    def update_components(self):
        self.clear_items()

        # Select correspondant à la page actuelle
        options = [
            discord.SelectOption(label=element, value=element)
            for element in self.get_current_page_options()
        ]
        select = discord.ui.Select(placeholder="Choisissez un élément", options=options, max_values=1)
        select.callback = self.select_callback
        self.add_item(select)

        # Boutons de navigation
        if self.current_page > 0:
            prev_button = discord.ui.Button(label="Précédent", style=discord.ButtonStyle.primary, row=1)
            prev_button.callback = self.previous_page
            self.add_item(prev_button)

        if self.current_page < self.total_pages - 1:
            next_button = discord.ui.Button(label="Suivant", style=discord.ButtonStyle.primary, row=1)
            next_button.callback = self.next_page
            self.add_item(next_button)
            

    async def select_callback(self, interaction: discord.Interaction):
        element = interaction.data.get("values", [None])[0]
        if not element:
            await interaction.response.send_message("Aucun élément sélectionné.", ephemeral=True)
            return

        # Trouver les détails de l'élément sélectionné
        selected_element = next((e for e in self.elements if e["name"] == element), None)
        if not selected_element:
            await interaction.response.send_message("Élément introuvable.", ephemeral=True)
            return

        element_lvl = selected_element["level"]
        element_dice = self.levels.get(str(element_lvl), "???")
        element_description = selected_element.get("description", "")

        # Formatage du message
        max_width = 36
        message = f"```╔{'═' * max_width}╗\n"
        message += f"║ {element.center(max_width - 2)} ║\n"
        message += f"╟{'─' * max_width}╢\n"
        message += f"║ Niveau : {element_lvl:<{max_width - 10}}║\n"
        message += f"║ Jet de dés : {element_dice:<{max_width - 14}}║\n"

        if element_description:
            message += f"╟{'─' * max_width}╢\n"
            wrapped_description = textwrap.wrap(element_description, max_width - 2)
            for line in wrapped_description:
                message += f"║ {line.ljust(max_width - 2)} ║\n"

        message += f"╚{'═' * max_width}╝```"

        await interaction.response.send_message(message, ephemeral=False)

    async def previous_page(self, interaction: discord.Interaction):
        if self.current_page > 0:
            self.current_page -= 1
            await self.refresh_view(interaction)
        else:
            await interaction.response.send_message("Vous êtes déjà sur la première page.", ephemeral=True)

    async def next_page(self, interaction: discord.Interaction):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            await self.refresh_view(interaction)
        else:
            await interaction.response.send_message("Vous êtes déjà sur la dernière page.", ephemeral=True)
