from random import randint
#Escolha dos personagens:
while True:
    personagem = input("Escolha seu personagem entre mago e guerreiro:")
    if personagem == "mago":
        mana = randint(5,10)
        print(f"Seu personagem tem {mana} de mana")
        print("-=" * 30)
        vida_player = 20
        vida_monstro = 20
        break
    elif personagem == "guerreiro":
        estamina = randint(5,15)
        print(f"Seu personagem tem {estamina} de estamina")
        print("-=" * 30)
        vida_player = 20
        vida_monstro = 20
        break
# História ensinando o jogo:
while True:
    atacar = input("Você foi abandonado em uma ilha após uma grande guerra contra seus iguais e não se lembra de nada. Após adentrar na ilha, você percebe a existência de seres estranhos (não, você não está sob efeito de narguilhes). Você percebe que um deles te persegue e precisa se defender, para isso selecione Atacar:")
    if atacar == "Atacar" and personagem == "guerreiro":
        vida_monstro -= 4
        print(f"O monstro está com {vida_monstro - 4} de vida e você tem {estamina - 2} de estamina e {vida_player} de vida. Agora é a vez dele atacar")
        print("-=" * 30)
        vida_player = 20
        break
    elif atacar == "Atacar" and personagem == "mago":
        print(f"O monstro está com {vida_monstro - 4} de vida e você tem {mana - 2} de mana e {vida_player} de vida. Agora é a vez dele atacar")
        print("-=" * 30)
        break
while True:
        defesa = input("Para você não sofrer dano do monstro, você deverá se defender, gastando 2 de estamina. Selecione Defesa:")
        if defesa == "Defesa" and personagem == "guerreiro":
            print(f"Você esquivou, mas agora está com {estamina - 2} de estamina")
            estamina -= 2
            print("Você também pode descansar, recuperando de 1 a 7 de estamina ou curar, gastando dois de estamina e recuperando 3 de vida")
            print("-=" * 30)
            break
        elif defesa == "Defesa" and personagem == "mago":
            print(f"Você esquivou, mas agora está com {mana - 2} de mana")
            mana -= 2
            print("Você também pode descansar, recuperando de 1 a 7 de estamina ou curar, gastando dois de estamina e recuperando 3 de vida")
            print("-=" * 30)
            break
turno = int(input("Agora você percebeu como esses seres malignos são, vamos ao jogo para valer! Escolha o turno 1 para sofrer, quer dizer, jogar:"))
if turno == 1:
    #Eu estou considerando o dano do player igual a zero como forma de ´´defesa`` aleatória do monstro
    dano_player = randint(0,5)
    vida_player = 20
    dano_monstro = randint(1,2)
    vida_monstro = 20
    descansar = randint(1,7)
    chanceespecial = randint(0,10)
