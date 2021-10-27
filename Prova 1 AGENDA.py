from string import punctuation

# Ao longo do código, usarei .strip() e .lower() com objetivo de reduzir os erros de digitação do usuário

def registrar():
    while True:
        usuario_registro_nome = input("Digite o nome do novo usuário (Mínimo: 5 caracteres; Máximo: 15 caracteres)\n --->").strip().lower()
        usuario_registro_senha = input("Digite sua nova senha (Mínimo: 5 caracteres; Máximo: 15 caracteres)\n --->").strip().lower()
        banco_usuario = open("Banco de dados - usuário.txt", "r")
        check_registrar = False  # Utilizarei a técnica do check como forma tornar mais eficiente o código - nesse caso, caso o check seja igual a False, o programa voltará ao início do loop
        for linha in banco_usuario.readlines(): # Analisando cada linha e armazenando em uma array com um elemento com todas as linhas
            separar = linha.split("/") # Separando em vários elementos da array com base no termo ´´/``
            if separar[0] == usuario_registro_nome:
                check_registrar = True
        if check_registrar == True: # Caso o usuário já exista
            print("Usuário já existente! Tente novamente")
            continue
        if len(usuario_registro_nome) <= 4 or len(usuario_registro_senha) <= 4:
            print("O mínimo é 5 caracteres para senha e nome! Tente novamente")
            continue
        if len(usuario_registro_nome) >= 16 or len(usuario_registro_senha) >= 16:
            print("O máximo é 15 caracteres para senha e nome! Tente novamente")
            continue
        for letra in punctuation:
            if letra in usuario_registro_nome or letra in usuario_registro_senha:  # Caso o usuário digite letras pretencentes ao punctuation
                print("Caracteres especiais não são permitidos! Tente novamente")
                continue
        banco_usuario = open("Banco de dados - usuário.txt", "a")
        banco_usuario.write(f"\n{usuario_registro_nome}/{usuario_registro_senha}") # Escrevendo no banco
        banco_usuario.close()
        break

def login():
    while True:
        banco_usuario = open("Banco de dados - usuário.txt", "r")
        usuario_login_nome = input("Digite o nome (Mínimo: 5 caracteres; Máximo: 15 caracteres)\n --->")
        usuario_login_senha = input("Digite a senha (Mínimo: 5 caracteres; Máximo: 15 caracteres)\n --->")
        check_login = False
        for linha in banco_usuario.readlines(): # Utilizando a mesma técnica usada em registrar()
            separar = linha.split("/")
            if separar[0] == usuario_login_nome:
                check_login = True
                if separar[1] == usuario_login_senha or separar[1] == usuario_login_senha + "\n": # Nesse caso, diferentemente do usado em registrar(), analisa-se se está na primeira linha (não tem /n - enter) ou outras linhas (que tem /n)
                    check_login = True
        if check_login == True:
            print(f"Bem vindo, {usuario_login_nome}!")
            break
        else:
            print("Nome e/ou senha inválidos! Tente novamente")
            continue

def ler():
    nome_arquivo_ler = input("Digite o nome do seu arquivo (equivale ao seu nome do login):").strip()
    try: # Utilizando try para caso o arquivo não exista para o respectivo usuário e precisa criar um novo
        arquivo = open(f"Banco de dados - anotações - {nome_arquivo_ler}.txt", "r")
    except FileNotFoundError:
        print("Você não possui um arquivo .txt\nVamos criar um novo")
        arquivo = open(f"Banco de dados - anotações - {nome_arquivo_ler}.txt", "w+")
    print(f"Veja suas anotações:\n{arquivo.readlines()}")


def escrevendo(): # Mesma lógica do ler()
    nome_arquivo_escrever = input("Digite o nome do seu arquivo (equivale ao seu nome do login):").strip()
    try:
        arquivo = open(f"Banco de dados - anotações - {nome_arquivo_escrever}.txt", "a")
    except FileNotFoundError:
        arquivo = open(f"Banco de dados - anotações - {nome_arquivo_escrever}.txt", "w+")
    print("Digite suas novas anotações")
    arquivo.write(f'-> {input("Escreva algo: ")}\n')

while True:
    pergunta_inicial_logar_registrar = input("Bem vindo(a) à sua Agenda! Você gostaria de registrar (1) ou logar (2)?\n --->").strip()
    if pergunta_inicial_logar_registrar == "1":
        registrar()
        continue
    elif pergunta_inicial_logar_registrar == "2":
        login()
        pergunta_agenda = input("Digite ´´1`` se deseja ler ou digite ´´2`` se deseja escrever algo nela ou ´´3`` se desejar sair\n --->").strip()
        if pergunta_agenda == "1":
            ler()
            pergunta_escrever = input("Você deseja escrever algo nesse arquivo (1) ou finalizar ou voltar diretamente à tela inicial (2)?").strip()
            # Caso o usuário queira, após ler o arquivo, escrever novamente e sair do código
            if pergunta_escrever == "1":
                escrevendo()
                print("Obrigado por participar!")
                break
            elif pergunta_escrever == "2":
                continue # Usado apenas para voltar à tela inicial
            else:
                print("Digite corretamente!") # Caso o usuário escreva algo indevido
                continue
        elif pergunta_agenda == "2":
            escrevendo()
            pergunta_ler = input("Você deseja escrever nesse arquivo (1) ou finalizar ou voltar diretamente à tela inicial (2)?").strip()
            if pergunta_ler == "1":
                ler()
                print("Volte sempre!")
                break
            elif pergunta_ler == "2":
                continue
            else:
                print("Digite corretamente!")
                continue
        elif pergunta_agenda == "3":
            print("Obrigado por participar") # Finalizando o código
            break
        else:
            print("Digite corretamente!")
            continue
    else:
        print("Digite corretamente!")
        continue





