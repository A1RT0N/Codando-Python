# Fatorial, Combinação, Permutação, Arranjo e Permutação com Repetição

# Fatorial ou permutação simples:
def factorial(escolha):
    num = 1 # Definindo uma constante que vai ser multiplicada
    while escolha >= 1:
        num = num * escolha
        escolha = escolha - 1 # Multiplicando a constante por 'escolha' e ir reduzindo 1
    return (num)


# Permutação com repetição:
def permutação_repetição():
    n_objetos = int(input("Digite o número de objetos no total:"))
    pergunta = int(input("Número de objetos repetidos:"))
    elementos_repetidos = [pergunta] #Coloquei em uma array porque é mais fácil de manipular, mesmo que os elementos sejam int
    contador_divisor = 1 # Constante
    while True:
        mais = input("Digite (1) se há mais objetos repetidos. Digite (2) se não há mais:")
        if mais == "1":
            pergunta2 = int(input("Número de novos objetos repetidos:"))
            elementos_repetidos.append(pergunta2)# Aqui o *= não tava resolvendo
            # Ele adiciona um elemento na lista a cada vez que se deseja adicionar um objeto repetido (que é o fatorial do denominador da permutação com repetição)
            continue
        elif mais == "2":
            for numeros in elementos_repetidos:
                contador_divisor *= factorial(numeros) # Ele pega cada elemento na lista (fatoriais) e vai multiplicando na constante
            print(factorial(n_objetos) / contador_divisor)
            break


# Combinação e arranjo:
def combinação_arranjo():
    n_combinação = int(input("Digite o número (n) de objetos no total:"))
    a = factorial(n_combinação)
    pergunta = int(input("Número de objetos (p) escolhidos:"))
    p = factorial(pergunta)
    subtração = n_combinação - pergunta
    b = factorial(subtração)
    question = input("A ordem da escolha importa? Digite 1 se for arranjo ou digite 2 se for combinação:")
    if question == "1":
        print(a/b)
    elif question == "2":
        print(a/(b*p))
    else:
        print("Escreva corretamente!")


# Rodando o código:
escolha = int(input("Digite o número fara encontrar o fatorial desse número: \n --->"))
print(factorial(escolha))
permutação_repetição()
combinação_arranjo()










# Outra forma de escrever um fatorial
'''
produtorio = 1
while escolha > 0:
    produtorio *= escolha
    escolha = escolha - 1
    if escolha == 1:
        print(produtorio)
        break
    else:
        continue'''