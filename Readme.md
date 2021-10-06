# Atividade funções array:
Escolher três funções do array

Recriar a função utilizando for (append não vale)
## Reverse
'''abc = [input('1 ---> '), input('2 ---> '), input('3 ---> '), input('4 ---> ')]
'''

- Mais informações em "Atividade funções complexos.py"

## Pop

del abc[-1]
print(abc)

## Remove

remove = input('Remover -- > ')
for elemento in abc:
    if remove == elemento:
        index = abc.index(elemento)
        del abc[index]
        print(abc)

## Count

count = input('Elemento para .count ---> ')
contagem = 0

while True:
    for indexC, elementoC in enumerate(abc):
        if elementoC == count:
            contagem += 1
    print(contagem)
    break

## Reverse

total = len(abc) - 1

for indexreverse, elementoreverse in enumerate(abc):
    lugar = total - indexreverse

abc = ["klma", "suamae", "lata", "batata"]
totalelementos = len(abc)
for elemento in abc:
    indexelemento = abc.index(elemento)
    if indexelemento == abc.index(elemento):
        abc.index(elemento) = abc.index(totalelementos - 1 - indexelemento)
    print(abc)

# CHOICES X CHOICE

-> Aqui vemos a importância de diferenciar choice de choices:
Choices serve para escolher uma letra de uma string ou um elemento de uma array aleatoriamente e colocá-lo em uma ARRAY
Já o choice escolhe aleatoriamente uma letra de uma string ou um elemento de uma array e transforma-o em uma STRING

- Absolute path: colocar \\ para achar arquivo.

- O que tá dentro do def não se relaciona com o que está fora do def, a não ser que tenha o global var

- Para dar parágrafo: \n

- w3schools.com/python/python_lambda.asp

###Ver aulas hashtag salvas

