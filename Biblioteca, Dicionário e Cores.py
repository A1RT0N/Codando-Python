#() = tuple() = tuplas
#[] = list() = array
#{} = dict() = dictionary
# Dicionário é parecido com array, mas eu posso nomear as index
# A gente nomeia index - cerveja, Cachaça,etc
# Sendo assim, não faz sentido ter insert, já que já nomeamos os index

pinga = {"Cerveja": ["Skol","RS10.00"], "Cachaça": ["Valente","RS8.00"], "Foguete": ["Foguete do mal", "RS1000.00"]}

pinga["Esportes"] = "Futbol", "Vôlei"
print(f"Ao adicionar Esportes:{pinga}")
print(pinga["Cerveja"][0])


# Keys mostra os index nomeados (usei o len - conta quantos tem - só pra aplicação):
'''abc = len(pinga.keys())
print(abc)'''
# Values mostra os elementos dentro dos indexes nomeados:
'''abc = pinga.values()
print(abc)'''
# Itens mostra tudo no dicionário:
'''abc = pinga.items()
print(abc)'''
'''pinga["Linguiça"] = ["Linguiça´s Ramalho", 0.5]
print(pinga)'''

'''for key, value in pinga.items():
    print(f"O {value} está na key {key}!")'''


# No dicionário, NÃO existe a função enumerate. Logo, precisamos usar:
'''
for k, v in dict.items():
    print(f"{k} = {v}")'''


# Explicação do monitor:
# Kyes, Valeus, Itens e []:
'''
-> Keys é o nome que você dá para a array dentro, tipo a = {"*key1*":[1,2,3], "*key2*":[2,4,5]}
-> Values é o que você nomeia:a = {"key1":*[1,2,3]*, "key2":*[2,4,5]*}
Caso eu queira retornar o 2 dentro da key1, eu faço:
a['key2'][0]
-> Itens é a junção das keys e items
Exemplo:
{*"key1":[1,2,3]*, "key2":[2,4,5]}
'''

# Outros modos de uso:
#print(pinga["Cachaça"])
'''valorstring = float(pinga["Cachaça"][1].split("RS")[1])
print(valorstring)'''

brasil = []
estado_1 = {'uf': "RJ", 'nome': 'Rio de Janeirp'}
brasil.append(estado_1)
print(brasil)

# Biblioteca:
'''
Para ver as bibliotecas instaladas já no Pycharm, é só colocar import e apertar Crtl + Espaço
-> Bibliotecas instaldas: https://docs.python.org/3/library/index.html

Importação de bibliotecas pelo Pycharm:
'''
import emoji
# https://pypi.org/project/emoji/
print(emoji.emojize("Olá, gatinhas :smiling_face_with_sunglasses:\nComo você estão hoje? Rsrsrsrs :cold_face:" , use_aliases=True))

# Cores no terminal:
user = input("Digite um nome bonito:")
cores = {'limpa': '\033[m',
'azul': '\033[34m',
'lilás e fundo vermelho': '\033[1:35:41m',
'verde': '\033[32m',
'amarelo': '\033[33m',
'branco': '\033[31m'}
print(f"Olá, {cores['verde']}{user}{cores['limpa']}!{cores['azul']} Prazer em te conhecer!{cores['limpa']}{cores['amarelo']} Seu nome é belo como esse amarelo!{cores['limpa']}" if user == "Ayrton" or user == "Suzané" or user == "Sané" else f"{cores['lilás e fundo vermelho']}Seu nome é tão feio como essa cor!{cores['limpa']}")


