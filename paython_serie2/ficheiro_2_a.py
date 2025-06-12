import random

# === BLOCO: Codificação de Fonte ===
# Converte um texto (string) em uma sequência de bits (string de '0' e '1')
def codificar_fonte(texto):
    return ''.join(f'{ord(c):08b}' for c in texto)  # Cada char vira 8 bits

# === BLOCO: Decodificação de Fonte ===
# Converte bits de volta em texto, de 8 em 8 bits
def decodificar_fonte(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(b, 2)) for b in chars if len(b) == 8)

# === BLOCO: Cifra (XOR simples com chave) ===
def cifrar(bits, chave='10101010'):
    chave_bits = (chave * ((len(bits) // len(chave)) + 1))[:len(bits)]
    return ''.join('1' if b != k else '0' for b, k in zip(bits, chave_bits))

# === BLOCO: Decifra (mesma operação XOR) ===
def decifrar(bits, chave='10101010'):
    return cifrar(bits, chave)  # XOR reversível

# === BLOCO: Codificação de Canal (Repetição 3,1) ===
def codificar_canal(bits):
    return ''.join(bit * 3 for bit in bits)

# === BLOCO: Decodificação de Canal (Repetição 3,1 com correção) ===
def decodificar_canal(bits):
    decodificado = ''
    for i in range(0, len(bits), 3):
        triplet = bits[i:i+3]
        if len(triplet) < 3:
            continue
        decodificado += '1' if triplet.count('1') >= 2 else '0'
    return decodificado

# === BLOCO: Canal BSC ===
def bsc(bits, p):
    resultado = ''
    for bit in bits:
        if bit not in '01':
            continue
        if random.random() < p:
            resultado += '0' if bit == '1' else '1'
        else:
            resultado += bit
    return resultado

# === BLOCO PRINCIPAL: pipeline do diagrama ===
def transmitir_arquivo(ficheiro_entrada, ficheiro_saida, p):
    # 1. Lê o conteúdo do ficheiro A (entrada)
    with open(ficheiro_entrada, 'r', encoding='utf-8') as f:
        texto_original = f.read()

    # 2. Codificação de fonte
    bits_fonte = codificar_fonte(texto_original)

    # 3. Cifra
    bits_cifrados = cifrar(bits_fonte)

    # 4. Codificação de canal (repetição 3,1)
    bits_codificados = codificar_canal(bits_cifrados)

    # 5. Transmissão pelo BSC
    bits_recebidos = bsc(bits_codificados, p)

    # 6. Decodificação de canal
    bits_corrigidos = decodificar_canal(bits_recebidos)

    # 7. Decifra
    bits_decifrados = decifrar(bits_corrigidos)

    # 8. Decodificação de fonte
    texto_recebido = decodificar_fonte(bits_decifrados)

    # 9. Escreve o conteúdo no ficheiro de saída
    with open(ficheiro_saida, 'w', encoding='utf-8') as f:
        f.write(texto_recebido)

    # 10. Estatísticas de BER e SER
    n = min(len(bits_fonte), len(bits_decifrados))
    ber = sum(1 for a, b in zip(bits_fonte[:n], bits_decifrados[:n]) if a != b) / n
    symbols = [bits_fonte[i:i+8] for i in range(0, n, 8)]
    received_symbols = [bits_decifrados[i:i+8] for i in range(0, n, 8)]
    ser = sum(1 for a, b in zip(symbols, received_symbols) if a != b) / len(symbols)

    print(f"[Canal BSC p={p}] BER: {ber:.4f}, SER: {ser:.4f}")
    print(f"Bits de informação transmitidos: {len(bits_fonte)}")
    print(f"Bits totais transmitidos: {len(bits_codificados)}")
    print(f"Ficheiro de entrada: {ficheiro_entrada}")
    print(f"Ficheiro de saída: {ficheiro_saida}")
