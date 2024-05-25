import os
os.system("clear")

# Solicitando a data de nascimento do usuário
print("Digite sua data de nascimento")
dia = int(input("Dia: "))
mes = input("Mês: ")
ano = int(input("Ano: "))

os.system("clear")

# Mostrando a data formatada
print(f"Você nasceu no dia {dia} de {mes} de {ano}")