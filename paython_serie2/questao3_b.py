# Primeiro: define a função gerar_fibonacci()
def gerar_fibonacci(n):
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

# Agora sim: funções que dependem dela
def calcular_crc8(data_bytes, polinomio=0x07):
    crc = 0
    for byte in data_bytes:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ polinomio
            else:
                crc <<= 1
            crc &= 0xFF
    return crc

def transmitir_com_crc(n):
    sequencia = gerar_fibonacci(n)
    dados = bytearray()
    for numero in sequencia:
        dados += numero.to_bytes(4, 'big')
    crc = calcular_crc8(dados)
    pacote = dados + bytes([crc])
    print("\nPacote transmitido com CRC:")
    print(pacote)
    return pacote

def verificar_recebimento(pacote):
    dados = pacote[:-1]
    crc_recebido = pacote[-1]
    crc_calculado = calcular_crc8(dados)
    print("\nVerificando CRC...")
    if crc_calculado == crc_recebido:
        print("CRC correto. Nenhum erro detectado.")
    else:
        print("Erro detectado! CRC inválido.")

def introduzir_erro(pacote, posicao, tipo='isolado'):
    pacote = bytearray(pacote)
    if tipo == 'isolado':
        pacote[posicao] ^= 0x01
    elif tipo == 'rajada':
        for i in range(3):
            if posicao + i < len(pacote):
                pacote[posicao + i] ^= 0xFF
    return bytes(pacote)

# Execução do código (parte experimental)
original = transmitir_com_crc(10)
verificar_recebimento(original)

erro_isolado = introduzir_erro(original, 5, tipo='isolado')
print("\nPacote com erro isolado:")
verificar_recebimento(erro_isolado)

erro_rajada = introduzir_erro(original, 3, tipo='rajada')
print("\nPacote com erro em rajada:")
verificar_recebimento(erro_rajada)
