import random

# =====================================================
# Função para gerar um ficheiro binário de teste
# =====================================================
def gerar_ficheiro_teste(nome_ficheiro, tamanho=1000):
    """
    Gera um ficheiro binário com dados sequenciais para simulação.
    """
    with open(nome_ficheiro, 'wb') as f:
        for i in range(tamanho):
            f.write(bytes([i % 256]))  # Escreve bytes de 0 a 255 ciclicamente
    print(f"Ficheiro de teste criado: {nome_ficheiro} ({tamanho} bytes)")

# =====================================================
# Função que simula o canal BSC
# =====================================================
def bsc(input_file_path, output_file_path, p):
    """
    Simula um canal binário simétrico (BSC) com probabilidade de erro p.
    Cada bit é invertido com essa probabilidade.
    """
    with open(input_file_path, 'rb') as input_file:
        input_bytes = input_file.read()

    output_bytes = bytearray()

    for byte in input_bytes:
        new_byte = 0
        for i in range(8):
            bit = (byte >> i) & 1
            if random.random() < p:
                bit ^= 1
            new_byte |= (bit << i)
        output_bytes.append(new_byte)

    with open(output_file_path, 'wb') as output_file:
        output_file.write(output_bytes)

    print(f"BSC aplicado com p = {p} -> {output_file_path}")

# =====================================================
# Função que calcula BER e SER e escreve num ficheiro .txt
# =====================================================
def calcular_ber_ser_simples(ficheiro_original, ficheiro_recebido, ficheiro_resultado="valores_ber_ser.txt"):
    """
    Compara dois ficheiros binários e guarda apenas os valores finais de BER e SER num ficheiro de texto.
    """
    with open(ficheiro_original, 'rb') as f1, open(ficheiro_recebido, 'rb') as f2:
        dados_originais = f1.read()
        dados_recebidos = f2.read()

    tamanho = min(len(dados_originais), len(dados_recebidos))
    total_bits = 0
    erros_bits = 0
    erros_simbolos = 0

    for i in range(tamanho):
        byte_orig = dados_originais[i]
        byte_recv = dados_recebidos[i]
        xor = byte_orig ^ byte_recv

        if xor != 0:
            erros_simbolos += 1

        erros_bits += bin(xor).count("1")
        total_bits += 8

    ber = erros_bits / total_bits
    ser = erros_simbolos / tamanho

    with open(ficheiro_resultado, 'w') as f:
        f.write(f"BER: {ber:.4f}\n")
        f.write(f"SER: {ser:.4f}\n")

    print(f"Valores de BER e SER guardados em '{ficheiro_resultado}'")

# =====================================================
# Função para simular BSC sem código de controlo de erros
# =====================================================
def simular_sem_codigo(ficheiro_entrada, valores_p):
    """
    Simula transmissões sobre o canal BSC para diferentes valores de p,
    sem qualquer codificação de controlo de erros.
    """
    for p in valores_p:
        ficheiro_saida = f"saida_sem_codigo_p{int(p*100)}.bin"
        bsc(ficheiro_entrada, ficheiro_saida, p)

        ficheiro_resultado = f"ber_ser_sem_codigo_p{int(p*100)}.txt"
        calcular_ber_ser_simples(ficheiro_entrada, ficheiro_saida, ficheiro_resultado)

        print(f"Simulação sem código concluída para p = {p}")

# =====================================================
# Execução principal
# =====================================================
if __name__ == "__main__":
    # Nome do ficheiro de entrada
    ficheiro_entrada = "entrada.bin"

    # Valores de probabilidade de erro a testar
    valores_p = [0.01, 0.05, 0.1, 0.2]

    # Gera o ficheiro binário de teste
    gerar_ficheiro_teste(ficheiro_entrada, tamanho=1000)

    # Executa a simulação sem códigos de correção
    simular_sem_codigo(ficheiro_entrada, valores_p)