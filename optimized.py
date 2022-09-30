import csv

COUT_MAX = 500
DATA = "data/data_brute.csv"

with open(DATA) as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    data = []
    for ligne in reader:
        data.append(ligne)
