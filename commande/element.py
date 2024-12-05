import discord
from discord.ext import commands

data = {
  "elements": [
    {"name": "Feu", "level": 1},
    {"name": "Eau", "level": 1},
    {"name": "Vent", "level": 1},
    {"name": "Terre", "level": 1},
    {"name": "Eau déminéralisée", "level": 1, "description":"element de chimie"},
    {"name": "Sel", "level": 1, "description": "element de chimie"},
    {"name": "Tornade", "level": 2},
    {"name": "Napalm", "level": 2},
    {"name": "Pression", "level": 2},
    {"name": "Glace", "level": 2},
    {"name": "Pierre", "level": 2},
    {"name": "Pluie", "level": 2},
    {"name": "Lave", "level": 2},
    {"name": "Boue", "level": 2},
    {"name": "Sable", "level": 2},
    {"name": "Électricité", "level": 2},
    {"name": "Argile", "level": 3},
    {"name": "Sable mouvant", "level": 3},
    {"name": "Bombe instable", "level": 3},
    {"name": "Magna", "level": 3},
    {"name": "Végétation", "level": 3},
    {"name": "Sable chaud", "level": 3},
    {"name": "Verre", "level": 4},
    {"name": "Lumière bioluminescente", "level": 4},
    {"name": "Roche", "level": 4},
    {"name": "Liquide réfrigérant", "level": 4},
    {"name": "Inquendance", "level": 4},
    {"name": "Tornade ardente", "level": 4},
    {"name": "Tempête", "level": 4},
    {"name": "Herbe sèche", "level": 4},
    {"name": "Proto stase", "level": 4},
    {"name": "Croissance", "level": 5},
    {"name": "Béton", "level": 5},
    {"name": "Spore malveillant", "level": 5},
    {"name": "Plexiglas", "level": 8},
    {"name": "Quartz", "level": 8, "description":"Oui anno... des lances de quartz... (au passage le bonus de cu de sac donne un lancer de 17d540)"},
    {"name": "Zéro absolu", "level": 8},
    {"name": "Mousse électrique", "level": 8,"description":"La solution pour avoir une source d'energie pres du village des plaines"},
    {"name": "Calcination", "level": 8},
    {"name": "Typhon", "level": 8},
    {"name": "Brume épaisse", "level": 8},
    {"name": "Pluie acide", "level": 8},
    {"name": "Explosion MK1", "level": 8},
    {"name": "Bombe fumigène", "level": 10},
    {"name": "Champignon malveillant", "level": 10},
    {"name": "Minerai de fer", "level": 11},
    {"name": "Brume aveuglante", "level": 12},
    {"name": "Explosion MK2", "level": 16},
    {"name": "Malveillance fongique", "level": 20, "description":"Origine de l'enfant avorter de 8 mois d'Alice"},
    {"name": "Fer raffiné", "level": 22},
    {"name": "Amant", "level": 24},
    {"name": "Béton armé", "level": 27},
    {"name": "Acier", "level": 24},
    {"name": "Acier galvanisé", "level": 29, "description":"Liam a emmenager dans un appartement de 1,5m²"},
    {"name": "Universalis", "level": 32, "description":"Tu veux rencontrer une divinite? Bas va si essaye Universalis. (Au passage, normalement c'est niveau 16 mais zopu confirme le niveau 32)"},
    {"name": "Explosion MK3", "level": 32},
    {"name": "Ferraille", "level": 46, "description":"Solution facile pour se faire de l'argent"},
    {"name": "Dynamique métallique", "level": 54},
    {"name": "Mamamia", "level":64, "description": "Attention, risque de destruction d'un biome possible"},
    {"name": "Patate", "level":1, "description": "Element qui est le plus mortel"},
  ],
  "levels": {
    "1": "1d10",
    "2": "2d30",
    "3": "3d50",
    "4": "5d80",
    "5": "7d110",
    "6": "9d150",
    "7": "13d200",
    "8": "17d270",
    "9": "20d340",
    "10": "25d420",
    "11": "30d540",
    "12": "35d660",
    "13": "40d730",
    "14": "45d850",
    "15": "50d1000",
    "16": "55d1325",
    "17": "60d1900",
    "18": "65d2300",
    "19": "70d3000",
    "20": "80d3600",
    "21": "90d4500",
    "22": "100d5400",
    "23": "120d6300",
    "default": "?d???"
  }
}
ElementList = sorted(["Feu","Eau","Vent","Terre","Eau déminéralisée","Mamamia","Patate",
    "Sel","Tornade","Napalm",  "Pression","Glace","Pierre","Pluie","Lave","Boue","Sable","Électricité","Argile", "Sable mouvant","Bombe instable",
    "Magna","Végétation","Sable chaud","Verre","Lumière bioluminescente","Roche","Liquide réfrigérant","Inquendance","Tornade ardente","Tempête",
    "Herbe sèche","Proto stase","Croissance","Béton","Spore malveillant","Plexiglas","Quartz","Zéro absolu","Mousse électrique","Calcination","Typhon",
    "Brume épaisse","Pluie acide","Explosion MK1","Bombe fumigène","Champignon malveillant","Minerai de fer","Brume aveuglante","Explosion MK2",
    "Malveillance fongique","Fer raffiné","Amant","Béton armé","Acier","Acier galvanisé","Universalis","Explosion MK3","Ferraille","Dynamique métallique"
])
        
