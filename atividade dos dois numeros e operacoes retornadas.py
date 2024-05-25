import os
os.system("clear")

def somar(n1, n2):
    resultadoSoma = n1 + n2
    return resultadoSoma

def subtracao(n1, n2):
    resultadoSubtracao = n1 - n2
    return resultadoSubtracao

def multiplicacao(n1, n2):
    resultadoMultiplicacao = n1 * n2
    return resultadoMultiplicacao

def divisao(n1, n2):
    resultadoDivisao = n1 / n2
    return resultadoDivisao

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtrair = subtracao(primeiroNumero, segundoNumero)
multiplica = multiplicacao(primeiroNumero, segundoNumero)
dividir = divisao(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")
print(f"Subtracao: {subtrair}")
print(f"Multiplicação: {multiplica}")
print(f"Divisão: {dividir}")
