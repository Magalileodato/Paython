# Este programa de é responsável de fornecer os valores máximo e mínino de um vetor


# Determinando os valores mínimo e máximo de um vetor.
# Parâmetro: v (list): Lista de números. Retorna:
# tuple: Uma tupla contendo (mínimo, máximo).

def min_max(v):
    if not v:  # Verifica se a lista está vazia
        return "O vetor está vazio!"

    minimo = v[0]  # Assume que o primeiro elemento é o menor
    maximo = v[0]  # Assume que o primeiro elemento é o maior

    for num in v:
        if num < minimo:
            minimo = num  # Atualiza o menor valor
        if num > maximo:
            maximo = num  # Atualiza o maior valor

    return minimo, maximo  # Retorna os valores mínimo e máximo

# Solicita ao usuário que insira os valores do vetor
entrada = input("Digite os números do vetor separados por espaço: ")

# Converte a entrada em uma lista de inteiros
vetor = list(map(int, entrada.split()))

# Chama a função e imprime o resultado
resultado = min_max(vetor)

if isinstance(resultado, tuple):
    minimo, maximo = resultado
    print(f"Valor mínimo: {minimo}, Valor máximo: {maximo}")
else:
    print(resultado)
