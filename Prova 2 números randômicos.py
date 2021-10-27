from random import randint
pontuação = 0 # Criando uma faixa de pontuação que será contabilizada no sistema
numero_aleatorio = randint(1, 10)
while True:
    pergunta = input("Digite o número inteiro de 1 a 10. Se deseja sair, escreva ´´sair``\n --->").strip().lower()
    if type(pergunta) == str and pergunta.isnumeric() == False: # Analisando se o input foi uma string
        if pergunta.lower() == "sair":
            print(f"Obrigado por participar! Sua pontuação é: {pontuação}")
            break
        else:
            print("Digite corretamente!") # Caso o usuário digite outra palavra sem ser ´´sair``
    elif type(pergunta) == str and pergunta.isalnum(): # Analisando se o input foi um int
        if int(pergunta) == numero_aleatorio:
            print("Parabéns, você acertou! Você ganhou mais um ponto. Vamos para a próxima rodada")
            pontuação += 1
            numero_aleatorio = randint(1,10) # Alterando o número aleatório inicial
        elif int(pergunta) < numero_aleatorio:
            print('O número que você digitou é menor que o escolhido. Tente novamente!')
        elif int(pergunta) > numero_aleatorio:
            print('O número que você digitou é maior que o escolhido. Tente novamente!')
        elif int(pergunta) >= 11:
            print("Os números devem estar no intervalo de 1 a 10. Tente novamente!") # Caso o usuário digite um número maior que 10

