import random
import string
import math
import matplotlib.pyplot as plt
from collections import Counter

# Função para gerar sequência de símbolos com base em probabilidades
def gerar_sequencia(alfabeto, probabilidades, N):
    return random.choices(alfabeto, probabilidades, k=N)

# (i) Gerar palavras-passe robustas
def gerar_palavra_passe():
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    return ''.join(gerar_sequencia(alfabeto, [1/len(alfabeto)]*len(alfabeto), random.randint(10, 14)))

# (ii) Gerar endereço IPv4
def gerar_ip_v4():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

# (iii) Gerar endereço IPv6
def gerar_ip_v6():
    return ':'.join(f"{random.randint(0, 65535):x}" for _ in range(8))

# (iv) Gerar tuplo hexadecimal com 8 elementos
def gerar_tuplo_hex():
    return tuple(f"{random.randint(0, 255):x}" for _ in range(8))

# Gerar arquivo com sequência de símbolos
def gerar_arquivo(alfabeto, probabilidades, N, nome_arquivo):
    sequencia = gerar_sequencia(alfabeto, probabilidades, N)
    with open(nome_arquivo, 'w', encoding='utf-8') as f:  # Agora o arquivo é salvo com codificação UTF-8
        f.write(''.join(sequencia))

# Função para calcular entropia
def calcular_entropia(probabilidades):
    return -sum(p * math.log2(p) for p in probabilidades if p > 0)

# Gerar histograma de sequência no arquivo
def gerar_histograma(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:  # Lê o arquivo com codificação UTF-8
        dados = f.read()

    contagem = Counter(dados)  # Conta a frequência de cada símbolo
    simbolos = list(contagem.keys())
    frequencias = list(contagem.values())
    
    plt.bar(simbolos, frequencias)  # Plota o histograma
    plt.xlabel('Símbolos')
    plt.ylabel('Frequência')
    plt.title('Histograma de Símbolos')
    plt.xticks(rotation=90)  # Gira os rótulos do eixo X para evitar sobreposição
    plt.show()

    # Retorna as probabilidades para o cálculo de entropia
    return [v / len(dados) for v in frequencias]

# (c) Gerar arquivos com diferentes condições
alfabeto1 = ['A', 'B', 'C', 'D']
probabilidades1 = [0.25, 0.25, 0.25, 0.25]
gerar_arquivo(alfabeto1, probabilidades1, 100, "ficheiro1.txt")
gerar_arquivo(alfabeto1, probabilidades1, 1000, "ficheiro2.txt")
# Gera alfabeto com 256 símbolos visíveis (hexadecimal de 00 a ff)
alfabeto3 = [f"{i:02x}" for i in range(256)]
probabilidades3 = [1/256] * 256

# Gera a sequência de 10.000 símbolos (strings como '00', 'ff', etc.)
sequencia = gerar_sequencia(alfabeto3, probabilidades3, 10000)

# Salva no arquivo com separação por espaço para facilitar leitura
with open("ficheiro3.txt", 'w', encoding='utf-8') as f:
    f.write(' '.join(sequencia))  # Conteúdo como: "1a ff 4e 2b ..."

# (d) Analisar os arquivos gerados
for arquivo in ["ficheiro1.txt", "ficheiro2.txt", "ficheiro3.txt"]:
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = f.read()
    contagem = Counter(dados)
    probabilidades = [v / len(dados) for v in contagem.values()]
    entropia = calcular_entropia(probabilidades)
    print(f"Entropia de {arquivo}: {entropia:.2f}")
    gerar_histograma(arquivo)
