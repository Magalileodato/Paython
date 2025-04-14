# Programa responsável por calcular os multiplos de quadtro
# Aapartir de um intervalo fornecido pelo usuário

#Solicitando ao usuário a definição do intervalo

left = int(input("Digite o início intervalo a ser considerado."))
rigth = int(input("Digite o fim do intervalo a ser considerado."))

#Garantindo que left seja menor que rigth
if left > rigth:
    left, rigth = rigth, left


# Criando uma lista de array para guardar os numeros multiplos de 4

numeros_multiplos_quatro = []

# Gerando os numeros multiplos de 4 dentro do intervalo fornecido


num = left
for num in range(left, rigth + 1):
    if num % 4 == 0:
        numeros_multiplos_quatro +=[num]
num = num+1

print("Os números de quatro sao:",numeros_multiplos_quatro )           
     