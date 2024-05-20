import os
os.system ("cls || clear")

# Variáveis

soma = 0

# Dados do usuário
for i in range (1, 3) :    
    while True:
        nota = float(input(f"Digite sua {i}º nota : "))

        if nota > 10 or nota < 0:
            print("Nota inválida")
        else:
            soma += nota
            break


media : float = soma / i    

import os
os.system ("cls || clear")
print(f"---Resultados---")
print(f"Nota: {nota}")
print(f"Média: {media}")