# Funções complexos:
'''sort() organiza a lista alfabeticamente por padrão
reverse() inverte a ordem dos elementos de uma lista
clear() remove todos os elementos de uma lista
insert() insere um elemento em uma lista numa posição especifica
index() retorna o index de um elemento
count() retorna o numero de vezes que um elemento aparece na lista
remove() remove um elemento de uma lista
pop() remove o ultimo elemento da lista'''

abc = [input('1 ---> '), input('2 ---> '), input('3 ---> '), input('4 ---> ')]
# pop


del abc[-1]
print(abc)


# remove

remove = input('Remover -- > ')
for elemento in abc:
    if remove == elemento:
        index = abc.index(elemento)
        del abc[index]
        print(abc)


# count


count = input('Elemento para .count ---> ')
contagem = 0

while True:
    for indexC, elementoC in enumerate(abc):
        if elementoC == count:
            contagem += 1
    print(contagem)
    break

# reverse

total = len(abc) - 1

for indexreverse, elementoreverse in enumerate(abc):
    lugar = total - indexreverse

