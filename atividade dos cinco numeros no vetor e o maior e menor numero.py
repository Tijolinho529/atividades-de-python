import os
os.system("clear")

# Variáveis
quantidadeNumeros = 5
numeros = []

for i in range(quantidadeNumeros):
    numero = float(input(f"Digite o {i}º numero: "))
    numeros.append(numero)

maiorNumero = max(maiorNumero, numero)
menorNumero = min(menorNumero, numero)

print("---Resultados---")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")