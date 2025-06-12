# Função para gerar os N primeiros números da sequência de Fibonacci
def gerar_fibonacci(n):
    # Lista para armazenar os números da sequência
    fibonacci = []
    a, b = 0, 1  # Dois primeiros termos
    for _ in range(n):
        fibonacci.append(a)  # Adiciona o termo atual à lista
        a, b = b, a + b  # Atualiza os dois últimos termos
    return fibonacci

# Simula a transmissão do Arduino para o PC (sem detecção de erros)
def transmitir_sem_erro(n):
    sequencia = gerar_fibonacci(n)  # Gera a sequência de Fibonacci
    print("Recebido no PC (sem CRC):")
    for numero in sequencia:
        print(numero)  # Imprime cada número como se fosse recebido
    return sequencia

# Exemplo de execução
transmitir_sem_erro(10)
