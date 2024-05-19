import os
import matplotlib.pyplot as plt
from individuo import *

# Parâmetros
tamanho = 100
tamanho_pop = 30
tamanho_torneio = 10
porcento_gap = 6
taxa_mutacao = 0.012
iteracoes = 5000
num_execucoes = 10

# Função para ler o arquivo CNF
def ler_cnf(nome_arquivo): 
    clausulas = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            clausula_atual = []
            for linha_numero, linha in enumerate(arquivo, start=1):
                if linha.startswith('c') or linha.startswith('p') or linha.startswith('%'):
                    continue  
                numeros = [int(x) for x in linha.split()]
                for num in numeros:
                    if num != 0:
                        clausula_atual.append(num)
                    else:
                        if clausula_atual:
                            clausulas.append(clausula_atual)
                            clausula_atual = []
            if clausula_atual:
                clausulas.append(clausula_atual)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' nao foi encontrado.")
    except ValueError:
        print(f"Erro na linha {linha_numero}: '{linha.strip()}' contém um valor inválido.")
    return clausulas

# Execução do algoritmo 10 vezes
for instancia in range(1, num_execucoes + 1):
    # Reinicializar variáveis antes de cada execução
    Individuo.populacao = []
    Individuo.maxfit = 0

    clausulas = ler_cnf("arquivo.cnf")
    Individuo.gerar_populacao_inicial(tamanho_pop, tamanho)

    medias = []
    best = []

    for iteracao in range(iteracoes):
        media = 0
        pop_send = []

        for i in Individuo.populacao:
            media += Individuo.testa(i, clausulas)
        medias.append(media / tamanho_pop)
        
        best.append(Individuo.maxfit)

        nova_pop = Individuo.nova_populacao(Individuo.populacao, taxa_mutacao, tamanho_torneio)
        for i in range(porcento_gap):
            pop_send.append(random.choice(Individuo.populacao))
        for i in range(tamanho_pop-porcento_gap):
            pop_send.append(random.choice(nova_pop))
        Individuo.atualiza_pop(pop_send)
        if Individuo.maxfit == 430:
            break

    # Criação da pasta para os gráficos se não existir
    graphs_dir = 'gráficos'
    os.makedirs(graphs_dir, exist_ok=True)

    # Salvando o gráfico
    plt.plot(medias, label='Média')
    plt.plot(best, label='Melhor Valor')
    plt.xlabel('Iteração')
    plt.ylabel('Valor')
    plt.title('Evolução da média e do melhor valor ao longo das iterações')
    plt.legend()
    plt.savefig(f'{graphs_dir}/instancia_{instancia}.png')
    plt.close()
