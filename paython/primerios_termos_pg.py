# Método responsável por forneceer o progração geométrica de
# acordo com as informações fornecidas

# Informações estruturais do programa
# Exibe os primeiros N termos de uma progressão geométrica.
# Parâmetros: N (int): Número de termos a serem exibidos.
#             u (float): Primeiro termo da progressão.
#             r (float): Razão da progressão. E retorna: None

def progressao_geometrica(N, u, r): 

    if N <= 0:
        print("O número de termos deve ser maior que zero.")# verificação se o termo é maior e igual zero
        return

    termo = u
    for _ in range(N): # Repete a operação N vezes
        print(termo, end=" ")
        termo *= r  # Multiplica pelo valor da razão para obter o próximo termo

# Entrada do usuário para tornar nossa aplicação mais dinamica
N = int(input("Digite o número de termos: "))
u = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão: "))

# Chamando a função com os valores fornecidos
progressao_geometrica(N, u, r)
