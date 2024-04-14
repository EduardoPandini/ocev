import random
from individuo import *
# Definindo o tamanho do vetor
tamanho = 101
tamanho_pop = 10
tamanho_torneio = 2


def testa_individuo(individuo): #testa cada individuo
    clausulas = ler_cnf('arquivo.cnf')
    for clausula in list(clausulas):
        for x in range(3):
            if clausula[x] < 0 and individuo[-clausula[x]] == 1:
                clausula[x] = 0
            elif clausula[x] < 0 and individuo[-clausula[x]] == 0:
                clausula[x] = 1
            else:
                clausula[x] = individuo[clausula[x]]
    count_certas = 0
    for i, clausula in enumerate(clausulas):
        if clausula[0] or clausula[1] or clausula[2]:
            count_certas = count_certas+1
    # print(clausulas)
    print(count_certas,"corretas")
    
    return(count_certas)

def roda_geracao(): #passa os individuos pra testar
    individuos_testados = []
    for individuo in Individuo.individuos:
        clausulas = ler_cnf('arquivo.cnf')
        certas = Individuo.testa_individuo(individuo, clausulas)

    return(individuos_testados)

def roleta(populacao):
    fit_tot = 0
    popsaida = []
    for individuo in populacao:
        fit_tot += individuo[0]
        print(fit_tot)
    for individuo in list(populacao):
        individuo = (individuo[0]/fit_tot, individuo[1])
        popsaida.append(individuo)
    print(popsaida)

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

Individuo.gera_inicial(tamanho_pop, tamanho)
clausulas = ler_cnf('arquivo.cnf')
roda_geracao()
# roleta(saida)

# print(saida)






