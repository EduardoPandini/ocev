import random

# Definindo o tamanho do vetor
tamanho = 101
tam_pop = 10
pop = []
tamanho_torneio = 2
def pop_inicial():
    for i in range(tam_pop):
        pop.append([random.randint(0, 1) for _ in range(tamanho)])


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
    # print(count_certas,"corretas")
    
    return(count_certas)

def roda_geracao(): #passa os individuos pra testar
    individuos_testados = []
    for individuo in pop:
        certas = testa_individuo(individuo)
        individuo_testado = (certas, individuo)
        individuos_testados.append(individuo_testado)
    return(individuos_testados)

def achaMax(pop_testada):
    max = 0
    for pop in pop_testada:
        if pop[0] > max:
            max = pop[0]
    return(max)


def achaMin(pop_testada):
    min = 1
    for pop in pop_testada:
        if pop[0] < min:
            min = pop[0]
    return(min)


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

def seleciona(pop_testada):
    selecionados = []
    maximo = achaMax(pop_testada)
    minimo = achaMin(pop_testada)
    intervalo = maximo - minimo
    for i, indivíduo in enumerate(pop_testada):
        aptidao_normalizada = (indivíduo[0] - minimo) / intervalo
        pop_testada[i] = (aptidao_normalizada, indivíduo[1])  # Atualiza com a aptidao normalizada
    while len(selecionados) < tam_pop:
        torneio = random.sample(pop_testada, tamanho_torneio)
        vencedor = max(torneio, key=lambda x: x[0])  # Seleciona o vencedor do torneio baseado no fitness (primeiro valor)
        selecionados.append(vencedor[1])
        # print(vencedor)
    return(selecionados)



    
    
    
    


pop_inicial()
clausulas = ler_cnf('arquivo.cnf')
saida = roda_geracao()
seleciona(saida)






