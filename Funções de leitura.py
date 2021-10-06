# São funções que permite que voce escreva ou leia arquivos txt e outros (png, bite, etc)

# Função Open (transferir algum arquivo para alguma variável)

# Permissão: r (read - ler o que tá lá dentro), a(append - adiciona ), w(write - sobrescrever [não adiciona coisas apenas] = apaga e escreve dnv),b(byte --> foto), w+(se não existir o arquivo em questão, criar; se existir,dar a premissão w)

# livro --> dados.txt (abrir arquivos)

# Sempre depois de terminar, coloca .close() para fechar o arquivo (não ocorrer mais alterações)

# /n serve para dar enter

# Read pega tudo que tá escrito e transforma em uma única string

# Readline retorna elementos para cada linha. Dá tbm pra fazer com uma linha específica (até qual termo tbm)

# Readlines = A cada linha ele trasnforma em uma array (tudo)
# Ele retorna uma array e cada elemente dessa array é uma linha
# O w+ serve pra criar a pasta de início. Ou seja, no início do código, coloque + e depois apaga só pra criar o arquivo

# https://www.youtube.com/watch?v=F8KB5_sEQH0&ab_channel=DevAprender

#def = define function

# Biblioteca de matemática:
'''import cmath
cmath.'''
# Biblioteca com strings para usar em input:
'''import string
string.ascii_letters
string.punctuation'''

# crtl - = ...
from time import sleep as intervalo

# Lipe tinha colocados dados como dados.txt

livro = open("kleber.txt", "r+")
livro.read()
livro.readline()
livro.readlines()

txt = open("kleber.txt", "a")
txt.write("\nbatata\n")

intervalo(2)

livro2 = open("kleber.txt", "w")
livro2.write(f'{input("Escreva algo: ")}\n')
livro2.write(f'{input("Escreva algo: ")}\n')
livro2.close()

gatinho = open("kleber.txt", "r")

for linha in gatinho.readline():
    print(linha)

def peça():
    if input("Qual é a senha?") != "Jailson Mendes":
        print("Essa não é a peça que cê queria")
    else:
        print("Você entrou - era essa peça que eu queria")

peça()

def sum(num1, num2):
    print(num1 + num2)

sum(12, 14)

def somar(number1, number2):
    return number1 + number2

print(somar(12, 13))

def tratamento(abc):
    abc.split("")
    "\n"
    return

# O close serve para fechar um programa para impedir hacker (sempre coloque .close() ao final do projeto)


# Curiosidade: biblioteca os

import os
while True:
    perg = input("Digite o arquivo que deseja remover:")
    if os.path.exists(perg):
        os.remove(perg)
        print("Arquivo removido com sucesso!")
        break
    else:
        print("Digite corretamente")
        continue




# Dica não dada por felipe:

# A função truncate serve para apagar tudo no arquivo:
f = open('fichas.txt', 'r+')
f.truncate(0) # need '0' when using r+
ler = f.read()
print(ler)