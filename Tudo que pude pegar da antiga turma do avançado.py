def ad(a):
    func = list()
    for tr in range(1, N+1):
        k = a
        print(len(k))
        print(len(a))
        if len(k) > len(a):
            k.pop()
            print('a')
        if not tr in a:
            k.append(tr)
        k.sort()
        func.append(k)
    return func
print(ad([1]))

from threading import Thread

# Chamar função Thread sem parametro
Thread(target=nome).start()

# Chamar função Thread com um parametro só
Thread(target=nome, args=[parametro unico,]).start()

# Chamar função Thread com mais parametros
Thread(target=nome da func, args=[parametro 1, parametro 2]).start()

# existem duas raças, vermelha e verde
# a única forma de se alimentar é através de uma unidade de comida
# para sobreviver a raça verde precisa comer uma unidade de comida e para reproduzir, duas
# para a raça vermelha sobreviver, ela precisa comer uma unidade de comida, e para reproduzir, uma e meia
# se duas pessoas da mesma espécie pegarem a mesma comida, elas dividem a comida no meio
# se duas pessoas de espécies diferentes tentarem comer o mesmo alimento, alguma delas é escolhida aleatoriamente
# a cada dois dias, alguém da raça vermelha morre, a cada 3 dias alguém da raça verde morre
# a cada dia q passa todos os sobreviventes ganham uma geração
# quantos de cada raça morreram, quantos foram gerados e a porcentagem de um sobre o outro



'''
dica: a velocidade das criaturas pode ser definida pela quantidade de bloquinhos que ela pode andar por turno
dica 2: regra de movimentação as criaturas sempre vão andar atras da comidinha que estiver mais perto
dica 3: vcs podem criar uma matriz de 20 por 20 e fazer a movimentação baseada na matriz (Tipo batalha naval)
dica 4: é mais fácil fazer as coordenadas x e y por arrays
'''

class ficha:
    def __init__(self):

        cls = ["Mago", "Guerreiro", "Assasino", "Curandeiro"]
        magia = ["Fogo", "Agua", "Terra", "Ar", "Luz", "Escuridão"]
        from random import randint, choice
        if input("Import? ---> S/N ") == "S":
            while True:
                try:
                    final = self.tratamento(input("Nome da ficha ---> "))
                    final.append("")
                    for b, a in enumerate(final):
                        if len(a) == 0:
                            del final[b]
                    final.pop()
                    print(final)
                    break
                except:
                    print("A ficha não existe!")
                    continue


        # Criação de ficha
        else:
            self.nome = input("Nome do personagem ---> ")
            self.vida = randint(0, 20)
            self.carisma = randint(0, 20)
            self.strong = randint(0, 20)

            while True:
                self.classe = input(f"Qual sera sua classe? \n{cls}\n---> ")

                if not self.classe in cls:
                    print("Essa opção não existe...")
                    continue
                else:
                    if self.classe == "Mago":
                        self.item = ["Cajado"]
                        self.magia = choice(magia)
                        self.mana = randint(0, 20)


                    elif self.classe == "Assasino":
                        self.item = ["Adagas"]
                        self.magia = ""
                        self.mana = ""

                    elif self.classe == "Guerreiro":
                        self.item = ["Espada"]
                        self.magia = ""
                        self.mana = ""

                    elif self.classe == "Curandeiro":
                        self.item = ["Cetro"]
                        self.magia = "Curar"
                        self.mana = randint(0, 20)
                    break
            while True:
                querer = input("Salvar ficha (1), Sair (2) ---> ")
                if querer == "1":
                    self.salvar()
                elif querer == "2":
                    break

    def salvar(self):
        with open(f"{self.nome}.txt","w+") as fix:
            fix.write(f"{self.vida}\n{self.carisma}\n{self.strong}\n{self.classe}\n{self.item}\n")
            if self.magia != "" and self.mana != "":
                fix.write(f"{self.magia}\n{self.mana}\n\n")
            fix.close()

    def tratamento(self,nami):
        nana = open(f"{nami}.txt", "r")
        tratar = nana.read()
        tratar2 = tratar.split("\n")
        nana.close()
        del tratar
        return tratar2


class dog:
    def __init__(self, name, race, age):
        from time import sleep
        self.name = name
        self.race = race
        self.age = age
        self.carinho = 20
        while True:
            car = input("Dar carinho? S/N ---> ")
            if car == "N":
                self.carinho -= 1
            elif car == "S":
                if self.carinho >= 20:
                    break
                self.dar_carinho()
            sleep(2)

    def dar_carinho(self):
        self.carinho += 1


