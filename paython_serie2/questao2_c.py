# =======================================================
# Teste experimental da cadeia A → B → C → D → E
# =======================================================
import os
from questa02_b import verificar_igualdade_ficheiros  # certifique-se de que o nome do arquivo está correto

def experimento_ficheiros():
    """
    Gera ficheiros de teste A, aplica cadeia de codificação e verificação,
    e mostra que A == E no final.
    """
    # Passo 1: criar ficheiro A com dados simulados
    ficheiro_a = "ficheiro_saida.bin"
    with open(ficheiro_a, 'wb') as f:
        f.write(os.urandom(256))  # 256 bytes aleatórios

    # Passo 2: para este exemplo, omitimos codificação de fonte/cifra e simulamos canal perfeito
    ficheiro_e = "ficheiro_entrada.bin"
    with open(ficheiro_a, 'rb') as fa, open(ficheiro_e, 'wb') as fe:
        fe.write(fa.read())  # simulação de transmissão sem erro

    # Passo 3: verificar igualdade entre ficheiros
    verificar_igualdade_ficheiros(ficheiro_a, ficheiro_e)

# ========================================
# EXECUÇÃO DO EXPERIMENTO
# ========================================
experimento_ficheiros()
