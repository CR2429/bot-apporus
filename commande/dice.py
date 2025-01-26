import random
import mysql.connector

# Récupérer le mot de passe
motdepasse = ""
connection = None
with open('passwordSQL.txt', 'r') as fichier:
    motdepasse = fichier.read().strip()

def d2():
    return random.randint(1,2)

def d3():
    return random.randint(1,3)

def d4():
    return random.randint(1,4)

def d5():
    return random.randint(1,5)

def d9():
    return random.randint(1,9)

def d10():
    return random.randint(1,10)

def d20():
    return random.randint(1,20)

def d30():
    return random.randint(1,30)

def d80():
    return random.randint(1,80)

def d100(ctx = ""):
    if (ctx != ""):
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
            # Generation de mon chiffre aleatoire
            user_id = int(ctx.author.id)
            chiffre100 = random.randint(1,100)
            
            #commande sql
            sql_query = "INSERT INTO dice_logs (user_id, result) VALUES (%s, %s)"
            params = (user_id, chiffre100)
            cursor.execute(sql_query, params)
            connection.commit()
            
            #renvoyer le resultat tout de meme du d100
            print(f"Lancer de dé enregistré avec succès pour l'utilisateur {user_id} : {chiffre100}")
            return chiffre100
        
        #gestion des erreurs
        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")
        except ValueError:
            print("Erreur : ctx.author.id n'est pas un entier valide.")
        finally:
            if connection:
                connection.close()
                print("Connexion à la base de données fermée.")
    
    return random.randint(1,100)