# programa responsável por calcular o fatorial de 
# acordo com as informações fornecidas do usuário

def fatorial(num):
    #Calculando o fatorial de um número
    if num == 0 or num == 1:
        return 1
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado


#Calcula o número de combinações C(n, k).
# onde os Parâmetros são:
# n (int): Número total de elementos.
# k (int): Número de elementos escolhidos. E retorna:
#int: Número de combinações possíveis.
def combinacao(n, k):

    if k > n or n < 0 or k < 0:
        return "Valores inválidos! Certifique-se de que 0 ≤ k ≤ n." # definindo um intervalo consistente
    
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

# Entrada do usuário para calcular as combinações

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

# Calculando e exibindo o resultado
resultado = combinacao(n, k)
print(f"C({n}, {k}) = {resultado}")
