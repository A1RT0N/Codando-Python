def adicionar():
    name = input("Nome do produto? ---> ")
    id = input("id do produto? ---> ")
    qnt = input("Quantidade do produto? ---> ")
    pr = input("Preço do produto? ---> ")
    banco[name] = [id, qnt, pr]
    atualizar_db()

def deletar():
    produto = input("Produto a ser deletado ---> ")
    try:
        del banco[produto]
        atualizar_db()
    except KeyError:
        pass
def atualizar_db():
    atualizar = open("data.txt", "w")
    for keyss, valuess in banco.items():
        info = "_".join(valuess)
        atualizar.write(f"{keyss}_{info}\n")
    atualizar.close()
def capturar_db():
    armazem = dict()
    db = open("data.txt", "r")
    captura1 = db.read()
    captura1 = captura1.split("\n")
    for elemento in captura1:
        if len(elemento) != 0:
            capsula = elemento.split("_")
            armazem[capsula[0]] = [capsula[1], capsula[2], capsula[3]]
    return armazem
def ver_produtos():
    for elementos in banco.keys():
        print(elementos)

def acessar_produtos():
    produto = input("Produto a ser acessado ---> ")
    for elemento in banco.keys():
        if produto == elemento:
            print(
                f'O produto {elemento} possui {banco[elemento][1]} unidades, o id {banco[elemento][0]} e custa {banco[elemento][2]} reais!')


while True:
    banco = capturar_db()
    # Ver se um produto tem um valor menor ou igual a 3 exemplares
    for keys, values in banco.items():
        num = int(values[1])
        if num <= 3:
            print(f"O produto {keys} tem {values[1]} exemplares!")

    print("-=" * 30)
    querer = input(
        "Adicionar (1) // Ver produtos (2) // Deletar produto (3) // Acessar produto (4) // sair (5) \n ---> ")

    if querer == "1":
        adicionar()

    elif querer == "2":
        print("-=" * 30)
        ver_produtos()

    elif querer == "3":
        deletar()

    elif querer == "4":
        acessar_produtos()

    elif querer == "5":
        break