import os

# __file__ -> variável que retorna o caminho do arquivo atual
# Pegando o caminho do arquivo atual
pasta_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    pasta_atual, 'legendas', 'legendas_03.srt'
)

# Lendo o arquivo inteiro
# O 'r' é para ler o arquivo
with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo o arquivo linha a linha
with open(caminho_arquivo, 'r') as arquivo:
    linha = arquivo.readline()
    while linha:
        partes = linha.split()
        inicio = partes[0] if partes else ''

        print(inicio, end=', ')
        linha = arquivo.readline()

# Lendo o arquivo linha a linha
with open(caminho_arquivo, 'r') as arquivo:
    for linha in arquivo:
        print(linha[:5], end='*')
