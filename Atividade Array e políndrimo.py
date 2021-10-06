# Escolher três funções do array
# Recriar a função utilizando for (append não vale)
# Exemplo:
# REVERSE
'''abc = [input('1 ---> '), input('2 ---> '), input('3 ---> '), input('4 ---> ')]
'''
# Faltam: copy insert sort

# pop

'''
del abc[-1]
print(abc)
'''

# remove

'''
remove = input('Remover -- > ')
for elemento in abc:
    if remove == elemento:
        index = abc.index(elemento)
        del abc[index]
        print(abc)
'''

# count

'''
count = input('Elemento para .count ---> ')
contagem = 0

while True:
    for indexC, elementoC in enumerate(abc):
        if elementoC == count:
            contagem += 1
    print(contagem)
    break
'''

# reverse

'''total = len(abc) - 1

for indexreverse, elementoreverse in enumerate(abc):
    lugar = total - indexreverse


'''
'''abc = ["klma", "suamae", "lata", "batata"]
totalelementos = len(abc)
for elemento in abc:
    indexelemento = abc.index(elemento)
    if indexelemento == abc.index(elemento):
        abc.index(elemento) = abc.index(totalelementos - 1 - indexelemento)
    print(abc)'''



'''
-> Crie um programa que mostre se uma palavre é ou não um políndromo
'''
frase = input("Qual a frase? ").upper().replace(" ", "")
print(frase)
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