class ElementDropdown(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.current_page = 0
        self.total_pages = (len(ElementList) - 1) // 25 + 1
        self.update_components()
        
        
    def get_current_page_options(self):
        start = self.current_page * 25
        end = start + 25
        return ElementList[start:end]
    
    async def refresh_view(self, interaction: discord.Interaction):
        self.update_components()
        await interaction.response.edit_message(view=self)
    
    def update_components(self):
        self.clear_items()

        # Select par raport a la page
        options = [
            discord.SelectOption(label=element, value=element)
            for element in self.get_current_page_options()
        ]
        select = discord.ui.Select(placeholder="Choisissez un élément", options=options, max_values=1)
        select.callback = self.select_callback
        self.add_item(select)

        # Bouton de navigation
        prev_button = discord.ui.Button(label="Précédent", style=discord.ButtonStyle.primary, row=1)
        prev_button.callback = self.previous_page
        if self.current_page > 0:
            self.add_item(prev_button)

        next_button = discord.ui.Button(label="Suivant", style=discord.ButtonStyle.primary, row=1)
        next_button.callback = self.next_page
        if self.current_page < self.total_pages - 1:
            self.add_item(next_button)
           
    async def select_callback(self, interaction: discord.Interaction):
        element = interaction.data.get("values", [None])[0]
        
        element_name = element
        element_lvl = 0
        element_dice = "???"
        element_description = ""
        
        #trouver le niveau
        for e in data["elements"]:
            if e["name"] == element_name:
                element_lvl = e["level"]
                if e["level"] > 23:
                    element_dice = "A definir par zopu"
                else:
                    element_dice = data["levels"][f"{e['level']}"]
                
                element_description = e.get("description",None)
                break
            
        #creer la reponse
        max_width = 36
        message = "```"
        message += "╔══════════════════════════════════════╗\n"
        message += f"║ {element_name.center(max_width)} ║\n"
        message += "╟──────────────────────────────────────╢\n"
        message += f"║ Niveau : {element_lvl:<28}║\n"
        message += f"║ Jet de dés : {element_dice:<24}║\n"
        
        if element_description:
            message += "╟──────────────────────────────────────╢\n"
            # Découper la description en lignes sans couper les mots
            words = element_description.split(' ')
            current_line = ''
            
            for word in words:
                if len(current_line + ' ' + word) <= max_width:
                    current_line += ' ' + word
                else:
                    message += f"║ {current_line.strip().ljust(max_width)} ║\n"
                    current_line = word
            
            # Ajouter la dernière ligne si nécessaire
            if current_line:
                message += f"║ {current_line.strip().ljust(max_width)} ║\n"
                
        message += "╚══════════════════════════════════════╝```"
        
        if element:
            print(element)
            await interaction.response.send_message(message, ephemeral=False)
        
    async def previous_page(self, interaction: discord.Interaction):
        # action du bouton precedant
        if self.current_page > 0:
            self.current_page -= 1
            self.update_components()
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.send_message("Vous êtes déjà sur la première page.", ephemeral=True)

    async def next_page(self, interaction: discord.Interaction):
        # action du bouton suivant
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_components()
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.send_message("Vous êtes déjà sur la dernière page.", ephemeral=True)
            
    async def reponse(element):
        element_name = element
        element_lvl = 0
        element_dice = "???"
        element_description = ""
        
        #trouver le niveau
        for e in data["elements"]:
            if e["name"] == element_name:
                element_lvl = e["level"]
                if e["level"] > 23:
                    element_dice = "A definir par zopu"
                else:
                    element_dice = data["levels"][f"{e["level"]}"]
                
                element_description = e.get("description",None)
                break
            
        #creer la reponse
        max_width = 36
        message = "```"
        message += "╔════════════════════════════════════╗\n"
        message += f"║ {element_name.center(max_width)} ║\n"
        message += "╟────────────────────────────────────╢\n"
        message += f"║ Niveau : {element_lvl:<33}║\n"
        message += f"║ Jet de dés : {element_dice:<27}║\n"
        
        if element_description:
            message += "╟────────────────────────────────────╢\n"
            lines = [element_description[i:i + max_width] for i in range(0, len(element_description), max_width)]
            for line in lines:
                message += f"║ {line.ljust(max_width)} ║\n"
        message += "╚════════════════════════════════════╝```"
        
        print(message)
        
        return message