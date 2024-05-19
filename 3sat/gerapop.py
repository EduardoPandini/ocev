import numpy as np


# Definindo o tamanho da população e a dimensão dos indivíduos
tamanho_populacao = 10
dimensao = 15

# Gerando a população com números inteiros entre -5 e 10 de forma uniforme
populacao = np.random.uniform(-6, 11, size=(tamanho_populacao, dimensao))

# Salvando a população em um arquivo de texto

np.savetxt("populacao_inteiros.txt", populacao, fmt='%d', delimiter=',') # Alterado para delimiter=',' para separar por vírgula
