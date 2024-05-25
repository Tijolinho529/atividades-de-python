import os
os.system("clear")

# Variáveis
quantidadeNotas = 4
notas = []

for i in range(quantidadeNotas):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / quantidadeNotas

print("\nExibindo notas: ")
print