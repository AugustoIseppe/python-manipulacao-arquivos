import os


def listar_arquivos(pasta, filtrar=""):
    todos = os.listdir(pasta)
    arquivos_filtrados = []

    for arquivo in todos:
        if not filtrar or filtrar in arquivo:
            arquivos_filtrados.append(arquivo)

    return arquivos_filtrados


def main():
    pasta_atual = os.path.dirname(__file__)

    pasta_legendas = os.path.join(
        pasta_atual, 'legendas'
    )

    arquivos = listar_arquivos(pasta_legendas, "srt")
    print(arquivos)


# essa condicional verifica se o arquivo está sendo executado diretamente ou se está sendo importado. Só será executado se for o arquivo principal
if __name__ == "__main__":
    main()