class humano(dog):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        super().__init__(name="fiaDaPuta", race='ariano', age=18)
        print(self.carinho)


humano("Odeio", 12)



# TUDO QUE TÁ NO CLASS.PY:
from array import array
from string import ascii_lowercase as alfabeto
from random import choice


class Cripto:
    def __init__(self, word=str(), la_chave=True):
        if la_chave == True:
            self.word = word
            self.chave = True
            self.criptografar()
        else:
            self.word = word
            self.chave = la_chave
            self.criptografar()

    def criptografar(self):
        self.gerar_array()
        self.gerar_alfabeto()

    # Transforma a frase e a chave em listas com as index correspondentes aos elementos da lista alfabeto
    # Exemplo "a" = 0 // "b" = 1 // "c" = 2
    def gerar_array(self):
        if self.chave == True:
            key = self.random_key(len(self.word))
        else:
            key = self.chave
        array_key = [alfabeto.index(letra) for letra in key]
        word_key = [alfabeto.index(letter) for letter in self.word]
        self.frase = array_key
        self.chave = word_key
        print(self.chave)

    # Gera uma chave aleatoria
    @staticmethod
    def random_key(tamanho):
        chave = list()
        for _ in range(0, tamanho):
            chave.append(choice(alfabeto))
        return chave

    # Gera o alfabeto de vigenere
    def gerar_alfabeto(self):
        final = list()
        contador = 0
        # Gerando cifra de vigenere para cada letra da frase
        for num in self.frase:
            alpha = list(alfabeto[num:])
            for falta in range(0, 26 - len(alpha)):
                alpha.append(alfabeto[falta])
            final.append(alpha[self.chave[contador]])
            contador += 1
        print(final)


Cripto("pato", "pata")




todos = dict()
verdes = 10


class Verde:
    def __init__(self):
        self.gerac = 3

    def saber_gerac(self):
        return self.gerac


for seres in range(1, verdes+1):
    todos[f"verde-{seres}"] = Verde()

gerados = 2


for batata in range(len(todos), len(todos) + gerados+1):
    todos[f"verde-{batata}"] = Verde()

pato = [array for array in todos.items()]
print(pato)
for verdeee, papo in pato:
        if papo.saber_gerac() == 3:
            del todos[verdeee]
del pato

print(todos)





from threading import Thread
class p:
    def __init__(self):
        self.pato = 0
        pato = Thread(target=self.mudar)
        pato.start()
        pato.join()
        print(self.retorno())

    def retorno(self):
        return self.pato

    def mudar(self):
        while self.pato != 60000:
            self.pato += 1

p()





from selenium.webdriver import Firefox


class Navegador:
    def __init__(self):
        self.luffy = Firefox(executable_path="geckodriver.exe")
        self.site("https://youtube.com")

    def site(self, url):
        self.luffy.get(url)


Navegador()





import socket as ss
from threading import Thread


# tipo ip
# qual protocolo
class Server:
    def __init__(self):
        self.server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.server.bind(("192.168.15.71", 52577))
        self.server.listen(1)
        while True:
            cliente, dress = self.server.accept()
            print("Conectado!")
            Thread(target=self.enviar, args=[cliente, ]).start()
            Thread(target=self.receber, args=[cliente, ]).start()


    @staticmethod
    def enviar(cliente):
        while True:
            msg = input()
            cliente.send(bytes(msg, "utf-8"))

    @staticmethod
    def receber(obj):
        while True:
            receber = obj.recv(2048)
            if receber:
                print(f"\n{receber.decode('utf-8')}")


Server()
import socket as ss
from threading import Thread
from time import sleep





