# =======================================================
#  Verificar que A == E (após codificação, cifra e canal)
# =======================================================
def verificar_igualdade_ficheiros(ficheiro_entrada, ficheiro_saida):
    """
    Compara dois ficheiros binários e indica se são idênticos.
    """
    with open(ficheiro_entrada, 'rb') as f1, open(ficheiro_saida, 'rb') as f2:
        dados1 = f1.read()
        dados2 = f2.read()

    if dados1 == dados2:
        print(f" Os ficheiros {ficheiro_entrada} e {ficheiro_saida} são idênticos.")
    else:
        print(f" Os ficheiros {ficheiro_entrada} e {ficheiro_saida} são diferentes.")
        print(f"Diferença de tamanho: {abs(len(dados1) - len(dados2))} bytes")

def verificar_igualdade_ficheiros(ficheiro_entrada, ficheiro_saida):
    """
    Compara dois ficheiros binários e indica se são idênticos.
    """
    with open(ficheiro_entrada, 'rb') as f1, open(ficheiro_saida, 'rb') as f2:
        dados1 = f1.read()
        dados2 = f2.read()

    if dados1 == dados2:
        print(f" Os ficheiros {ficheiro_entrada} e {ficheiro_saida} são idênticos.")
    else:
        print(f" Os ficheiros {ficheiro_entrada} e {ficheiro_saida} são diferentes.")
        print(f"Diferença de tamanho: {abs(len(dados1) - len(dados2))} bytes")

# ========================================
# CHAMADA DA FUNÇÃO
# ========================================

# Substitua pelos nomes reais dos seus ficheiros:
verificar_igualdade_ficheiros("entrada.txt", "resultados.txt")
