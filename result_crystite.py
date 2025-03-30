from datetime import datetime
import os
import time

import discord
import pandas as pd


async def run(ctx,dictionnaire) :  
    # utiliser la bonne methode celon l'utilisateur
    if ctx.author.id == 0 :
        await hovars(ctx,dictionnaire)
    else :
        message = ""
        iterrence = len(dictionnaire["Type"])
        for i in range(iterrence):
            #element
            Type = dictionnaire["Type"][i]
            Armure = dictionnaire["Armure"][i]
            Stats_principale = dictionnaire["Stats principale"][i]
            Valeur_stat_2 = dictionnaire["Valeur stat 2"][i]
            Type_stat_2 = dictionnaire["Type stat 2"][i]
            Valeur_stat_3 = dictionnaire["Valeur stat 3"][i]
            Type_stat_3 = dictionnaire["Type stat 3"][i]
            Exaltation = dictionnaire["Exaltation"][i]
            Bonus = dictionnaire["Bonus"][i]
            
            #messsage
            message = message + f"- {Type} - {Armure} => {Stats_principale}, +{Valeur_stat_2} {Type_stat_2}, +{Valeur_stat_3} {Type_stat_3}, {Exaltation} exaltation, {Bonus}\n"
            
        #creation du fichier
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        file_path = f"crystite_{timestamp}.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(message)
        #envoyer le fichier
        await ctx.send(file=discord.File(file_path))
        
        #suppression du fichier apres quelque secondes (au cas ou sa prendr du temps a envoyer le fichier)
        time.sleep(10)
        os.remove(file_path)
            

