'''c = 12
def soma(a = 0, b = 0):
    # a = 0 serve para definir, caso a pessoa não coloque nada em soma()
    global c
    c = 15
    return a-b
print(soma(12, 21))

def duvida():
    n = int(input("Escreva um número:"))
    for k in range(n):
        print(k)
duvida()
# Isso daqui:
from random import randint
arma = {1: 'Espada', 2: 'Adaga', 3: 'Arco', 4: 'Flecha', 5: 'Cajado'}
arma_oficial = arma[randint(1,5)]
# É a mesma coisa disso:
from random import choices
arma = ['Espada', 'Adaga', 'Arco', 'Flecha', 'Cajado']
arma = choices(arma)
print(arma)

a = int(input("Digite um numero para ser convertido em binário:"))
bin_a = bin(a)
print(bin_a)

dados_1 = "Maria Cláudia;23;Desenvolvedora Web"
nome,idade,profissao = dados.split(";")
print(nome)
print(idade)
print(profissao)

a = open("fichas.txt", "r")
for linha in a.readlines():
    print(linha.split("_"))

import random
print(random.uniform(0, 10)'''
import time

'''a = open("dados.txt", "r")
for linha in a.readlines():
    print("bolo" in linha)
'''

# Bibliotecas extras:
import pandas
import pyautogui
import numpy
import openpyxl
import pyperclip

time.sleep(8)
print(pyautogui.position())
# Aula 01 intensivão de Python: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga  -> Júpiter

# Sobre a prova:
# 2 questões de 40 e 1 questão de 20, usando def
# Avaliação baseada em: Otimização, funcional, comentário (sem estupido e sem mt), estabilidade (try), sintaxe (escrita)
# Questões: Banco de dados (dict); Programação científica - lógica (Alg romanos e pi), Trabalhosa e fácil (RPG)