import csv

COUT_MAX = 500
DATA = "data/dataset2_Python+P7.csv"

with open(DATA) as fichier:
    reader = csv.DictReader(fichier, delimiter=",")
    data = []
    for ligne in reader:
        data.append(ligne)

meilleur_investissement = {"Actions": [], "Coût": 0, "Gain": 0,
                           "Profit (en %)": 0}
liste_actions = []
total_cout = 0
total_gain = 0
for action in data:
    if float(action["price"]) <=0:
        """exclusion des actions ayant des valeurs suspectes (non valables)"""
        gain = 0
    else:
        gain = float(action["price"]) * float(action["profit"]) / 100
    action["gain"] = gain

data = sorted(data, key=lambda action: float(action["profit"]), reverse=True)
for action in data:
    if action["gain"] != 0:
        if float(action["price"]) + total_cout <= COUT_MAX:
            liste_actions.append(action["name"])
            total_cout += float(action["price"])
            total_gain += action["gain"]

meilleur_investissement["Actions"] = liste_actions
meilleur_investissement["Coût"] = round(total_cout, 2)
meilleur_investissement["Gain"] = round(total_gain, 2)
profit_portefeuille = total_gain / total_cout * 100
meilleur_investissement["Profit (en %)"] = round(profit_portefeuille, 2)

print(meilleur_investissement)
