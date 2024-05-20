import os
os.system("cls || clear")

# Dados do usuário
nomeProduto = input("Digite o nome do produto : ")
quantidadeProduto = int(input("Digite a quantidade do produto : "))
precoUnitario = float(input("Digite o preço unitário do produto : "))

# Cálculos
total = quantidadeProduto * precoUnitario
valorTotal = total - desconto

if quantidadeProduto <= 5:
    desconto: float = (total * 2) / 100

    if quantidadeProduto > 5 and quantidadeProduto <= 10:
        desconto: float = (total * 3) / 100

        if quantidadeProduto > 10:
            desconto: float = (total * 5) / 100

# Resultados
print("---Resultados---")
print(f"Nome do produto : {nomeProduto}")
print(f"Quantidade do produto : {quantidadeProduto}")
print(f"Preço Unitário : {precoUnitario}")
print(f"Total : {total}")
print(f"Total a pagar : {valorTotal}")

