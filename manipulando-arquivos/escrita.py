import os

# __file__ -> variável que retorna o caminho do arquivo atual
# Pegando o caminho do arquivo atual
pasta_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    pasta_atual, 'textos', 'texto-01.txt'
)

# Lendo o arquivo inteiro
# O 'w' é para escrever no arquivo

# o 'a' é para adicionar no arquivo sem apagar o conteúdo anterior
# with open(caminho_arquivo, 'a') as arquivo:
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write("Python é uma linguagem de programação\n")

linhas = [
    "Sociedade Esportiva Palmeiras",
    "Sport Club Corinthians Paulista",
    "Santos Futebol Clube",
    "São Paulo Futebol Clube",
    "Clube de Regatas Flamengo",
    "Fluminense Football Club",
    "Botafogo de Futebol e Regatas",
    "Club de Regatas Vasco da Gama",
    "Grêmio Foot-Ball Porto Alegrense",
    "Sport Club Internacional",
    "Cruzeiro Esporte Clube",
    "Clube Atlético Mineiro",
]

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.writelines("\n" + linha for linha in linhas)
