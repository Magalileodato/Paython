import random  # Importa a biblioteca random para gerar números aleatórios

# Função que simula o canal BSC (Binary Symmetric Channel)
def bsc(bits, p):
    result = ''  # String para armazenar os bits de saída
    for bit in bits:  # Percorre cada bit da entrada
        if bit not in '01':
            continue  # Ignora qualquer caractere que não seja 0 ou 1
        # Troca o bit com probabilidade p
        if random.random() < p:
            # Se o bit for 0, troca para 1; se for 1, troca para 0
            result += '1' if bit == '0' else '0'
        else:
            result += bit  # Mantém o bit se não for trocado
    return result  # Retorna os bits modificados

# Codificação com código de repetição (3,1)
def encode_repetition(bits):
    return ''.join(bit * 3 for bit in bits)  # Cada bit é repetido 3 vezes

# Decodificação do código de repetição com correção (por maioria)
def decode_repetition(bits):
    decoded = ''
    for i in range(0, len(bits), 3):  # Processa 3 bits de cada vez
        triplet = bits[i:i+3]
        if len(triplet) < 3:
            continue  # Ignora blocos incompletos
        # Aplica decisão por maioria: se pelo menos 2 bits forem 1, decodifica como 1
        decoded += '1' if triplet.count('1') >= 2 else '0'
    return decoded

# Codificação com código de Hamming (7,4)
def encode_hamming_7_4(data):
    encoded = ''
    for i in range(0, len(data), 4):  # Processa 4 bits de cada vez
        block = data[i:i+4].ljust(4, '0')  # Preenche com zeros se faltar bits
        d = list(map(int, block))  # Converte os bits para inteiros
        # Calcula os bits de paridade
        p1 = d[0] ^ d[1] ^ d[3]
        p2 = d[0] ^ d[2] ^ d[3]
        p3 = d[1] ^ d[2] ^ d[3]
        # Organiza os bits na ordem: p1 p2 d0 p3 d1 d2 d3
        encoded += f'{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}'
    return encoded

# Decodificação do código de Hamming (7,4) com correção
def decode_hamming_7_4(bits):
    decoded = ''
    for i in range(0, len(bits), 7):  # Processa 7 bits de cada vez
        block = bits[i:i+7]
        if len(block) < 7:
            continue
        b = list(map(int, block))  # Converte os bits para inteiros
        # Calcula os bits da síndrome
        s1 = b[0] ^ b[2] ^ b[4] ^ b[6]
        s2 = b[1] ^ b[2] ^ b[5] ^ b[6]
        s3 = b[3] ^ b[4] ^ b[5] ^ b[6]
        # Calcula a posição do erro (se houver)
        error_position = s1 + (s2 << 1) + (s3 << 2)
        # Corrige o bit com erro, se necessário
        if 1 <= error_position <= 7:
            b[error_position - 1] ^= 1
        # Extrai os bits de dados corrigidos (d0 d1 d2 d3)
        decoded += f'{b[2]}{b[4]}{b[5]}{b[6]}'
    return decoded

# Função que calcula a taxa de erro de bits (BER) e taxa de erro de símbolos (SER)
def calculate_ber_ser(original, received, symbol_size=8):
    n = min(len(original), len(received))  # Usa o comprimento mais curto
    bit_errors = sum(1 for o, r in zip(original[:n], received[:n]) if o != r)  # Conta erros bit a bit
    ber = bit_errors / n  # Calcula a BER
    if symbol_size > 1:
        # Divide em símbolos (ex: 8 bits por símbolo)
        symbols = [original[i:i+symbol_size] for i in range(0, n, symbol_size)]
        received_symbols = [received[i:i+symbol_size] for i in range(0, n, symbol_size)]
        # Conta símbolos com pelo menos um erro
        symbol_errors = sum(1 for s, r in zip(symbols, received_symbols) if s != r)
        ser = symbol_errors / len(symbols)  # Calcula SER
    else:
        ser = ber
    return ber, ser

# Gera uma sequência aleatória de bits
def gerar_bits(n):
    return ''.join(random.choice('01') for _ in range(n))  # Ex: '0110101...'

# Função principal da simulação
def simular_transmissao_e_gravar_resultados():
    entrada = gerar_bits(1000)  # Gera 1000 bits aleatórios
    probabilidades = [0.01, 0.05, 0.1, 0.2]  # Lista de valores de p a testar

    # Abre um ficheiro para escrita dos resultados
    with open('resultados.txt', 'w') as f:
        f.write("Resultados da Simulação sobre o Canal BSC\n")
        f.write("========================================\n\n")

        # Executa simulação para cada valor de p
        for p in probabilidades:
            f.write(f"--- Probabilidade de erro p = {p:.2f} ---\n")

            # (i) Sem código
            recebida = bsc(entrada, p)  # Aplica canal BSC
            ber, ser = calculate_ber_ser(entrada, recebida)  # Calcula erros
            f.write(f"[Sem Código] BER = {ber:.4f}, SER = {ser:.4f}\n")

            # (ii) Repetição (3,1)
            codificada = encode_repetition(entrada)  # Codifica com repetição
            transmitida = bsc(codificada, p)  # Aplica BSC
            decodificada = decode_repetition(transmitida)  # Decodifica
            ber, ser = calculate_ber_ser(entrada, decodificada)  # Calcula erros
            f.write(f"[Repetição (3,1)] BER = {ber:.4f}, SER = {ser:.4f}\n")

            # (iii) Hamming (7,4)
            codificada = encode_hamming_7_4(entrada)  # Codifica com Hamming
            transmitida = bsc(codificada, p)  # Aplica BSC
            decodificada = decode_hamming_7_4(transmitida)  # Decodifica
            ber, ser = calculate_ber_ser(entrada, decodificada)  # Calcula erros
            f.write(f"[Hamming (7,4)] BER = {ber:.4f}, SER = {ser:.4f}\n\n")

# Executa a função principal
simular_transmissao_e_gravar_resultados()
