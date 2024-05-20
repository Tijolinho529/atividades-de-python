import os
os.system("cls || clear")

# Variáveis
primeiroNúmero = int(input("Digite seu primeiro número : "))
segundoNúmero = int(input("Digite seu segundo número : "))
soma = primeiroNúmero + segundoNúmero
media = soma / 2
produto = primeiroNúmero * segundoNúmero
maiorNumero = max(primeiroNúmero, segundoNúmero)
menorNumero = min(primeiroNúmero, segundoNúmero)

# Dados do usuário
print(f"Primeiro número : {primeiroNúmero}")
print(f"Segundo número : {segundoNúmero}")
print(f"Média : {media}")
print(f"Soma : {soma}")
print(f"Produto : {produto}")
print(f"Maior número : {maiorNumero}")
print(f"Menor número : {menorNumero}")