# Absolute path: colocar \\ para achar arquivo.

# O que tá dentro do def não se relaciona com o que está fora do def, a não ser que tenha o global var

# Para dar parágrafo: \n

conta = dict()
usuarios = []
def registrar():
    while True:
        nome = input("Insira o nome do usuário:")
        if nome in usuarios:
            print("Esse usuário já existe. Coloque outro")
            continue
        else:
            break
    while True:
        lock = input("Insira a senha do seu usuário:")
        if len(lock) < 10:
            print(f"Sua senha deve conter mais de 10 caracteres. Faltam {10 - len(lock)} caracteres")
            continue
        elif len(lock) > 17:
            print(f"Sua senha deve conter menos de 17 caracteres. Faltam {len(lock) - 17} caracteres")
            continue
        else:
            conta[nome] = lock
            usuarios.append(nome)
            break

def logar():
    while True:
        nome1 = input("Insira o nome do usuário para logar:")
        if nome1 not in conta.keys():
            print("Essa conta não está disponível")
        else:
            break
    while True:
        lock1 = input("Insira sua senha:")
        if lock1 not in conta[nome1]:
            print("Essa conta não existe!")
        else:
            print("Você logou com sucesso!")
            break

while True:
    choose = input("Escolhe entre 'Registrar', 'Logar' ou 'Sair':")
    if choose == "Registrar":
        registrar()
    elif choose == "Logar":
        logar()
    elif choose == "Sair":
        exit()
        print(conta)
        print(usuarios)
    else:
        print("Digite corretamente!")

