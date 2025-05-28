import matplotlib.pyplot as plt
import time
import re

# Função para ler os pontos do arquivo no formato: Point(id=..., x=..., y=...)
def ler_pontos_formatados(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

    pontos = []

    # Pula a primeira linha (com a quantidade total e o tempo)
    for linha in linhas[1:]:
        linha = linha.strip()
        if linha.startswith("Point"):
            # Extrai os valores de x e y usando expressão regular
            match = re.search(r'x=([-\d.Ee]+), y=([-\d.Ee]+)', linha)
            if match:
                x = float(match.group(1))
                y = float(match.group(2))
                pontos.append((x, y))

    return pontos

# Simula tempo de execução para diferentes quantidades de pontos
def simular_tempo_processamento(pontos):
    tamanhos = [100, 500, 1000, 5000, 10000, 50000, 100000, 200000]
    tempos = []

    for tamanho in tamanhos:
        if tamanho > len(pontos):
            break

        inicio = time.time()

        # Simula processamento dos pontos
        for i in range(tamanho):
            x, y = pontos[i]
            # Aqui você pode realizar alguma operação se quiser simular algo real

        fim = time.time()
        tempos.append(fim - inicio)

    return tamanhos[:len(tempos)], tempos

# Lê os pontos dos dois arquivos
pontos_uniao = ler_pontos_formatados('uniao.txt')
pontos_inter = ler_pontos_formatados('intercessao.txt')

# Simula tempo de execução
dim_uniao, tempo_uniao = simular_tempo_processamento(pontos_uniao)
dim_inter, tempo_inter = simular_tempo_processamento(pontos_inter)

# Geração do gráfico
plt.plot(dim_uniao, tempo_uniao, label='União', marker='o', color='blue')
plt.plot(dim_inter, tempo_inter, label='Interseção', marker='s', color='green')

plt.xlabel('Quantidade de pontos processados')
plt.ylabel('Tempo de execução (simulado em segundos)')
plt.title('Tempo vs Quantidade de Pontos — União vs Interseção')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
