import os
os.system("cls || clear")

# Variáveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite sua primeira nota: "))
segundaNota = float(input("Digite sua segunda nota: "))
media = (primeiraNota + segundaNota) / 2

# Dados do usuário
print(f"Nome : {nome}")
print(f"Idade : {idade}")
print(f"Primeira nota : {primeiraNota}")
print(f"Segunda nota : {segundaNota}")
print(f"Média : {media}")