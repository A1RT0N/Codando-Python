# Quando tá preto, significa que não foi utilizado
from string import punctuation as ponto
def registro():
    while True:
        usuário = input("Digite o nome de seu usuário\n (Min: 5; Max: 10)\n ->")
        senha = input("Digite sua senha\n (Min: 8; Max: 15)\n ->")
        banco = open("banco.txt", "r")
        # Essa técnica do check serve para voltar ao início
        check = False
        for linha in banco.readlines():
            # Relembrando: Split serve para separar em dois elementos a partir de um símbolo
            sep = linha.split("/")
            if sep[0] == usuário:
                check = True
        if check:
            print("Usuário já existe!")
            continue
        if len(usuário) <= 4 or len(usuário) >= 11:
            print("Nome de usuário é maior/menor do que o permitido")
            continue
        if len(senha) <= 7 or len(senha) >= 16:
            print("Senha é maior/menor do que o permitido")
            continue
        check = False
        for p in ponto:
            if p in usuário:
                check = True
        if check:
            print("Caracteres especiais não são permitidos!")
            continue
        banco = open("banco.txt", "a")
        banco.write(f"\n{usuário}/{senha}")
        banco.close()
        break
def logar():
    logusuario = input("Digite seu usuário:")
    logsenha = input("Digite sua senha:")
    banco = open("banco.txt", "r")
    for linha in banco.readlines(): # readlines() transforma tudo de bancos em uma array e o for lê cada linha
        # Sep seria uma array com usuário e senha
        sep = linha.split("/")
        if sep[0] == logusuario:
            if sep[1] == logsenha or sep[1] == logsenha + "\n":
                # O return seria para dar o valor e parar a função na hora, mas não printa
                banco.close()
                return f"Bem vindo, {logusuario}!"
    banco.close()
    return "Usuário/senha incorretos!"

while True:
    acao = input("Escolha se você quer Registrar, Logar ou Sair:")
    if acao == "Registrar":
        registro()
    elif acao == "Logar":
        print(logar())
        break
    elif acao == "Sair":
        exit()
    else:
        print("Digite corretamente!")
        continue






