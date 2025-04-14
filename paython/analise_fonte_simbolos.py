import os
import zipfile
import collections
import math
import matplotlib.pyplot as plt

def extract_files(zip_path, extract_to="temp_files"):
    # Extrai os arquivos do ZIP para um diretório temporário. 
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def analyze_file(file_path):
    #Analisa um arquivo e retorna estatísticas sobre os símbolos. 
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    total_chars = len(content)  # Número total de caracteres no arquivo
    freq = collections.Counter(content)  # Contagem de frequência dos caracteres
    
    # Determina o símbolo mais frequente e sua contagem
    symbol, max_count = freq.most_common(1)[0]
    probability = max_count / total_chars  # Probabilidade do símbolo mais frequente
    information = -math.log2(probability)  # Informação própria do símbolo
    
    # Calcula a entropia do arquivo
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in freq.values())
    
    return symbol, probability, information, entropy, freq

def plot_histogram(freq, file_name):
    # Gera um histograma dos símbolos no arquivo.
    symbols, counts = zip(*freq.items())  # Separa os símbolos e suas contagens
    plt.figure(figsize=(10, 5))  # Define o tamanho da figura
    plt.bar(symbols, counts)  # Cria o gráfico de barras
    plt.xlabel("Símbolos")
    plt.ylabel("Frequência")
    plt.title(f"Histograma de frequência - {file_name}")
    plt.show()

def main(zip_path):
    """ Função principal que processa todos os arquivos do ZIP. """
    extract_dir = extract_files(zip_path)  # Extrai os arquivos para um diretório temporário
    
    for file_name in os.listdir(extract_dir):  # Percorre todos os arquivos extraídos
        file_path = os.path.join(extract_dir, file_name)
        if os.path.isfile(file_path):  # Verifica se é um arquivo
            # Analisa o arquivo e obtém as estatísticas
            symbol, probability, information, entropy, freq = analyze_file(file_path)
            
            # Exibe os resultados
            print(f"Arquivo: {file_name}")
            print(f"Símbolo mais frequente: {symbol}")
            print(f"Probabilidade: {probability:.6f}")
            print(f"Informação própria: {information:.6f} bits")
            print(f"Entropia: {entropy:.6f} bits/símbolo")
            print("-" * 40)
            
            # Gera o histograma para visualização
            plot_histogram(freq, file_name)

# Substitua pelo caminho real do arquivo ZIP
zip_path = "TestFilesCD.zip"
main(zip_path)