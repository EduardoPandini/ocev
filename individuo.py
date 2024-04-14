import random
import sys
class Individuo:
    populacao = []
    maxfit =0
    def __init__(self, fitness, genes):
        self.fitness = fitness
        self.genes = genes
        # self.populacao.append(self)
    
    def __str__(self):
        return f"{self.fitness}, {self.genes}"


    def gerar_populacao_inicial(tamanho_populacao, tamanho_genes):
        for _ in range(tamanho_populacao):
            genes = [random.randint(0, 1) for _ in range(tamanho_genes)]
            individuo = Individuo(0, genes)
            Individuo.populacao.append(individuo)
    
    def testa(self, clausulas):
        fit = 0
        for clausula in clausulas:
            nova_clausula = []
            for valor in clausula:
                novo_valor = self.genes[abs(valor) - 1] if valor > 0 else 1 - self.genes[abs(valor) - 1]
                nova_clausula.append(novo_valor)
            if nova_clausula[0] or nova_clausula[1] or nova_clausula[2]:
                fit +=1
        self.fitness = fit
        print(fit)
        if fit ==430:
            print("430 caralhooooooo")
            print(self.genes)
            print(clausulas)
            sys.exit()
        if fit > Individuo.maxfit:
            Individuo.maxfit = fit
            # print(Individuo.maxfit)
        return fit

    def crossover(self, outro_individuo):
        ponto_corte = random.randint(0, len(self.genes) - 1)
        novo_genes = self.genes[:ponto_corte] + outro_individuo.genes[ponto_corte:]
        return Individuo(0, novo_genes)
    
    def mutação(self, taxa_mutação):
        for i in range(len(self.genes)):
            if random.random() < taxa_mutação:
                self.genes[i] = 1 - self.genes[i]

    def seleção_torneio(populacao, tamanho_torneio):
        torneio = random.sample(populacao, tamanho_torneio)
        return max(torneio, key=lambda x: x.fitness)
    
    def nova_populacao(populacao, taxa_mutação, tamanho_torneio):
        nova_populacao = []
        while len(nova_populacao) < len(populacao):
            pai1 = Individuo.seleção_torneio(populacao, tamanho_torneio)
            pai2 = Individuo.seleção_torneio(populacao, tamanho_torneio)
            filho = pai1.crossover(pai2)
            filho.mutação(taxa_mutação)
            nova_populacao.append(filho)
        Individuo.populacao = nova_populacao 