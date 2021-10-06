# Comando:
'''
 -> Crie um programa que gere fichas de rpg:
 ---- Parte 1 ----
 O programa deve perguntar para o usuario se ele deseja importar uma ficha de rpg já existente (em um txt) ou se ele gostaria de criar uma
 Caso o usuario queira importar uma ficha já existente o programa vai pedir o nome do txt onde está localizado a ficha
 E após pegar o nome da ficha o programa ira importar os atributos do jogador pra dentro do sistema
 Mas se o usuario quiser criar uma, o programa irá requisitar o nome do personagem e sua a classe (Guerreiro, assasino ou mago)
 Posteriormente o programa ira gerar os seguintes valores de maneira randomica:
 Mana (de 1 a 20), vida (de 1 a 20), carisma (1 a 4), o tipo de arma (espada, adagas, arco e flecha e cajado) e fome (de 1 a 4)
 ---- Parte 2 ----
 Após gerar a ficha ou importa-la vocês deverão dar opções para o jogador de manipular os valores de sua ficha como no exemplo abaixo:
 Você gostaria de: Mudar a vida (1) // Mudar a mana (2) // Mudar a fome (3) // Salvar a ficha em um txt (4) // Jogar dado (5) // Sair (6) --->
 Ps: Se o jogador inserir algum valor no programa que não seja valido o programa deve alerta-lo e pedir para  inserir o valor novamente
 Ps2: Não se esqueça do try e do except
 Ps3: Se a mana, vida ou fome do jogador tiver em "0" o programa deve alertar o usuario'''

from random import randint, choices

# Criando novo arquivo:
def importar_arquivo(arquivo):
    try:
        a = open(f'{arquivo}.txt', "r") # Coloquei format para o usuário não ter que escrever .txt
        print(f"O seu arquivo possui as seguintes fichas: {a.readlines()}\n Onde cada termo entre ´´_`` representa respectivamente: Nome do personagem, Classe, Mana, Vida, Carisma, Fome e Arma") # Lendo a linha do arquivo e mostrando ao usuário
    except FileNotFoundError:
        print("Arquivo não encontrado!") # Caso o arquivo não exista em txt
def criar_arquivo(arquivo):
    criar = open(f'{arquivo}.txt, w+')
    criar.close()


while True:
    pergunta_importar = input("Você deseja importar ficha de um rpg existente (1) ou criar uma (2)?\n --->")
    if pergunta_importar == "1":
        arquivo = input("Digite o nome do arquivo onde está localizado a ficha:\n --->")
        if not arquivo.isalpha():
            print("Favor inserir letras. Caracteres especiais não são permitidos!")
            continue
        else:
            importar_arquivo(arquivo)
            break
    elif pergunta_importar == "2":
        arquivo = input("Crie o nome do arquivo em txt:\n --->")
        if not arquivo.isalpha():
            print("Favor inserir letras. Caracteres especiais não são permitidos!")
            continue
        else:
            criar_arquivo(arquivo)
        break



# Configurando características dadas:


def mudar_vida():
    bancos['Vida'] = input("Digite um novo valor para a vida:")
    print(f"Suas novas configurações são: {bancos}")
def mudar_mana():
    bancos['Mana'] = input("Digite um novo valor para a mana:")
    print(f"Suas novas configurações são: {bancos}")
def mudar_fome():
    bancos['Fome'] = input("Digite um novo valor para a fome:")
    print(f"Suas novas configurações são: {bancos}")
def salvar():
    atualizar = open(f'{arquivo}.txt', "w")
    salvar_dados = list(bancos.values())
    atualizar.write("_".join(salvar_dados))
    return bancos

while True:
    pergunta_nome_personagem = input("Digite o nome do personagem:\n --->").lower()
    pergunta_classe_personagem = input("Digite sua classe (Guerreiro, Assassino ou Mago):\n --->").lower().strip()
    if pergunta_classe_personagem == "guerreiro" or pergunta_classe_personagem == "assassino" or pergunta_classe_personagem == "mago":
        nome = str(pergunta_classe_personagem)
        mana = str(randint(0, 20))
        vida = str(randint(1, 20))
        carisma = str(randint(0, 4))
        fome = str(randint(0, 4))
        arma = ['Espada', 'Adaga', 'Arco', 'Flecha', 'Cajado']
        arma_oficial = str(choices(arma))
        bancos = {'Nome Jogador': pergunta_nome_personagem, 'Classe Jogador': pergunta_classe_personagem,
                  'Mana': mana,
                  'Vida': vida, 'Carisma': carisma, 'Fome': fome, 'Arma': arma_oficial}
        while True:
            decisão = input("Você gostaria de: Mudar a vida (1) // Mudar a mana (2) // Mudar a fome (3) // Salvar a ficha em um txt (4) // Jogar dado (5) // Sair (6)\n--->")
            if decisão == "1":
                mudar_vida()
                continue
            elif decisão == "2":
                mudar_mana()
                continue
            elif decisão == "3":
                mudar_fome()
                continue
            elif decisão == "4":
                salvar()
                print("Arquivo salvo com suceso!")
                continue
            elif decisão == "5":
                while True:
                    try:
                        dado = int(input('Qual o máximo valor do dado?\n --->'))
                        if dado > 25:
                            print('Seu valor está muito alto para o dado')
                        elif dado < 25:
                            dado = randint(1, dado)
                            print(f'O dado parou no número {dado}')
                            break
                    except ValueError:
                        print('Digite corretamente um valor')
                continue
            elif decisão == "6":
                print("Obrigado por participar do jogo!")
                exit()
            elif mana and fome and vida == 0:
                print(f"Atenção!\nVocê possui vida/mana/fome zerada!\nFome = {fome}, Mana = {mana} e Vida = {vida} ")
            else:
                print("Escreva corretamente")
                continue
    else:
        print("As classes só podem ser Guerreiro, Assassino ou Mago. Escreva corretamente!")
        continue


