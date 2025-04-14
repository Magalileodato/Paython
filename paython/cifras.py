import matplotlib.pyplot as plt
import math
from collections import Counter

# Função que cifra dados usando a cifra de Vigenère em nível de bytes
def vigenere_cipher(text, key):
    result = []
    key = key.encode()  # Converte a chave para bytes
    for i, char in enumerate(text):
        result.append((char + key[i % len(key)]) % 256)  # Operação de cifra por byte
    return bytes(result)

# Função que decifra dados cifrados com a cifra de Vigenère
def vigenere_decipher(ciphered, key):
    result = []
    key = key.encode()
    for i, char in enumerate(ciphered):
        result.append((char - key[i % len(key)]) % 256)  # Operação inversa da cifra
    return bytes(result)

# Função que cifra um arquivo de entrada e salva o resultado em outro arquivo
def cifra_arquivo(caminho_entrada, caminho_saida, chave):
    with open(caminho_entrada, 'rb') as f:
        conteudo = f.read()
    cifrado = vigenere_cipher(conteudo, chave)
    with open(caminho_saida, 'wb') as f:
        f.write(cifrado)

# Função que decifra um arquivo cifrado e salva o resultado em outro arquivo
def decifra_arquivo(caminho_cifrado, caminho_saida, chave):
    with open(caminho_cifrado, 'rb') as f:
        cifrado = f.read()
    decifrado = vigenere_decipher(cifrado, chave)
    with open(caminho_saida, 'wb') as f:
        f.write(decifrado)

# Calcula a entropia de Shannon de um conjunto de dados
def calcula_entropia(dados):
    contador = Counter(dados)        # Conta a frequência de cada byte
    total = len(dados)               # Número total de bytes
    entropia = 0
    for freq in contador.values():
        p = freq / total             # Probabilidade do byte
        entropia -= p * math.log2(p) # Soma a entropia
    return entropia

# Gera um histograma com a distribuição de bytes do arquivo
def gera_histograma(dados, titulo):
    contador = Counter(dados)
    plt.figure(figsize=(10, 4))
    plt.bar(contador.keys(), contador.values(), color='blue')
    plt.title(titulo)
    plt.xlabel('Byte (0-255)')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

# ---------------------------
# Execução do programa
# ---------------------------
if __name__ == "__main__":
    # Define a chave de cifra
    chave = "criptografia"

    # Define os caminhos dos arquivos
    arquivo_original = "ficheiro1.txt"
    arquivo_cifrado = "ficheiro_cifrado.txt"
    arquivo_decifrado = "ficheiro_decifrado.txt"

    # Etapa 1: Cifrar o arquivo original
    cifra_arquivo(arquivo_original, arquivo_cifrado, chave)

    # Etapa 2: Decifrar o arquivo cifrado
    decifra_arquivo(arquivo_cifrado, arquivo_decifrado, chave)

    # Etapa 3: Ler os dados de cada arquivo para análise
    with open(arquivo_original, 'rb') as f:
        dados_original = f.read()

    with open(arquivo_cifrado, 'rb') as f:
        dados_cifrado = f.read()

    with open(arquivo_decifrado, 'rb') as f:
        dados_decifrado = f.read()

    # Etapa 4: Mostrar entropias
    print("Entropia do arquivo original:  ", round(calcula_entropia(dados_original), 4))
    print("Entropia do arquivo cifrado:   ", round(calcula_entropia(dados_cifrado), 4))
    print("Entropia do arquivo decifrado: ", round(calcula_entropia(dados_decifrado), 4))

    # Etapa 5: Gerar histogramas
    gera_histograma(dados_original, "Histograma - Arquivo Original")
    gera_histograma(dados_cifrado, "Histograma - Arquivo Cifrado")
    gera_histograma(dados_decifrado, "Histograma - Arquivo Decifrado")
