# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
num= int(input("digite um número"))
def verificar_paridade(num):
    if num % 2 == 0:
        return f"O número {num} é par."
    else:
        return f"O número {num} é ímpar."

resultado = verificar_paridade(num)
print(resultado) 
