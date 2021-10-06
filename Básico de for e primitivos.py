# IMPORTANTE: Caso queira ver mais sobre isso e outros documentos, vá para pasta "Arquivos programação"

# BÁSICO DE FOR:

# for analisa cada termo em uma variável. Ele é um loop
# a variável "letra" é uma variável exclusiva para o for
# == é só pra true ou falso
# for ... in ...:
# = determina o valor
# == pergunta se é igual
#// numero antes da virgula # / divisão normal
#range (0, 11, 3) -> pega os numeros inteiros de 0 a 10 (intervalo fechado) e vê os múltiplos de 3
#range nao conta o ultimo numero, so o primeiro

# Exemplo de atividade com for:
#palavra = "ajsvdjasfb xponconpelasdnm s"
#semo = ""
#for letra in palavra:
    #if letra == "o":
        #semo += letra # letra + sem o (nada)
#print(semo)

# For analisa cada letra em uma string, se você quiser analisar um texto, coloque if "text" not in variavel ...

# Importante: o for é usado em ARRAYS!!! (for k in array: ...)
# Mas ele também pode ser usado em um intervalo (mostra quantes vezes você quer repetir) - for j in range(0, 6) - vai fazer 0, 1, 2, 3, 4 e 5

# Range:
print(list(range(0,10,2)))


# Exercício:
perg1 = int(input("Qual o número inicial do intervalo? "))
perg2 = int(input("Qual o número final do intervalo? "))

for numero in range(perg1, perg2+1):
    if numero % 6 == 0:
        print(f"O {numero} é múltiplo de 6")
        print("-="*30)
    if numero % 2 == 0:
        print(f"O {numero} é par")
        print("-="*30)
    else:
        print(f"O {numero} é ímpar")
        print("-="*30)

# OBSERVAÇÃO:
# O exit(code) serve para terminar o código imediatamente. A diferença entre ele e break é que o break serve para loops
# Já o continue, no caso do while, ser ve para voltar ao início do loop. No caso do for, serve para ir para o próximo termo


# PRIMITIVOS:
'''
int -> número inteiro
float -> número real
str -> strig => palavra ou qualquer coisa entre aspas
'''
# Exemplo
n1 = int(input("Escreva:"))
n2 = int(input("Escreva dnv:"))
print(type(n2))  # SERVE PARA SABER A NATUREZA DE UMA VARIÁVEL (str, int, float, etc)!!!
s = n1 + n2
print(f"A soma é {s}")
'''
-> Quando você faz isso, o Python concatena os elementos em vez de somar, pois n1 e n2 foram configuradas como strings.
Para resolver isso, basta colocar int em n1 e n2
'''

# Bônus - interpolação:
a = 'João'
b = 32
c = 1242.3
print(f"O {a:^20} tem {b} anos e ganha R${c:.2f}")
