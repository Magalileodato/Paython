import zipfile
import os
import collections
import math
import matplotlib.pyplot as plt
import mimetypes

# Função para calcular entropia e estatísticas
def analisar_ficheiro(path):
    with open(path, "rb") as f:
        dados = f.read()
    
    contador = collections.Counter(dados)
    total = sum(contador.values())

    simbolo_mais_freq, freq = contador.most_common(1)[0]
    probabilidade = freq / total
    info_propria = -math.log2(probabilidade)

    entropia = -sum((f/total) * math.log2(f/total) for f in contador.values())

    return {
        "simbolo": simbolo_mais_freq,
        "frequencia": freq,
        "probabilidade": probabilidade,
        "info_propria": info_propria,
        "entropia": entropia,
        "contador": contador
    }

# Função para gerar histograma
def gerar_histograma(contador, titulo):
    plt.figure(figsize=(10, 4))
    itens = sorted(contador.items(), key=lambda x: x[0])
    x = [item[0] for item in itens]
    y = [item[1] for item in itens]
    plt.bar(x, y)
    plt.title(titulo)
    plt.xlabel("Símbolos (bytes)")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Caminho do ZIP
zip_path = "TestFilesCD.zip"
extrair_para = "TestFilesCD"

# Extrair arquivos
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extrair_para)

# Listar arquivos extraídos
estatisticas = []
tipos_arquivo = collections.Counter()

for root, _, files in os.walk(extrair_para):
    for nome_arquivo in files:
        caminho = os.path.join(root, nome_arquivo)
        tipo, _ = mimetypes.guess_type(caminho)
        tipos_arquivo[tipo or "desconhecido"] += 1

        try:
            resultado = analisar_ficheiro(caminho)
            estatisticas.append((nome_arquivo, resultado))
            print(f"\nArquivo: {nome_arquivo}")
            print(f"  Símbolo mais frequente: {resultado['simbolo']} (byte)")
            print(f"  Probabilidade: {resultado['probabilidade']:.4f}")
            print(f"  Informação própria: {resultado['info_propria']:.4f} bits")
            print(f"  Entropia: {resultado['entropia']:.4f} bits/símbolo")
            gerar_histograma(resultado['contador'], f"Histograma de {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao processar {nome_arquivo}: {e}")

# Mostrar os tipos de arquivos mais comuns
print("\nTipos de arquivos mais comuns:")
for tipo, count in tipos_arquivo.most_common():
    print(f"  {tipo}: {count}")

