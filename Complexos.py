"Complexo armazena mais de um valor"
# Range(1, 10, -1)
#variavelcomplexa = ("p", "h", "e", "l", "l", "i", "p", "e")
#del variavelcomplexa =
#enumerate retorna dois valores (o elemento e a index desse elemento)
#nome.index(p)
#for elemento in variavelcomplexa:
#count conta a quantidade de termo em uma variavel
#variavel.count(elementoquequeranalisar)
#() indica uma tupla (tipo de variável complexa)
# carlos = ("carlos")
#variavelcomplexa[] serve pra pegar o index do elemento que está dentro dele
# Mais informações em ´´Atividade Complexos``
 '''O enumerate vc usa assim:
 for i,x in enumerate(var)
 i = Index do objeto analisado
 x = objeto analisado
 O enumerate serve para você usar o index do objeto
 Imagina, você quer remover um objeto x
 Mas existem 2 objetos iguais "x"
 então você usa a index dele, porque o remove smepre remove o primeiro'''

nome = ("p", "h", "e", "l", "l", "i", "p", "e")
letra = input("Escolha uma letra do nome phellipe:")
for index_analisado, elemento in enumerate(nome):
    if not letra in nome:
        print("não existe!")
        break
    else:
        if nome.count(letra) > 1:
            for x in range(len(nome) - 1, -1, -1):
                if nome[x] == letra:
                    print(f"A letra {letra} está no index {x}.")
                    break
            break
        if letra == elemento:
            print(f"A letra {letra} está na posição {index_analisado}")





