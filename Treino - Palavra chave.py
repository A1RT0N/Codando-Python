'''
Instruções:
-Crie um programa que peça uma palavra chave e o nome de um arquivo txt (se o arquivo não existir o programa ira criar um)
-O programa deve analizar todo o texto dentro do txt e retornar quantas vezes a palavra chave foi citada no texto
-No final de cada analize o programa deve registrar em um outro txt as seguintes informações: numero do texto analizado, a palavra chave que foi usada durante a análise, o nome do txt analizado e quantas repetições foram identificadas.
exemplo:
		   1 . Sherek  --->  Roteirosherek.txt ---> 300
		   2. Batata   --->   Receitadepure.txt ---> 10

-Observação 1: Se não houver nada escrito dentro do arquivo txt o programa ira pedir para você escrever algo dentro do mesmo
-Observação 2: Se a palavra chave não for citada nenhuma vez dentro do txt ele avisará que a palavra não foi citada nenhuma vez'''

def analise():
    global a
    global pergunta_nome_arquivo
    try:
        a = open(f"{pergunta_nome_arquivo}.txt", "r")
    except FileNotFoundError:
        pergunta_nome_arquivo = input("Arquivo não encontrado! Crie um arquivo novo:")
        b = open(f'{pergunta_nome_arquivo}.txt', "w+")
        b.close()
        a = open(f"{pergunta_nome_arquivo}.txt", "r")
    for linha in a.readlines():
        if palavra_chave in linha:
            global contador
            contador += 1

while True:
    contador = 0
    pergunta_nome_arquivo = input("Digite o nome do arquivo da palavra chave:")
    palavra_chave = input("Qual a palavra chave a ser analisada no arquivo:")
    analise()
    contador += 1
    numero_texto_analisado = 1
    pergunta_mais_palavraschaves = input("Você deseja analisar mais palavras no mesmo arquivo ou em outro? Digite 1 para Sim e 2 para Não\n--->")
    registro_informações = open("analise.txt", "a")
    if pergunta_mais_palavraschaves == "1":
        numero_texto_analisado += 1
        registro_informações.write(f"{numero_texto_analisado} . {palavra_chave} ---> {pergunta_nome_arquivo} ---> {contador}\n")
        continue
    elif pergunta_mais_palavraschaves == "2":
        registro_informações.write(f"{numero_texto_analisado} . {palavra_chave} ---> {pergunta_nome_arquivo} ---> {contador}\n")
        print("Arquivo salvo em ´´analise.txt`` com sucesso!")
        break
    else:
        print("Digite corretamente!")
        continue






