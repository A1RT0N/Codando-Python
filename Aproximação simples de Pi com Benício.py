import math
import random

# Definindo o número de lançamentos:
n = int(input("Digite o número de lançamentos:"))

# Definindo o contador de vezes que a agulha toca a linha:
contador = 0

# Criando uma agulha para cada lançamento:

for k in range(n):
    b = random.random() # Isso cria um número entre zero e um
    t = random.random() * 2 * math.pi
    # Verificando se a agulha toca ou não a linha:
    if math.ceil(min(b, b + math.sin(t))) == math.floor(max(b, b + math.sin(t))):
        contador += 1

# Gerando o resultado:
print(f"O número de agulhas lançadas foi: {n}")
print(f"O número de agulhas que tocaram a linha foi {contador}")
print(f"A probabilidade obtida experimentalmente foi: {contador/n}")
print(f"Uma aproximação para o valor de pi será: {2*n/contador}")
