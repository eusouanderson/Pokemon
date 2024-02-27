import requests

url = "https://pokeapi.co/api/v2/ability/?limit=20&offset=20"

# Fazendo a solicitação GET para a API
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Convertendo a resposta para JSON
    data = response.json()
    
    # Extraindo e imprimindo os resultados
    abilities = data['results']
    print(data)
    for ability in abilities:
        print(ability['name'])
        if "mana" in ability:
            ability = "MaNA"
        
else:
    print("Erro ao fazer a solicitação:", response.status_code)
