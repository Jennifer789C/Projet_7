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

data = sorted(data, key=lambda action: float(action["profit"]), reverse=True)
for action in data:
    if float(action["price"]) > 0:
        """exclusion des actions ayant des valeurs suspectes (non fiables)"""
        if float(action["price"]) + total_cout <= COUT_MAX:
            liste_actions.append(action["name"])
            total_cout += float(action["price"])
            gain = float(action["price"]) * float(action["profit"]) / 100
            total_gain += gain
            index = data.index(action) + 1
            action1 = data[index]
            while float(action1["price"]) <= 0:
                index = index + 1
                action1 = data[index]
            if total_cout + float(action1["price"]) >= COUT_MAX:
                break

cout_restant = COUT_MAX - total_cout
data_restante = []
for action in data:
    if action["name"] in liste_actions:
        continue
    if 0 < float(action["price"]) <= cout_restant:
        """exclusion des actions ayant des valeurs suspectes (non fiables)"""
        gain = float(action["price"]) * float(action["profit"]) / 100
        action["gain"] = gain
        data_restante.append(action)

data_restante = sorted(data_restante, key=lambda action: action["gain"],
                       reverse=True)
for action in data_restante:
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
