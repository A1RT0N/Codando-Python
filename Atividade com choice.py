# Joguinho
from random import choice
alfabeto = "abcdefghijklmnopqrstuvwxyz"
palavra = ""
pontos = 0

quantos = int(input("Quantos letras terá a palavra? ---> "))
while True:
    if len(palavra) == quantos:
        letra_escolhida = choice(palavra)
        acertar = int(input(f"Quantas letras {letra_escolhida} existe na palavra secreta? ---> "))
        if acertar == palavra.count(letra_escolhida):
            print("Você acertou!")
            pontos += 1
            palavra = ""
            continue
        else:
            print(f"Você errou, sua pontuação foi de {pontos} pontos")
            break
    else:
        palavra += choice(alfabeto)

'''
Aqui vemos a importância de diferenciar choice de choices:
Choices serve para escolher uma letra de uma string ou um elemento de uma array aleatoriamente e colocá-lo em uma ARRAY
Já o choice escolhe aleatoriamente uma letra de uma string ou um elemento de uma array e transforma-o em uma STRING '''