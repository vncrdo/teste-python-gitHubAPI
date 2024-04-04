import requests

def criar_repositorio(token, nome_repositorio):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "name": nome_repositorio,
        "auto_init": True,  # Opcional: Inicializa o repositório com um README.md
        "private": False   # Opcional: Define o repositório como público
    }

    resposta = requests.post(url, json=payload, headers=headers)

    if resposta.status_code == 201:
        print(f"Repositório '{nome_repositorio}' criado com sucesso!")
        return resposta.json()
    else:
        print(f"Falha ao criar o repositório. Status: {resposta.status_code}")
        return None

# Token de acesso pessoal do GitHub
token = "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"

# Nome do repositório que deseja criar
nome_repositorio = "teste-python-gitHubAPI"

# Chamada da função para criar o repositório
criar_repositorio(token, nome_repositorio)