class Client:
    def __init__(self):
        try:
            self.client = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
            self.client.bind((ss.gethostname(), 32323))
            self.client.connect(("179.186.166.107", 47678))
            self.viadagem()
            # Enviar
            Thread(target=self.send_menssage).start()
            # Receber
            self.get_menssage()
        except ConnectionRefusedError:
            print("Erro!")

    @staticmethod
    def viadagem():
        print("conectei!")
        print("Iniciando", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print(".", end="")
        print("\n")

    def send_menssage(self):
        while True:
            msg = input()
            self.client.send(bytes(msg, "utf-8"))

    def get_menssage(self):
        while True:
            receber = self.client.recv(2048)
            if receber:
                print(f'\n{receber.decode("utf-8")}')


Client()

# Servidor do chat online
import socket as ss
from threading import Thread
from pyautogui import alert


class Servidor:
    def __init__(self):
        self.conect = dict()
        self.server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.server.bind((ss.gethostname(), 52765))
        self.server.listen(5)
        Thread(target=self.testando).start()
        self.accept()

    def accept(self):
        while True:
            obj_client, dress = self.server.accept()
            Thread(target=self.pegando_nome, args=[obj_client, dress[0]]).start()

    def pegando_nome(self, ocliente, end):
        while True:
            nome = ocliente.recv(1024)
            if nome:
                nome_do_cliente = nome.decode("utf-8")
                self.conect[nome_do_cliente] = [ocliente, end]
                break
        print(self.conect)

    def testando(self):
        while True:
            if len(self.conect) != 0:
                try:
                    for key_conectados, conectados in self.conect.items():
                        try:
                            conectados[0].send(bytes("\n", "utf-8"))

                        except Exception:
                            del self.conect[key_conectados]
                            alert(f"O cliente {key_conectados} foi desconectado!")
                except RuntimeError:
                    continue


Servidor()

# Cliente do chat online
import socket as ss
from random import randint


class Clientt:
    def __init__(self):
        self.cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.cliente.bind((ss.gethostname(), randint(50000, 60000)))
        self.cliente.connect((ss.gethostname(), 52765))
        self.cliente.send(bytes(input("Coloque seu nome ---> "), "utf-8"))


Clientt()






abc = ["pato", "jesus cristo 2", "vinicius eleuterio", "pinguin é um gostoso"]

arrayy = [len(elementos) for elementos in abc if len(elementos) != 4 if elementos == "jesus cristo 2"]
print(arrayy)

import socket as ss
from random import randint


class Clientt:
    def __init__(self):
        self.cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.cliente.bind((ss.gethostname(), randint(50000, 60000)))
        self.cliente.connect((ss.gethostname(), 52765))

        self.my_name = input("Coloque seu nome ---> ")
        self.cliente.send(bytes(self.my_name, "utf-8"))

        while True:
            querer = input("Conectar (1) // Ver conexões (2) // Sair (3)\n---> ")
            if querer == "1":
                pass
            elif querer == "2":
                conectados = self.ver_conexoes()
                print("-=" * 30)
                if len(conectados) == 0:
                    print("Apenas você está online!")
                else:
                    print(conectados)
                print("-=" * 30)
            elif querer == "3":
                self.cliente.close()
                break

    def ver_conexoes(self):
        self.cliente.send(bytes("envie_dicionario", "utf-8"))
        while True:
            pato = self.cliente.recv(1024)
            if pato:
                menssagem = pato.decode("utf-8")
                if menssagem != "$" and "\n%" in menssagem:
                    tratamento = menssagem.split("\n%")[1]
                    try:
                        retorno = tratamento.split("\n")
                        retorno.remove(self.my_name)
                        return retorno
                    except ValueError:
                        pass


Clientt()








import socket as ss
from threading import Thread
from pyautogui import alert
from time import sleep


class Servidor:
    def __init__(self):
        self.conect = dict()
        self.server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.server.bind((ss.gethostname(), 52765))
        self.server.listen(5)

        Thread(target=self.testando).start()

        while True:
            obj_client, dress = self.server.accept()
            nome_do_cliente = self.receber(obj_client)
            self.conect[nome_do_cliente] = [obj_client, dress[0]]
            Thread(target=self.menu_do_server, args=[obj_client, ]).start()

    @staticmethod
    def receber(qm):
        while True:
            try:
                nome = qm.recv(1024)
            except ConnectionResetError:
                break
            except ConnectionAbortedError:
                break
            if nome:
                return nome.decode("utf-8")

    def testando(self):
        while True:
            if len(self.conect) != 0:
                try:
                    for key_conectados, conectados in self.conect.items():
                        try:
                            conectados[0].send(bytes("$", "utf-8"))
                            sleep(1.5)
                            print(f"{len(self.conect)} clientes estão conectadas em mim!")
                        except Exception:
                            del self.conect[key_conectados]
                            alert(f"O cliente {key_conectados} foi desconectado!")
                except RuntimeError:
                    continue
            else:
                print("Não há clientes conectados!")
                sleep(1.5)

    def menu_do_server(self, cliente):
        while True:
            ordem = self.receber(cliente)

            if ordem == "envie_dicionario":
                clientes = "\n".join([a for a in self.conect.keys()])
                cliente.send(bytes(f"\n%{clientes}", "utf-8"))

            if ordem == "chatzinho":
                pass

Servidor()


# PyautoGui -> Interface

