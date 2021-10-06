# Variáveis globais e locais
# Bully -> binários (Verdadeiro ou Falso)
# Is
# Continua reseta o loop
test = 121 #-> Variável global
def testando():
    #global test #-> Global deixa
    test = 2
# Se eu não colocar o test e printar, vai ignorar, porque o teste dentro do def é uma variável local
testando()
print(test)

# Se eu inverter print com testando() vai dar ruim
# TRATAMENTO DE ERROS E EXCEÇÕES

def divisão():
    while True:
        import webbrowser
        try: #Se não der erro no que tá dentro do try, ele pula o except
            p1 = int(input("Digite o valor de a:"))
            p2 = int(input("Digite o valor de b:"))
            retornar = p1/p2
            return retornar
#       except Exception: -> O Exceptation serve caso aconteça QUALQUER tipo de erro no programa
        except ValueError:
            print("Digite números em vez de letras!")
            continue
        except ZeroDivisionError:
            print("Divisão por zero não existe!")
            continue
        except webbrowser:
            print("Erro!")
            continue

print(divisão())


'''divisão(int(input("Qual o valor de a?"), int(input("Qual o valor de b?")))) -> Assim, se b for zero, dá erro. Como resolver isso?'''
 # except Exceptation: -> Se der qualquer erro, o programa faz tal ação