'''
-> Criar um programa que peça valores numericos em loop até que a pessoa negue colocar mais valores
Depois o programa classifica os números do menor pra maior numero
Depois o programa classifica os números do maior para o menor numero
Depois o programa classifica qual é o menor numero
Depois o programa classifica qual é o maior numero
Numeros divisiveis por 6
Numeros pares'''


'''sort() organiza a lista alfabeticamente por padrão
reverse() inverte a ordem dos elementos de uma lista
clear() remove todos os elementos de uma lista
insert() insere um elemento em uma lista numa posição especifica
index() retorna o index de um elemento
count() retorna o numero de vezes que um elemento aparece na lista
remove() remove um elemento de uma lista
pop() remove o ultimo elemento da lista'''

def division_6():
    for numero in list_1:
        if int(numero) % 6 == 0:
            print(f"{numero} é divisível por 6")
        elif int(numero) < 0:
            print(f"{numero} é menor que zero (No conjunto dos números naturais, não é divisível por 6)")
        else:
            print(f"{numero} não é divisível por 6")

def pares():
    for par in list_1:
        if int(par) % 2 == 0:
            print(f"{par} é par")
        elif int(par) < 0:
            print(f"{par} é menor que zero (No conjunto dos números naturais, não é divisível por 6)")
        else:
            print(f"{par} não é par")

list_1 = list()
while True:
    try:
        pergunta_1 = float(input("Digite valores numéricos:"))
        list_1.append(pergunta_1)
        pass
    except ValueError:
        print("Digite corretamente!")
        continue
    try:
        pergunta_2 = input("Escreva C se deseja continuar ou S se deseja sair:").lower().strip()
    except ValueError:
        print("Escreva apena C ou S!")
        continue
    if pergunta_2 == "c":
        continue

    elif pergunta_2 == "s":
        print(list_1)
        list_1.sort()
        print(list_1)
        list_1.reverse()
        print(list_1)
        print(f"O menor número da lista é: {list_1[-1]}")
        print(f"O maior número da lista é: {list_1[0]}")
        division_6()
        pares()
        break
    else:
        print("Digite corretamente!")
        continue


