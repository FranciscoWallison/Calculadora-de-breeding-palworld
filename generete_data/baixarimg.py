import csv
import json
import requests
import os

# Criar o diretório para salvar as imagens
os.makedirs('imagens', exist_ok=True)

# Caminho para o arquivo JSON
caminho_arquivo = 'treeData.json'

with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

    for nome_chave in dados.keys():
        nome_formatado = nome_chave.replace(" ", "_").lower().replace("_", "-").replace("-special", "")
        # Construir a URL da imagem
        url = f'https://palwiki.io/assets/img/pals/{nome_formatado}.png'

        # Fazer o download da imagem
        response = requests.get(url)
        
        # Salvar a imagem no diretório
        with open(f'imagens/{nome_formatado}.png', 'wb') as img_file:
            img_file.write(response.content)

        print(f' Downloads concluídos: {nome_formatado}' )

