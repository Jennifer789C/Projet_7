import csv

COUT_MAX = 500
DATA = "data/data_brute.csv"

with open(DATA) as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    data = []
    for ligne in reader:
        data.append(ligne)

meilleur_investissement = {"Actions": [], "Coût": 0, "Profit": 0,
                           "Bénéfice (en %)": 0}
liste_actions = []
total_cout = 0
total_profit = 0
data = sorted(data, key=lambda action: float(action["benefice"]), reverse=True)
for action in data:
    if float(action["price"]) + total_cout <= COUT_MAX:
        liste_actions.append(action["name"])
        total_cout += float(action["price"])
        profit = float(action["price"]) * float(action["benefice"]) / 100
        total_profit += profit

meilleur_investissement["Actions"] = liste_actions
meilleur_investissement["Coût"] = round(total_cout, 2)
meilleur_investissement["Profit"] = round(total_profit, 2)
benefice_portefeuille = total_profit / total_cout * 100
meilleur_investissement["Bénéfice (en %)"] = round(benefice_portefeuille, 2)

print(meilleur_investissement)
