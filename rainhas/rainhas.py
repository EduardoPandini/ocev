import os
import random
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
N = 32
pop_size = 20
generations = 5000
mutation_rate = 0.05
tournament_size = 3
gap_percentage = 0.2
num_executions = 10

# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(' '.join('Q' if x else '.' for x in row))
    print("\n")

# Função de avaliação
def fitness(board):
    conflicts = 0
    N = len(board)
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts
 
# Inicialização da população
def initialize_population(pop_size, N):
    population = []
    for _ in range(pop_size):
        individual = list(range(N))
        random.shuffle(individual)
        population.append(individual)
    return population

# Seleção por torneio
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: fitness(x))
    return selected[0]

# Cruzamento
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    child2 = parent2[:point] + [gene for gene in parent1 if gene not in parent2[:point]]
    return child1, child2

# Mutação
def mutate(board, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(board)), 2)
        board[idx1], board[idx2] = board[idx2], board[idx1]

# Algoritmo genético
def genetic_algorithm(pop_size, generations, mutation_rate, gap_percentage, N):
    population = initialize_population(pop_size, N)
    best_fit_per_gen = []
    average_fit_per_gen = []  # Lista para armazenar as médias de fitness de cada geração
    best_solution = None
    best_fitness = float('inf')
    
    for gen in range(generations):
        population.sort(key=lambda x: fitness(x))
        if fitness(population[0]) < best_fitness:
            best_solution = population[0]
            best_fitness = fitness(population[0])
        
        best_fit_per_gen.append(best_fitness)
        
        # Calcular média de fitness da geração atual
        generation_fitness = [fitness(individual) for individual in population]
        average_fitness = sum(generation_fitness) / len(generation_fitness)
        average_fit_per_gen.append(average_fitness)
        
        if best_fitness == 0:
            break
        
        gap_size = int(gap_percentage * pop_size)
        new_population = population[:gap_size]  # Manter os melhores (generational gap)
        
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population[:pop_size]
    
    return best_solution, best_fitness, best_fit_per_gen, average_fit_per_gen

# Função para converter a solução do vetor para matriz
def convert_to_matrix(solution):
    matrix = np.full((len(solution), len(solution)), '.', dtype=str)
    for i, col in enumerate(solution):
        matrix[i][col] = 'Q'
    return matrix


# Criar a pasta para os gráficos
graphs_dir = f'gráficos{N}x{N}'
os.makedirs(graphs_dir, exist_ok=True)

# Executar o algoritmo genético para o valor de N especificado
for i in range(num_executions):
    best_solution, best_fitness, best_fit_per_gen, average_fit_per_gen = genetic_algorithm(pop_size, generations, mutation_rate, gap_percentage, N)

    # Gráfico de convergência
    plt.plot(best_fit_per_gen, label='Melhor Fitness')
    plt.plot(average_fit_per_gen, label='Média Fitness')
    plt.xlabel('Gerações')
    plt.ylabel('Fitness (número de conflitos)')
    plt.title(f'Convergência do Algoritmo Genético - Execução {i + 1}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{graphs_dir}/execucao_{i + 1}.png')
    plt.close()
