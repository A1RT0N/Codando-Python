from random import randint as sorteio
from time import sleep as pausa
#Escolha de classe
while True:
    manayest = " "
    vidatotal = 10
    danomax = 10
    vmanayest = 10
    vida = 10
    classe = int(input("Escolha sua classe: Mago = 1 / Guerreiro = 2 --> "))
    if classe == 1:
        classe = "Mago"
        manayest = "Mana"
        vidatotal += 5
        vida += 5
        break
    elif classe == 2:
        classe = "Guerreiro"
        manayest = "Estamina"
        danomax += 5
        break
    else:
        continue
print(f"Sua classe é {classe}. Seu personagem tem {vmanayest} de {manayest}, {vidatotal} de vida e {danomax} de dano máximo")

#Estatísticas do Monstro
vidamaxmonstro = 20
vidamonstro = 20
danobasemonstro = 2
danomonstro = 2
pausa(2)

#Printando o início da batalha e decidindo se o monstro vai atacar ou defender
while True:
    print("=-" * 30)
    print(f"Vida: {vida} // {manayest}: {vmanayest} // Dano máximo: {danomax}")
    print(f"Monstro: Vida: {vidamonstro}")
    escmonstro = sorteio(1, 2)
    acao = int(input("Você encontrou um monstro, o que deseja fazer? 1 - Atacar / 2 - Cura: "))
    print("=-" * 30)

    if escmonstro == 2:
        print("O monstro parece que vai se defender")
    pausa(1)
    print("=-" * 30)

    #Ação de ataque sem mana/estamina
    if vmanayest == 0 and acao == 1:
        print(f"Você não pode atacar pois sua {manayest} acabou, você deve se curar.")
        continue
    #Ação de ataque com mana/estamina
    elif vmanayest > 0 and acao == 1:
        chancepl = sorteio(1, 10)
        dano = sorteio(1, danomax)

        #Defesa do monstro
        if escmonstro == 2:
            dano //= 2

        #Erro de ataque
        if 2 >= chancepl:
            print("Você erra o ataque toscamente!")
            vmanayest -= 1

        #Chance de dano de fogo e gelo do mago
        elif 2 < chancepl:
            if chancepl == 10 and classe == "Mago":
                fogoygelo = sorteio(1, 2)
                if fogoygelo == 1:
                    vidamonstro -= dano + 4
                    print(f"+4 de dano flamejante! Seu dano total é {dano + 4}.")
                elif fogoygelo == 2:
                    vidamonstro -= dano
                    print(f"Dano congelante! O inimigo não vai atacar na próxima rodada. Seu dano total é {dano}")
                    continue
                vmanayest -= 1
            #Dano comum
            else:
                vidamonstro -= dano
                print(f"Você causou {dano} de dano.")
                vmanayest -= 1
    #Ação de cura
    elif acao == 2:
        vida += 2
        vmanayest += 2
        if vmanayest > 10:
            vmanayest = 10
        if vida > vidatotal:
            vida = vidatotal
        if vmanayest > 10 and vida > vidatotal:
            vmanayest = 10
            vida = vidatotal
            print(f"Você já tem vida e {manayest} totalmente cheios.")
            continue
        print(f"Você curou 2 de vida e 2 de {manayest}")
    print("=-" * 30)
    pausa(1)

    #Monstro morto, opção de sair e respawn, com equação de boss
    if vidamonstro <= 0:
        vidamaxmonstro += 10
        danobasemonstro += 2
        danomax += 5
        vidatotal += 5
        vidamonstro = vidamaxmonstro
        vida = vidatotal
        danomonstro = danobasemonstro
        vmanayest = 10
        print(f"Você matou o monstro! Sua vida total e seu dano máximo aumentaram em 5, toda a sua vida e {manayest} foram curadas.")
        sair = input("Você deseja sair agora? Digite 0 pra sim.")
        if sair == "0":
            break
        else:
            pausa(1)
            if (vidamaxmonstro - 10) // 100 == (vidamaxmonstro - 10) / 100:
                vidamonstro = vidamaxmonstro + 150*((vidamaxmonstro - 10) // 100)
                danomonstro = danobasemonstro + 5*(danobasemonstro // 10)
                print(f"Hora do chefe! Tome cuidado para não morrer!")
            continue

    #Ataque do monstro
    if escmonstro == 1:
        print("=-"*30)
        print("O monstro vai atacar.")
        print("=-"*30)
        pausa(1)
        chancems = sorteio(1, 5)
        if chancems == 1:
            print("O monstro errou o ataque.")
            continue
        elif chancems > 1:
            vida -= danomonstro
            print(f"Você tomou {danomonstro} de dano.")
            if vida <= 0:
                pausa(1)
                input("O monstro te ataca violentamente. Esse golpe é tão forte que você é arremessado metros de distância. Suas ultimas palavras são: ")
                break

    #Aumenta 1 de vida no final de cada rodada
    vida += 1
    if vida > vidatotal:
        vida = vidatotal