nome = ("p","h","e","l","i","p","e")
letra = input("Qual letra você quer ver dentro de phelipe? _ ")

for index, letrinha in enumerate(nome):
    if letra not in nome:
        print("Essa letra não está no nome.")
        break
    else:
        if nome.count(letra) > 1:
            for x in range(len(nome)-1, -1, -1):
                if nome[x] == letra:
                    print(f"A letra {letra} está no index {x}.")
                    break
            break
        else:
            if letra == letrinha:
                print(f"A letra {letra} está no index {index}.")

# O enumerate retorna uma tupla com 2 valores, logo é recomendado 2 variáveis no for, uma para a index e outra para o termo equivalente da index.
# Caso você queira fazer pegar cada letra de elementos de um complexo faça:
name = ("Joao", "Maria", "Carlos")
''' for suamae in name:
   for letra in suamae:
       print(letra)'''
for index_analisado , nome_analisado in enumerate(name):
    print(f"O elemento {nome_analisado} se localiza no index: {index_analisado}!")
'''    tup = (1, 2, 3, 4, 5)
    print(tup.index[2])'''