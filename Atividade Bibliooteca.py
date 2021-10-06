biblioteca = dict()
# Determinando o registro da conta:
while True:
    registro_nome = input("Digite seu login:")
    if "!" in registro_nome or "@" in registro_nome or "." in registro_nome:
        print("Caracteres especiais não são permitidos")
        continue
    elif len(registro_nome) <= 4:
        print("O nome tem que ter no mínimo 5 caracteres")
        continue
    registro_senha = input("Sua senha deve ter até 10 caracteres. Digite sua senha:")
    if "!" in registro_senha or "@" in registro_senha or "." in registro_senha:
        print("Caracteres especiais não são permitidos")
        continue
    elif len(registro_senha) >= 10:
        print("O nome tem que ter até 10 caracteres")
        continue
    elif registro_nome in biblioteca:
        print("Esse usuário já existe")
        break
    else:
        biblioteca[registro_nome] = registro_senha
        print(f"Seu login e senha da(s) sua(s) conta(s) é(são): {biblioteca}")
    # Determinando o que fazer depois de registrar-se:
    stop = input("Desejas Logar ou Sair ou Criar uma nova conta?")
    if stop == "Criar uma nova conta":
        print("Registre uma nova conta")
    elif stop == "Sair":
        exit(stop)
    elif stop == "Logar":
        break
# Determinando o logar após registro:
while True:
    if stop == "Logar":
        login_nome = input("Digite o nome:")
        login_senha = input("Digite a senha:")
        if login_nome == registro_nome and login_senha == registro_senha:
            print("Login efetuado com sucesso!")
            break
        else:
            print("Usuário ou senha incorreto!")
            continue
    else:
        print("Erro!")
        continue




'''Criar um sistema de Login

sistema deve ter as funções:
"Registar"
"Logar"
"Sair"


Usar o seguinte sistema no dicionario.
nome : senha
Key : value 
___~

 - senha 10 caracteres sem e sem caracteres especiais ( OK )

 - Usuario 5 caracteres no minimo e sem caractere especiais ( OK )

 - Se usar "Registrar" e o usuario exista no dicionario, o sistema deve alertar 
que não pode usar o mesmo usuario. (OK)

 - Ao fazer o registro o sistema pergunta se voce quer registrar logar ou sair 
se a senha for incorreta ele deve dizer "Usuario ou senha incorreto!" e pedir para logar novamente (OK)

- Se o usuario e senha for correto e a senha também ele printa que o login  foi efetuado. ( OK )
'''
# Gostei de fazer essa atividade