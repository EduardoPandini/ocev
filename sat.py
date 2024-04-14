
from individuo import *
# Definindo o tamanho do vetor
tamanho = 100
tamanho_pop = 50
tamanho_torneio = 10

def ler_cnf(nome_arquivo): #le o arquivo de entrada pra separar as clausulas
    clausulas = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            clausula_atual = []
            for linha_numero, linha in enumerate(arquivo, start=1):
                if linha.startswith('c') or linha.startswith('p') or linha.startswith('%'):
                    continue  # Ignora linhas de comentário e linha de cabecalho
                numeros = [int(x) for x in linha.split()]
                for num in numeros:
                    if num != 0:
                        clausula_atual.append(num)
                    else:
                        if clausula_atual:
                            clausulas.append(clausula_atual)
                            clausula_atual = []
            # Adiciona a última cláusula se nao houver zero no final do arquivo
            if clausula_atual:
                clausulas.append(clausula_atual)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' nao foi encontrado.")
    except ValueError:
        print(f"Erro na linha {linha_numero}: '{linha.strip()}' contém um valor inválido.")
    return clausulas


clausulas = ler_cnf("arquivo.cnf")
# print(len(clausulas))
Individuo.gerar_populacao_inicial(tamanho_pop, tamanho)


while True:
    media = 0
    for i in Individuo.populacao:

        media += Individuo.testa(i, clausulas)

    taxa_mutação = 0.015
    
    Individuo.nova_populacao(Individuo.populacao, taxa_mutação, tamanho_torneio)
    print(media/tamanho_pop)



