class Individuo:
    população = []

    def __init__(self, fitness, genes):
        self.fitness = fitness
        self.genes = genes
        self.população.append(self)

    @staticmethod
    def gerar_clausulas(genes, clausulas):
        nova_lista_clausulas = []
        for clausula in clausulas:
            nova_clausula = []
            for valor in clausula:
                novo_valor = genes[abs(valor) - 1] if valor > 0 else 1 - genes[abs(valor) - 1]
                nova_clausula.append(novo_valor)
            nova_lista_clausulas.append(nova_clausula)
        return nova_lista_clausulas
# Exemplo de uso:
clausulas_originais = [[-2, 2, 2], [4, -2, 6]]
genes_do_individuo = [1, 0, 1, 1, 0, 1]  # Exemplo de genes

novas_clausulas = Individuo.gerar_clausulas(genes_do_individuo, clausulas_originais)
print(novas_clausulas)
