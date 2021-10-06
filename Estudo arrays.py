# TUPLAS, DIFERENTEMENTE DE ARRAYS, SÃO IMUTÁVEIS!!!
# list = array em outras linguagens
# Array tem tudo que a tupla tem, e é completamente mutável os valores (diferentemente da tupla)
# Colchetes serve para definir uma index e fazer uma complexa

pato = [ "1carro", "fendas faringianas", "saco", "vitelo", "cordados"]

#del pato [0]

#print(pato)

# Adicionar um elemento:

pato.append(input("Qual o seu nome?"))

print(pato)

# arrays

pato = ["pato", "phelipe", "abc"]

# Adiciona um valor
pato.append(input("Ola qual é seu nome? ---> "))

abc = pato.copy()
print(abc)


# Contar quantos de um elemento expecifico existem naquela array
print(pato.count("Phelipe"))


# Achar a index de um determinado elemento dentro da array
print(f"O elemento abc se encontra na index: {pato.index('abc')}")
# Obs: o .index(x) vale também para tuplas

# Insere um elemento em uma posição expecifica dentro das array
pato.insert(1, "apressado")
print(pato)


# Ele "estora" o ultimo elemento da array
print(f"Antes do pop {pato} !")
pato.pop()
print(f"Depois do pop {pato} !")


# Remove um elemento pelo seu valor e não por sua index (como o del faz)
pato.remove("abc")
print("abc removido")


# Inverte a array
pato.reverse()
print(pato)


# Ele organiza a array em ordem alfa numerica
# 1 ---> 1234567
# 2 ---> ABC
# 3 ---> abc
pato.sort()
print(pato)


# Manipulando textos

curso_em_video = "Eu não sou noé, seu fdp!"
# Fatiamento (serve para strings e arrays):
print(curso_em_video[:10])
print(curso_em_video[16:])
print(f"Olha como sou noiado: {curso_em_video[2:19:2]}")
# Análise:
print(len(curso_em_video))
print(curso_em_video.count("e",0, 19))
print(f'A primeira letra do termo ``fdp´´ está no index:{curso_em_video.lower().find("fdp")}')
# Se em no print acima com find der -1, significa que não existe o termo em análise na string em questão
if 'noé' in curso_em_video:
    print(f'O termo ´´noé`` tem em na strg: {curso_em_video}')
# Transformação:
print(curso_em_video.replace("seu fdp!", "meu caro amigo lindo e maravilhoso!"))
print(curso_em_video.capitalize()) # Capitalize coloca só a primeira letra maiúscula
print(curso_em_video.title()) # Title coloca as letras iniciais de palavras maiúsculas
# Observação:
# o .lower() associado ao input serve para tornar o que o usuário escreveu como minúsculo (Ver em Prova primeira chamada 3)
# o .strip() associado ao input serve para tirar os espaços que o usuário escreveu no input
demente = input("Digite bastante espaço antes de escrever e depois pro cê ver:")
print(f'Consertei sua cagada com os espaços:{demente.strip()}')
# .join -> Serve para juntar em uma string
nome = ["Pato", "Auau", "Lélé", "Escola"]
print(" ".join(nome))
print("_".join(nome))
'''Ver atividade do MARCOS!'''

# .split -> divisão da string -> quando tem () sem nada dentro, ele separa de acordo com os espaços na string
joao = "Eu preciso me sentir bem comigo mesmo, pois sou muito bom e não preciso ser melhor que ninguém"
dividido = joao.split()
print(dividido)
print(f'Dentro da string, na palavra ´´preciso``, a terceira letra dessa palavra é:{dividido[1][3]}')
print(joao.split("e"))
'''
string.split(separator, maxsplit)
Em que:
string: corresponde ao nome da variável que servirá de base para a divisão;
separator: indica o caractere utilizado como separador da string;
maxsplit: representa a quantidade máxima de divisões realizadas.
'''
print(joao.lower().split(" ", 4))