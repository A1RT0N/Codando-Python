# count

quantos = ["Heitor", "Phelipe", "G_faria", "Matheus Lopes", "Luis", "Nenhum soldado ficara para trás", "1", "1", "1", "1"]
find = input("Find ---> ")

controle = 0
for elemento in quantos:
    if elemento == find:
        controle += 1
print(controle)
# index
quantos = ["Heitor", "Phelipe", "G_faria", "Matheus Lopes", "Luis", "Nenhum soldado ficara para trás", 1, "1", "2", 2]

while True:
    querer = input("Texto (1) // numero (2) ---> ")
    if querer == "1":
        qst = input("Exemplo ---> ")
        break
    elif querer == "2":
        qst = int(input("Exemplo ---> "))
        break
    else:
        continue

for index, elemento in enumerate(quantos):
    if elemento == qst:
        print(index)
# insert
array1 = ["Heitor", "Phelipe", "G_faria", "Matheus Lopes", "Luis", "Nenhum soldado ficara para trás", 1, "1", "2", 2]

index_insert = int(input("Index --> "))
element_insert = input("Elemento --> ")

array2 = list()

for index, elemento in enumerate(array1):
    if index != index_insert:
        array2.append(elemento)
    else:
        array2.append(element_insert)
        array2.append(elemento)

print(array2)

# pop
# Sem for
batata = ["Heitor", "Phelipe", "G_faria", "Matheus Lopes", "Luis", "Nenhum soldado ficara para trás"]
index = len(batata) - 1
del batata[index]
print(index)

# Com for
for controle in batata:
    if batata.index(controle) == len(batata) - 1:
        batata.remove(controle)
# remove

exemplo = ["Heitor", "Phelipe", "G_faria", "Matheus Lopes", "Luis", 1, 2 ,3]

while True:
    querer = input("Texto (1) // numero (2) ---> ")
    if querer == "1":
        qst = input("Exemplo ---> ")
        break
    elif querer == "2":
        qst = int(input("Exemplo ---> "))
        break
    else:
        continue

for elemento in exemplo:
    if elemento == qst:
        index = exemplo.index(elemento)
        del exemplo[index]

print(exemplo)