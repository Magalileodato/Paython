# Calculando o divisor máximo comum em um intervalo fornecido

# Fornecendo os numeros inteiros para realiar o cálculo

#Método responsávelpor calcular o máximo divisor comum
def mdc(a,b):
    while b !=0:
        a,b = b,a % b
    return a 
    
#Solicitando ao usuário a definição dos numéros inteiros

num1 = int(input("Forneça o primeiro número."))
num2 = int(input("Forneça o segundo número."))

resultado = mdc(num1,num2)

print(f"O maior divisor comum entre {num1} e {num2} é {resultado}.")           