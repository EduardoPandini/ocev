def normalizar_vetor(vetor):
    # Encontre os valores máximo e mínimo
    valor_max = max(vetor)
    valor_min = min(vetor)
    
    # Calcule o intervalo
    intervalo = valor_max - valor_min
    
    # Normalize o vetor
    vetor_normalizado = [(x - valor_min) / intervalo for x in vetor]
    
    return vetor_normalizado

# Exemplo de uso
vetor = [1, 2, 3, 4, 5]
vetor_normalizado = normalizar_vetor(vetor)
print(vetor_normalizado)
