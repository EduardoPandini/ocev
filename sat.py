import random

# Definindo o tamanho do vetor
tamanho = 101

# Gerando o vetor com valores aleatórios de 0 ou 1
vetor = [random.randint(0, 1) for _ in range(tamanho)]
print(vetor[31])
print(vetor[5])
print(vetor[61])

def ler_cnf(nome_arquivo):
    clausulas = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            clausula_atual = []
            for linha_numero, linha in enumerate(arquivo, start=1):
                if linha.startswith('c') or linha.startswith('p') or linha.startswith('%'):
                    continue  # Ignora linhas de comentário e linha de cabeçalho
                numeros = [int(x) for x in linha.split()]
                for num in numeros:
                    if num != 0:
                        clausula_atual.append(num)
                    else:
                        if clausula_atual:
                            clausulas.append(clausula_atual)
                            clausula_atual = []
            # Adiciona a última cláusula se não houver zero no final do arquivo
            if clausula_atual:
                clausulas.append(clausula_atual)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except ValueError:
        print(f"Erro na linha {linha_numero}: '{linha.strip()}' contém um valor inválido.")
    return clausulas

nome_arquivo = 'arquivo.cnf'
clausulas = ler_cnf(nome_arquivo)

for i, clausula in enumerate(clausulas):
    for x in range(3):
        print(clausula[x], vetor[clausula[x]])

        if clausula[x] < 0 and vetor[-clausula[x]] == 1:
            print("atomo é ", clausula[x])
            clausula[x] = 0
        elif clausula[x] < 0 and vetor[-clausula[x]] == 0:
            print("atomo é ", clausula[x])
            clausula[x] = 1
        else:
            clausula[x] = vetor[clausula[x]]


count_certas = 0
print("Cláusulas do arquivo CNF:")
for i, clausula in enumerate(clausulas):
    print(f"Cláusula {i+1}: {clausula}")
    if clausula[0] or clausula[1] or clausula[2]:
        print("oh wow sugoi neeeeeee")
        count_certas = count_certas+1
    else:
        print("nooooo")

print(count_certas)



