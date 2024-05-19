import matplotlib.pyplot as plt
from individuo import *

# Definindo o tamanho do vetor
tamanho = 100
tamanho_pop = 30
tamanho_torneio = int(tamanho_pop / 3)
taxa_generation_gap = 0.7  # Generation Gap de 70%

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

clausulas = ler_cnf("arquivo.cnf")
Individuo.gerar_populacao_inicial(tamanho_pop, tamanho)

conta = 0
medias = []
best = []
for parada in range(5000):
    conta += 1
    media = 0
    for i in Individuo.populacao:
        media += Individuo.testa(i, clausulas)
    medias.append(media / tamanho_pop)
    taxa_mutacao = 0.015
    best.append(Individuo.maxfit)
    
    # Nova geração com Generation Gap
    nova_geracao = []
    nova_geracao.extend(Individuo.populacao[:int(tamanho_pop * taxa_generation_gap)])  # Adicionando parte dos melhores indivíduos
    
    # Gerando novos indivíduos aleatórios para preencher o restante da população
    while len(nova_geracao) < tamanho_pop:
        novo_individuo = Individuo()  # Crie a função __init__ no arquivo individuo.py para inicializar um novo indivíduo
        novo_individuo.gerar_individuo(tamanho)  # Método para gerar um novo indivíduo aleatório
        nova_geracao.append(novo_individuo)
    
    Individuo.populacao = nova_geracao  # Atualize a população com a nova geração
    
    # Executando o torneio e a mutação na nova população
    Individuo.nova_populacao(Individuo.populacao, taxa_mutacao, tamanho_torneio)

plt.plot(medias, label='Média')
plt.plot(best, label='Melhor Valor')
plt.xlabel('Iteração')
plt.ylabel('Valor')
plt.title('Evolução da média e do melhor valor ao longo das iterações')
plt.legend()
plt.show()
