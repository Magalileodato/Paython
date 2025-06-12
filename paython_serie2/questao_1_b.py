import random

def bsc(input_file, output_file, p):
    with open(input_file, 'r') as infile:
        input_data = infile.read()

    output_data = ''
    for bit in input_data:
        if bit not in '01':
            continue
        if random.random() < p:
            flipped_bit = '1' if bit == '0' else '0'
            output_data += flipped_bit
        else:
            output_data += bit

    with open(output_file, 'w') as outfile:
        outfile.write(output_data)

def calculate_ber_ser(original, received, symbol_size=1):
    # Garante que ambas as strings tenham o mesmo tamanho
    n = min(len(original), len(received))
    original = original[:n]
    received = received[:n]

    bit_errors = sum(1 for o, r in zip(original, received) if o != r)
    ber = bit_errors / n

    if symbol_size > 1:
        # Divide em blocos de "symbol_size" bits
        symbols = [original[i:i+symbol_size] for i in range(0, n, symbol_size)]
        received_symbols = [received[i:i+symbol_size] for i in range(0, n, symbol_size)]

        total_symbols = min(len(symbols), len(received_symbols))
        symbol_errors = sum(1 for s, r in zip(symbols, received_symbols) if s != r)
        ser = symbol_errors / total_symbols
    else:
        ser = ber  # símbolo = 1 bit

    return ber, ser

# 1. Criar ficheiro de teste com 1000 bits aleatórios
def gerar_ficheiro_binario(nome, tamanho):
    with open(nome, 'w') as f:
        bits = ''.join(random.choice('01') for _ in range(tamanho))
        f.write(bits)
    return bits

# -------------------------------
# EXECUÇÃO DE TESTES
# -------------------------------
input_file = 'entrada.txt'
output_file = 'saida.txt'
bitstream = gerar_ficheiro_binario(input_file, 1000)

# Testar para diferentes valores de p
for p in [0.0, 0.1, 0.3, 0.5]:
    bsc(input_file, output_file, p)

    with open(output_file, 'r') as f:
        received_bits = f.read()

    ber, ser = calculate_ber_ser(bitstream, received_bits, symbol_size=8)

    print(f'>>> p = {p:.1f}')
    print(f'BER = {ber:.4f} ({ber*100:.2f}%)')
    print(f'SER (por byte) = {ser:.4f} ({ser*100:.2f}%)\n')