while turno > 0:
    #vez_do_player
    ação_player = input("Um monstro se espreita pelas sombras da ilha. Mate-o! (Caso queira viver) Selecione uma ação (Atacar ou Descansar ou Curar ou Defender):")
    if ação_player == "Atacar" and personagem == "mago":
        mana -= 2
        vida_monstro -= dano_player
        print(f"O monstro está com {vida_monstro - dano_player} de vida e você está com {mana} de mana")
        vida_player -= dano_monstro
        print(f"O monstro te atacou, agora você está com {vida_player - dano_monstro} de vida")
        print("-=" * 30)
        continue
    #Configurando o especial do mago:
    elif ação_player == "Atacar" and personagem == "mago":
            print("Você usou seu especial e congelou o monstro. Ele não consegue se mexer!")
            ataqueespecial = input("Como o monstro nada pode fazer, selecione 'Atacar' para destruí-lo:")
            if ataqueespecial == "Atacar":
                print(f"O monstro está com {vida_monstro - dano_player} de vida ")
            if vida_monstro == 0:
                break
    elif ação_player == "Atacar" and personagem == "guerreiro":
        estamina -= 2
        print(f"O monstro está com {vida_monstro - dano_player} de vida e você está com {estamina} de estamina")
        vida_monstro -= dano_player
        print(f"O monstro te perseguiu, agora você está com {vida_player - dano_monstro} de vida")
        vida_player -= dano_monstro
        print("-=" * 30)
    elif ação_player == "Descansar" and personagem == "guerreiro":
        print(f"Você descansou e está com {estamina + descansar} de estamina")
        estamina += descansar
        vida_player -= dano_monstro
        print(f"O monstro correu atrás de você, agora você está com {vida_player - dano_monstro} de vida")
        print("+" * 60)
    elif ação_player == "Descansar" and personagem == "mago":
        print(f"Você descansou e está com {mana + descansar} de mana")
        mana += descansar
        vida_player -= dano_monstro
        print(f"O monstro correu atrás de você, agora você está com {vida_player - dano_monstro} de vida")
        print("+" * 60)
    elif ação_player == "Curar" and personagem == "guerreiro":
        print(f"Você se curou e está com {vida_player + 3} de vida e está com {estamina - 2} de estamina")
        vida_player += 3
        estamina -= 2
        vida_player -= dano_monstro
        print(f"O monstro correu atrás de você, agora você está com {vida_player - dano_monstro} de vida")
        print("+" * 60)
    elif ação_player == "Curar" and personagem == "mago":
        print(f"Você se curou e está com {vida_player + 3} de vida e está com {mana - 2} de mana")
        vida_player += 3
        mana -= 2
        vida_player -= dano_monstro
        print(f"O monstro correu atrás de você, agora você está com {vida_player - dano_monstro} de vida")
        print("+" * 60)
    elif ação_player == "Defender" and personagem == "mago":
        print(f"Você se defendeu do monstro e está com {mana - 2} de mana ")
        mana -= 2
    elif ação_player == "Defender" and personagem == "guerreiro":
        print(f"Você se defendeu do monstro e está com {estamina - 2} de mana ")
        estamina -= 2
        continue
    #Caso a mana/estamina acabe
    if personagem == "mago" and mana <= 0:
        falta = input("Você está sem mana. Selecione 'Descansar' para recuperar:")
        if falta == "Descansar":
            print(f"Você descansou e está com {mana + descansar} de mana")
            mana += descansar
            print(f"O monstro correu atrás de você, agora você está com {vida_player - dano_monstro} de vida")
            vida_player -= dano_monstro
            print("+" * 60)
    if personagem == "guerreiro" and estamina <= 0:
        falta1 = input("Você está sem estamina. Selecione 'Descansar' para recuperar:")
        if falta1 == "Descansar":
            print(f"Você descansou e está com {estamina + descansar} de mana")
            estamina += descansar
            print(f"O monstro correu atrás de você, agora você está com {vida_player - dano_monstro} de vida")
            vida_player -= dano_monstro
            print("+" * 60)
    #Fazendo a parada para continuar o jogo:
    if vida_monstro <= 0:
        sair = input("Você pode sair do jogo agora, mas se quer continuar, você recuperará toda sua vida e será mais poderoso, assim como os monstros. Deseja continuar? Escreva 'Sim' ou 'Não':")
        if sair == "Não":
            certeza = input("Esse jogo é um caminho sem volta. As suas conquistas não serão salvas. Tem certeza que deseja sair dessa ilha? Digite 'Sim' ou 'Não':")
            if certeza == "Sim":
                "Ainda bem, seu fraco. Até um outro dia!"
                break
            elif certeza == "Não":
                print("Ainda bem, gracinha!")
                print("-=" * 30)
                continue
        elif sair == "Sim":
            print("Vamos ao jogo!")
            print("-=" * 30)
            vida_monstro = 20
            vida_monstro += 10
            dano_monstro += 3
            dano_player += 5
            vida_player += 5
            if personagem == "guerreiro":
                estamina = estamina
                estamina += 1
            if personagem == "mago":
                mana = mana
                mana += 1
            continue
        #Momento de enfrentar o boss
        if vida_player >= 60:
            vida_monstro = 140
            dano_monstro = 20
            print("A ajuda está chegando, mas parece que algo terrível está por perto. Chegou a hora de enfrentar o boss! Vamos lá!!!")
            continue
    if vida_player <= 0:
        input("Você é arremessado violentamente para longe! Você vê apenas o sol raiando nas águas da ilha. Suas últimas palavras são:")
        break

# REGRAS:
#escolher mago ou guerreiro (OK)
#se escolher guerreiro vai ter uma barra de estamina de 5 a 15 (OK)
#se escolher mago vai ter uma barra de mana de 5 a 10 (que equivale a estamina) (OK)
#monstro começa com 20 de vida e toda vez que você mata um monstro você tem a opção de sair do jogo, porém se você quiser continuar o jogo você recupera toda sua vida e o próximo monstro terá mais 10 de vida, e mais 3 de ataque do que o anterior e você terá mais 5 de ataque e mais 5 de vida (PESADO)
#O jogador tem 4 opções: Atacar ( 1 a 5 de dano, e gasta 2 de estamina), defender (mesma mecânica do ultimo, e gasta 2 de estamina), curar (mesma mecânica) ou descansar (recupera de 1 a 7 de estamina) (PESADO)
#o monstro escolhe aleatoriamente entre atacar dando 2 de dano ou se defender no qual ele se comporta igual ao jogador (OK), exceto que ele recebe só um terço do dano (AH PQP ME MAMA)
#O dano do mago tem a chance de 1 em 10 de ter um efeito magico de gelo no qual o gelo congela o monstro por um turno (PESADO DEMAIS)
#A cada 10 monstros vai ter 1 chefão (Fácil)
#O chefão tem bem mais vida e mais dano (Fácil)
#por turno o jogador recupera 1 de estamina (Fácil)
