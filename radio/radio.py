import os
import random
import matplotlib.pyplot as plt

# Parâmetros
pop_size = 20
generations = 100
mutacao = 0.1

# Função para decodificar cromossomo binário para valores inteiros
def decode(chromosome):
    ST_bin = chromosome[:5]
    LX_bin = chromosome[5:]
    ST = int(ST_bin, 2)
    LX = int(LX_bin, 2)
    return ST, LX

# Função de avaliação
def fitness(chromosome):
    ST, LX = decode(chromosome)
    if ST > 24 or LX > 16:
        return -float('inf'), 0, ST, LX, 1  # Penalização máxima
    FO = 30 * ST + 40 * LX
    H = max(0, (ST + 2 * LX - 40) / 16)
    FOn = FO / 1360
    Hn = H
    r = -1
    fit = FOn + r * Hn
    return fit, FO, ST, LX, H

# Inicialização da população
def initialize_population(pop_size):
    return [''.join(random.choice('01') for _ in range(10)) for _ in range(pop_size)]

# Seleção por torneio
def tournament_selection(population, fitnesses, k=3):
    selected = random.sample(range(len(population)), k)
    selected_fitnesses = [(fitnesses[i], i) for i in selected]
    selected_fitnesses.sort(reverse=True)
    return population[selected_fitnesses[0][1]]

# Cruzamento de um ponto
def crossover(parent1, parent2):
    point = random.randint(1, 9)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutação
def mutate(chromosome, mutation_rate=mutacao):
    new_chromosome = ''.join(
        (bit if random.random() > mutation_rate else str(1 - int(bit)))
        for bit in chromosome
    )
    return new_chromosome

# Algoritmo genético
def genetic_algorithm(pop_size, generations, instance):
    population = initialize_population(pop_size)
    best_fit_per_gen = []
    
    for gen in range(generations):
        fitnesses = [fitness(indiv) for indiv in population]
        population = sorted(population, key=lambda x: fitness(x)[0], reverse=True)
        best_fit_per_gen.append(fitnesses[0][1])
        
        new_population = population[:2]  # Elitismo: mantém os 2 melhores
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:pop_size]
    
    # Avaliação final
    final_fitnesses = [fitness(indiv) for indiv in population]
    best_individual = sorted(population, key=lambda x: fitness(x)[0], reverse=True)[0]
    best_fit = fitness(best_individual)
    
    # Gráfico de convergência
    plt.plot(range(generations), best_fit_per_gen)
    plt.xlabel('Gerações')
    plt.ylabel('Valor da Função Objetivo')
    plt.title('Convergência do Algoritmo Genético')
    plt.grid(True)
    graphs_dir = 'gráficos'
    os.makedirs(graphs_dir, exist_ok=True)  # Cria a pasta "gráficos" se não existir
    plt.savefig(f'{graphs_dir}/instancia_{instance}.png')
    plt.close()  # Fechar o gráfico e liberar memória
    
    return best_individual, best_fit, best_fit_per_gen

# Executar o algoritmo genético 10 vezes
results = []
for i in range(10):
    best_individual, best_fit, best_fit_per_gen = genetic_algorithm(pop_size, generations, i+1)
    results.append(best_fit)
    print(f"Execução {i+1}:")
    print(f"  Binário do melhor indivíduo: {best_individual}")
    print(f"  Valores finais obtidos para as variáveis do problema: ST = {best_fit[2]}, LX = {best_fit[3]}")
    print(f"  Valor final da função objetivo: {best_fit[1]}")
    print(f"  Infringiu alguma restrição: {'Sim' if best_fit[4] > 0 else 'Não'}")

# Exibir todos os valores de fitness ao final das 10 execuções
for i, fit in enumerate(results):
    print(f"Execução {i+1}: Valor da Função Objetivo = {fit[1]}")
