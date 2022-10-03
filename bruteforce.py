import csv
from itertools import combinations

COUT_MAX = 500
DATA = "data/data_brute.csv"

with open(DATA) as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    data = []
    for ligne in reader:
        data.append(ligne)

meilleur_investissement = {"Actions": [], "Coût": 0, "Profit": 0,
                           "Bénéfice (en %)": 0}
nombre_actions = list(range(len(data)))
for i in nombre_actions:
    possibilites = combinations(data, i+1)
    """possibilités = toutes les combinaisons possibles d'actions : 
    c'est-à-dire tous les portefeuilles allant d'une seule action au 
    portefeuille composé de toutes les actions"""
    for portefeuille in possibilites:
        total_cout = 0
        total_profit = 0
        liste_actions = []
        for action in portefeuille:
            total_cout += float(action["price"])
            profit = float(action["price"]) * float(action["benefice"]) / 100
            total_profit += profit
            liste_actions.append(action["name"])
        if total_cout <= COUT_MAX:
            benefice_portefeuille = total_profit / total_cout * 100
            if total_profit > meilleur_investissement["Profit"]:
                meilleur_investissement["Actions"] = liste_actions
                meilleur_investissement["Coût"] = round(total_cout)
                meilleur_investissement["Profit"] = round(total_profit, 2)
                meilleur_investissement["Bénéfice (en %)"] = \
                    round(benefice_portefeuille, 2)

print(meilleur_investissement)
