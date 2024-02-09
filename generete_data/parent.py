import csv
import json
import requests
import os

# Leitura do CSV
with open('combinationsv1-3-012.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = list(csvreader)
    
# Sua lógica para ler CSV e criar a estrutura de dados
individuals = rows[0][1:]  # Nomes dos indivíduos
treeData = {}

for row in rows[1:]:
    nome_pai = row[0].lstrip('_').replace(" ", "_").lower().replace("_", "-").replace("-special", "")
    
    for index, parent in enumerate(row[1:]):
        nome_mae = individuals[index].replace(" ", "_").lower().replace("_", "-").replace("-special", "")
        nome_filho = parent.replace(" ", "_").lower().replace("_", "-").replace("-special", "")

        if nome_filho not in treeData:
            treeData[nome_filho] = {'parents': []}

        treeData[nome_filho]['parents'].append({'nome_pai': nome_pai, 'nome_mae': nome_mae})

# Criar JSON mostrando quem pode ser pai de quem
relationshipData = {}

for nome_filho, info in treeData.items():
    for parent_info in info['parents']:
        nome_pai = parent_info['nome_pai']
        nome_mae = parent_info['nome_mae']

        if nome_pai not in relationshipData:
            relationshipData[nome_pai] = []

        relationshipData[nome_pai].append(nome_filho)

# Convertendo para JSON e salvando em um arquivo
with open('relationshipData.json', 'w') as jsonfile:
    json.dump(relationshipData, jsonfile, indent=2)