async def hovars(ctx, dictionnaire) :
    data_armure = {
        "Armure": [],
        "Rarete": [],
        "armure": [],
        "barriere": [],
        "affinité feu": [],
        "affinités eau" : [],
        "affinités vent" : [],
        "affinités terre" : [],
        "caractéristique" : [],
        "exaltation" : [],
        "enchantement" : []
    }
    data_arme = {
        "Armes": [],
        "Rarete": [],
        "Dégats": [],
        "affinité feu": [],
        "affinités eau" : [],
        "affinités vent" : [],
        "affinités terre" : [],
        "caractéristique" : [],
        "exaltation" : [],
        "enchantement" : []
    }
    index = len(dictionnaire["Type"])
    
    for i in range(index):
        #element
        Type = dictionnaire["Type"][i]
        Armure = dictionnaire["Armure"][i]
        Couleur = dictionnaire["Couleur"][i]
        Stats_principale = dictionnaire["Stats principale"][i]
        Valeur_stat_2 = dictionnaire["Valeur stat 2"][i]
        Type_stat_2 = dictionnaire["Type stat 2"][i]
        Valeur_stat_3 = dictionnaire["Valeur stat 3"][i]
        Type_stat_3 = dictionnaire["Type stat 3"][i]
        Exaltation = dictionnaire["Exaltation"][i]
        Bonus = dictionnaire["Bonus"][i]
        
        #remplir la liste d'arme
        if (Armure == "") :
            #changement du nom
            if (Type == "Arme 1 main tranchante"):
                data_arme["Armes"].append("1mt")
            if (Type == "Arme 2 main tranchante"):
                data_arme["Armes"].append("2mt")
            if (Type == "Arme 1 main contondante"):
                data_arme["Armes"].append("1mc")
            if (Type == "Arme 2 main contondante"):
                data_arme["Armes"].append("2mc")
                
            #ajout facile a faire
            data_arme["Rarete"].append(Couleur)
            data_arme["Dégats"].append(Stats_principale)
            data_arme["enchantement"].append(Bonus)
            data_arme["exaltation"].append(Exaltation)

            #drapeau des stats
            feu = True
            eau = True
            vent = True
            terre = True
            autre = True
            
            #les stats bonus
            if (Type_stat_2 == Type_stat_3):
                stat = int(Valeur_stat_2) + int(Valeur_stat_3)
                if (Type_stat_2 == "Feu"):
                    data_arme["affinité feu"].append(stat)
                    feu = False
                elif (Type_stat_2 == "Eau"):
                    data_arme["affinités eau"].append(stat)
                    eau = False
                elif (Type_stat_2 == "Vent"):
                    data_arme["affinités vent"].append(stat)
                    vent = False
                elif (Type_stat_2 == "Terre"):
                    data_arme["affinités terre"].append(stat)
                    terre = False
            else:
                if (Type_stat_2 == "Feu"):
                    data_arme["affinité feu"].append(Valeur_stat_2)
                    feu = False
                elif (Type_stat_2 == "Eau"):
                    data_arme["affinités eau"].append(Valeur_stat_2)
                    eau = False
                elif (Type_stat_2 == "Vent"):
                    data_arme["affinités vent"].append(Valeur_stat_2)
                    vent = False
                elif (Type_stat_2 == "Terre"):
                    data_arme["affinités terre"].append(Valeur_stat_2)
                    terre = False
                    
                if (Type_stat_3 == "Feu"):
                    data_arme["affinité feu"].append(Valeur_stat_3)
                    feu = False
                elif (Type_stat_3 == "Eau"):
                    data_arme["affinités eau"].append(Valeur_stat_3)
                    eau = False
                elif (Type_stat_3 == "Vent"):
                    data_arme["affinités vent"].append(Valeur_stat_3)
                    vent = False
                elif (Type_stat_3 == "Terre"):
                    data_arme["affinités terre"].append(Valeur_stat_3)
                    terre = False
                else:
                    data_arme["caractéristique"].append(Valeur_stat_3)
                    autre = False
            
            #remplir les champs vide
            if terre:
                data_arme["affinités terre"].append("")
            if eau:
                data_arme["affinités eau"].append("")
            if feu:
                data_arme["affinité feu"].append("")
            if vent:
                data_arme["affinités vent"].append("")
            if autre:
                data_arme["caractéristique"].append("")
        
        #remplir la liste des armures   
        else:
            if (Armure == "Barrière"):
                data_armure["armure"].append("")
                data_armure["barriere"].append(Stats_principale)
            elif (Armure == "Armure"):
                data_armure["armure"].append(Stats_principale)
                data_armure["barriere"].append("")
            else:
                data_armure["armure"].append(Stats_principale)
                data_armure["barriere"].append(Stats_principale)
                
            #ajout facile a faire
            data_armure["Armure"].append(Type)
            data_armure["Rarete"].append(Couleur)
            data_armure["enchantement"].append(Bonus)
            data_armure["exaltation"].append(Exaltation)

            #drapeau des stats
            feu = True
            eau = True
            vent = True
            terre = True
            autre = True
            
            #les stats bonus
            if (Type_stat_2 == Type_stat_3):
                stat = int(Valeur_stat_2) + int(Valeur_stat_3)
                if (Type_stat_2 == "Feu"):
                    data_armure["affinité feu"].append(stat)
                    feu = False
                elif (Type_stat_2 == "Eau"):
                    data_armure["affinités eau"].append(stat)
                    eau = False
                elif (Type_stat_2 == "Vent"):
                    data_armure["affinités vent"].append(stat)
                    vent = False
                elif (Type_stat_2 == "Terre"):
                    data_armure["affinités terre"].append(stat)
                    terre = False
            else:
                if (Type_stat_2 == "Feu"):
                    data_armure["affinité feu"].append(Valeur_stat_2)
                    feu = False
                elif (Type_stat_2 == "Eau"):
                    data_armure["affinités eau"].append(Valeur_stat_2)
                    eau = False
                elif (Type_stat_2 == "Vent"):
                    data_armure["affinités vent"].append(Valeur_stat_2)
                    vent = False
                elif (Type_stat_2 == "Terre"):
                    data_armure["affinités terre"].append(Valeur_stat_2)
                    terre = False
                    
                if (Type_stat_3 == "Feu"):
                    data_armure["affinité feu"].append(Valeur_stat_3)
                    feu = False
                elif (Type_stat_3 == "Eau"):
                    data_armure["affinités eau"].append(Valeur_stat_3)
                    eau = False
                elif (Type_stat_3 == "Vent"):
                    data_armure["affinités vent"].append(Valeur_stat_3)
                    vent = False
                elif (Type_stat_3 == "Terre"):
                    data_armure["affinités terre"].append(Valeur_stat_3)
                    terre = False
                else:
                    data_armure["caractéristique"].append(f"{Valeur_stat_3} {Type_stat_3}")
                    autre = False
            
            #remplir les champs vide
            if terre:
                data_armure["affinités terre"].append("")
            if eau:
                data_armure["affinités eau"].append("")
            if feu:
                data_armure["affinité feu"].append("")
            if vent:
                data_armure["affinités vent"].append("")
            if autre:
                data_armure["caractéristique"].append("") 
        
    #transphormer en fichier
    df1 = pd.DataFrame(data_arme)
    df2 = pd.DataFrame(data_armure)
    
    # Tri des DataFrames par la première colonne (Armes ou Armure)
    df1 = df1.sort_values(by="Armes", ascending=True)
    df2 = df2.sort_values(by="Armure", ascending=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    file_path = f"cristite_{timestamp}.xlsx"
    with pd.ExcelWriter(file_path,engine="openpyxl") as writer:
        df1.to_excel(writer, sheet_name="Arme", index=False)
        df2.to_excel(writer, sheet_name="Armure", index=False)
    
    #Envoie du fichier
    await ctx.send(file=discord.File(file_path))
    
    #suppression du fichier apres quelque secondes (au cas ou sa prendr du temps a envoyer le fichier)
    time.sleep(10)
    os.remove(file_path)
        