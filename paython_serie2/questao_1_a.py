import random  # Biblioteca usada para gerar números aleatórios

def gerar_ficheiro_teste(nome_ficheiro, tamanho=100):
    """
    Gera um ficheiro binário com conteúdo sequencial para testes.
    
    Parâmetros:
        nome_ficheiro (str): Nome do ficheiro a criar.
        tamanho (int): Número de bytes a escrever.
    """
    with open(nome_ficheiro, 'wb') as f:  # Abre o ficheiro em modo escrita binária
        for i in range(tamanho):  # Para cada valor até ao tamanho
            f.write(bytes([i % 256]))  # Escreve o byte (0 a 255 em ciclo)
    print(f"Ficheiro de teste criado: {nome_ficheiro} ({tamanho} bytes)")

def bsc(input_file_path, output_file_path, p):
    """
    Simula um canal binário simétrico (BSC).
    Cada bit é invertido com probabilidade p.

    Parâmetros:
        input_file_path (str): Caminho para o ficheiro original.
        output_file_path (str): Caminho para o ficheiro modificado.
        p (float): Probabilidade de erro por bit.
    """
    # Lê o ficheiro original em modo binário
    with open(input_file_path, 'rb') as input_file:
        input_bytes = input_file.read()  # Guarda todos os bytes do ficheiro

    output_bytes = bytearray()  # Inicializa array para guardar o resultado

    # Processa cada byte lido
    for byte in input_bytes:
        new_byte = 0  # Variável para construir o novo byte
        for i in range(8):  # Itera por cada um dos 8 bits do byte
            bit = (byte >> i) & 1  # Extrai o bit i do byte
            if random.random() < p:  # Com probabilidade p...
                bit ^= 1  # ... inverte o bit (0 -> 1 ou 1 -> 0)
            new_byte |= (bit << i)  # Adiciona o bit na posição correta
        output_bytes.append(new_byte)  # Adiciona o byte ao array final

    # Escreve os novos bytes num ficheiro de saída
    with open(output_file_path, 'wb') as output_file:
        output_file.write(output_bytes)

    print(f"Transmissão BSC concluída (p = {p}) -> {output_file_path}")

# =========================
# Execução do exemplo
# =========================

# Nome do ficheiro de entrada
ficheiro_entrada = "entrada.bin"

# Nome do ficheiro de saída com ruído
ficheiro_saida = "saida.bin"

# Probabilidade de erro por bit
probabilidade_erro = 0.1  # 10%

# Gera o ficheiro de teste com 1000 bytes
gerar_ficheiro_teste(ficheiro_entrada, tamanho=1000)

# Aplica o canal BSC ao ficheiro criado
bsc(ficheiro_entrada, ficheiro_saida, probabilidade_erro)