# Biblioteca, dicionários e cores
- Função: is.(alpha, num, etc)
- /n serve para dar enter no código
- () = tuple() = tuplas
- [] = list() = array
- {} = dict() = dictionary
- Dicionário é parecido com array, mas eu posso nomear as index
- A gente nomeia index - cerveja, Cachaça,etc
- Sendo assim, não faz sentido ter insert, já que já nomeamos os index
- Keys mostra os index nomeados (usei o len - conta quantos tem - só pra aplicação):
  - abc = len(pinga.keys()
    - print(abc)
- Values mostra os elementos dentro dos indexes nomeados:
    - abc = pinga.values()
      - print(abc)
- Itens mostra tudo no dicionário:
    - abc = pinga.items()
      -print(abc)
    - pinga["Linguiça"] = ["Linguiça´s Ramalho", 0.5]
        - print(pinga)
    - for key, value in pinga.items():
        - print(f"O {value} está na key {key}!")
- No dicionário, NÃO existe a função enumerate. Logo, precisamos usar:
  
####Explicação do monitor:
- Kyes, Valeus, Itens e []:

- Keys é o nome que você dá para a array dentro, tipo a = {"*key1*":[1,2,3], "*key2*":[2,4,5]}
- Values é o que você nomeia:a = {"key1":*[1,2,3]*, "key2":*[2,4,5]*} 
  - Caso eu queira retornar o 2 dentro da key1, eu faço:
    - a['key2'][0]
- Itens é a junção das keys e items 
  - Exemplo:
    - {*"key1":[1,2,3]*, "key2":[2,4,5]}

###Outros modos de uso:
- print(pinga["Cachaça"])
  - valorstring = float(pinga["Cachaça"][1].split("RS")[1])
    - print(valorstring)
    
####Biblioteca:
Para ver as bibliotecas instaladas já no Pycharm, é só colocar import e apertar Crtl + Espaço
-> Bibliotecas instaladas: https://docs.python.org/3/library/index.html

# Complexos

- "Complexo armazena mais de um valor"
- variavelcomplexa = ("p", "h", "e", "l", "l", "i", "p", "e")
- del variavelcomplexa =
- enumerate retorna dois valores (o elemento e a index desse elemento)
- nome.index(p)
- for elemento in variavelcomplexa:
- count conta a quantidade de termo em uma variavel
- variavel.count(elementoquequeranalisar)
- () indica uma tupla (tipo de variável complexa)
- carlos = ("carlos")
- variavelcomplexa[] serve pra pegar o index do elemento que está dentro dele
#### Mais informações em ´´Atividade Complexos``
 O enumerate vc usa assim:
 - for i,x in enumerate(var)
- i = Index do objeto analisado 
- x = objeto analisado
- O enumerate serve para você usar o index do objeto.
 Imagina, você quer remover um objeto x.
 Mas existem 2 objetos iguais "x".
 Então você usa a index dele, porque o remove smepre remove o primeiro
  
# For

- // numero antes da virgula # / divisão normal
- range (0, 11, 3) -> pega os numeros inteiros de 0 a 10 (intervalo fechado) e vê os múltiplos de 3
- range nao conta o ultimo numero, só o primeiro 
- For analisa cada letra em uma string, se você quiser analisar um texto, coloque if "text" not in variavel ... 
- Importante: o for é usado em ARRAYS!!! (for k in array: ...)
- Mas ele também pode ser usado em um intervalo (mostra quantes vezes você quer repetir) - for j in range(0, 6) - vai fazer 0, 1, 2, 3, 4 e 5
- OBSERVAÇÃO:
  - O exit(code) serve para terminar o código imediatamente. A diferença entre ele e break é que o break serve para loops 
    - Já o continue, no caso do while, ser ve para voltar ao início do loop. No caso do for, serve para ir para o próximo termo
- Concetenar = somar strings; Somar = somar ints
### Bibliotecas extras:
- import pandas 
- import pyautogui 
- import numpy 
- import openpyxl 
- import pyperclip
- import os

# Array:
- string.split(separator, maxsplit)
  - Em que:
    - string: corresponde ao nome da variável que servirá de base para a divisão; 
    - separator: indica o caractere utilizado como separador da string; 
    - maxsplit: representa a quantidade máxima de divisões realizadas.
- .split -> divisão da string -> quando tem () sem nada dentro, ele separa de acordo com os espaços na string
- .join -> Serve para juntar em uma string
- o .strip() associado ao input serve para tirar os espaços que o usuário escreveu no input
- o .lower() associado ao input serve para tornar o que o usuário escreveu como minúsculo (Ver em Prova primeira chamada 3)
- Fatiamento (serve para strings e arrays)
- TUPLAS, DIFERENTEMENTE DE ARRAYS, SÃO IMUTÁVEIS!!!
- list = array em outras linguagens
- Array tem tudo que a tupla tem, e é completamente mutável os valores (diferentemente da tupla)
- Colchetes serve para definir uma index e fazer uma complexa

# Funções complexos
- sort() organiza a lista alfabeticamente por padrão 
- reverse() inverte a ordem dos elementos de uma lista 
- clear() remove todos os elementos de uma lista 
- insert() insere um elemento em uma lista numa posição especifica
- index() retorna o index de um elemento
- count() retorna o numero de vezes que um elemento aparece na lista
- remove() remove um elemento de uma lista
- pop() remove o ultimo elemento da lista'''

# Funções de leitura:

- São funções que permite que voce escreva ou leia arquivos txt e outros (png, bite, etc)
- Função Open (transferir algum arquivo para alguma variável)

- Permissão: r (read - ler o que tá lá dentro), a(append - adiciona ), w(write - sobrescrever [não adiciona coisas apenas] = apaga e escreve dnv),b(byte --> foto), w+(se não existir o arquivo em questão, criar; se existir,dar a premissão w)

- Sempre depois de terminar, coloca .close() para fechar o arquivo (não ocorrer mais alterações)

- Read pega tudo que tá escrito e transforma em uma única string

- Readline retorna elementos para cada linha. Dá tbm pra fazer com uma linha específica (até qual termo tbm)

- Readlines = A cada linha ele trasnforma em uma array (tudo)
- Ele retorna uma array e cada elemente dessa array é uma linha
- O w+ serve pra criar a pasta de início. Ou seja, no início do código, coloque + e depois apaga só pra criar o arquivo
    - https://www.youtube.com/watch?v=F8KB5_sEQH0&ab_channel=DevAprender
- A função truncate serve para apagar tudo no arquivo

### Biblioteca de matemática:
import cmath
### Biblioteca com strings para usar em input:
import string

string.ascii_letters

string.punctuation

