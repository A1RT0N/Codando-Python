'''
-> Crie um programa que transforme qualquer numero romano em um numero inteiro
Exemplo: XVIII sera transformado automaticamente no numero 18
O I corresponde ao número 1
O V corresponde ao numero ao 5
O X corresponde ao numero 10
O L corresponde ao numero 50
O C corresponde ao numero 100
O D corresponde ao numero 500
O M corresponde ao numero 1000
'''

'''def romano_add():
romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
Ex: CDXL = 440 --> D>C>L>X --> 440 = (500 -100) + (50-10) 
Ex 2: DCLXIII = 663 = 500 + 100 + 10 + 1 + 1 + 1
'''


def romano_a_add(romano):
    try:
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        numero = 0
        for i in range(len(romano)): # Ele pega cada número inteiro no intervalo de 0 até o tamanho do input romano para servir como index do input (que é uma string e, portanto, tem index. Ex: joao = 'XV' -> print(joao[1])
            if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]: # Usamos esse if quando o algarismo da frente for maior que o de trás. Como o index de qualquer elemento do romano não pode ser < 0, logo temos que colocar i > 0. Obs: não podemos somar i com algum número natural em romano[] pois se o elmento tiver dois index (Ex: XV), ele vai procurar o index do k = 2 quando k for 1, o que não existe!
                numero += romanos[romano[i]] - 3 * romanos[romano[i - 1]]
            else: # Esse else é pra quando i for igual a 1 ou quando o número da frente for menor que o de trás
                numero += romanos[romano[i]]
        return numero
    except KeyError:
        print("Digite adequadamente!")

print(romano_a_add(input("Digite um número em Romano (obedeça as regras):\n --->")))





def romanToInt(romano_user):
    romanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanDic_compostos = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    numero = 0
    for k in range(len(romano_user)):
        if k> 0:
            compostos = str(romano_user[k-1]) + str(romano_user[k])
            print(compostos)
            if compostos in romanDic_compostos.keys():
                numero += romanDic_compostos[romano_user[k]]
            else:
                print("Aff")
        else:
            numero += romanDic[romano_user[k]]
    print(numero)


'''https://programmerclick.com/article/11371855762/
'''
'''romanToInt('XI')'''