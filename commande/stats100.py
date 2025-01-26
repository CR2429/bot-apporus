from datetime import datetime
import math
import os
import discord
import mysql.connector

# Récupérer le mot de passe
motdepasse = ""
connection = None
with open('passwordSQL.txt', 'r') as fichier:
    motdepasse = fichier.read().strip()

# Fonction pour analyser les résultats
async def analyze_d100(user_id,ctx):
    try:
        # Connextion au serveur sql
        print("Connexion a la base de donne")
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='apporus',
            password=motdepasse,
            database='apporus'
        )
        print("connection reussite")
        cursor = connection.cursor()
        
        # Récupère tous les résultats
        cursor.execute("SELECT result FROM dice_logs WHERE user_id = %s", (user_id,))
        results = [row[0] for row in cursor.fetchall()]

        if not results:
            return f"L'utilisateur <@{user_id}> n'a aucun lancer enregistré."

        # Analyse des résultats
        total_rolls = len(results)
        average = sum(results) / total_rolls
        variance = sum((x - average) ** 2 for x in results) / total_rolls
        stddev = math.sqrt(variance)
        
        # Comptage des catégories
        success_absolute = sum(1 for result in results if result == 1)
        critical_success = sum(1 for result in results if 2 <= result <= 5)
        critical_failure = sum(1 for result in results if 96 <= result <= 99)
        absolute_failure = sum(1 for result in results if result == 100)  

        # Calcul des pourcentages
        success_absolute_percentage = (success_absolute / total_rolls) * 100
        critical_success_percentage = (critical_success / total_rolls) * 100
        critical_failure_percentage = (critical_failure / total_rolls) * 100
        absolute_failure_percentage = (absolute_failure / total_rolls) * 100  


        # Distribution
        cursor.execute("""
            SELECT result, COUNT(*) as count
            FROM dice_logs
            WHERE user_id = %s
            GROUP BY result
            ORDER BY result
        """, (user_id,))
        distribution = cursor.fetchall()

        # Préparation du message avec formatage
        analysis = discord.Embed(title=f"Statistiques des lancers de d100", color=discord.Color.blue())
        analysis.title = f"Statistiques des lancers de d100 de <@{user_id}>"
        analysis.add_field(name="🧮 Total des lancers", value=f"{total_rolls}", inline=False)
        analysis.add_field(name="📊 Moyenne des résultats", value=f"{average:.2f} (théorique : 50,5)", inline=False)
        analysis.add_field(name="📉 Écart-type", value=f"{stddev:.2f}", inline=False)
        analysis.add_field(name="🎯 Succès absolu (1)", value=f"{success_absolute} ({success_absolute_percentage:.2f}%)", inline=False)
        analysis.add_field(name="✨ Succès critique (2-5)", value=f"{critical_success} ({critical_success_percentage:.2f}%)", inline=False)
        analysis.add_field(name="💀 Échec critique (96-99)", value=f"{critical_failure} ({critical_failure_percentage:.2f}%)", inline=False)
        analysis.add_field(name="⚰️ Échec absolu (100)", value=f"{absolute_failure} ({absolute_failure_percentage:.2f}%)", inline=False)  
        
        # Générer un fichier texte pour la distribution
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        file_path = f"distribution_{timestamp}.txt"
        with open(file_path, 'w') as f:
            for result, count in distribution:
                f.write(f"{result} : {count} fois\n")

        # Envoi du fichier en pièce jointe
        await ctx.respond(f"<@{user_id}> voici tes statistiques des lancers de d100 !")
        await ctx.send(embed=analysis)
        await ctx.send(file=discord.File(file_path))

        # Supprimer le fichier après l'envoi
        os.remove(file_path)
    
    #gestion des erreurs
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        if connection:
            connection.close()
            print("Connexion à la base de données fermée.")