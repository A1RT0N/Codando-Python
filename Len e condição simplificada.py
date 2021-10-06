while True:
        carinha = input("Qual é seu nome, imbecil:")
        if len(carinha) < 6:
            print(f"Ô jegue, faltam {len(carinha)} caracteres")
            continue
        elif len(carinha) > 16:
            print(f"Nome grande não cacete, tire { len(carinha) - 16} caracteres")
            continue
        elif "!" in carinha or "@" in carinha or "." in carinha:
            print("Escreve direito, puta!")
            continue
        else:
            print("Tudo certo, gata!")
        break

# Condição simplificada (boa quando você está muiiittoooo apertado com o quesito linha):

tempo = float(input("Quantos anos seu carro tem?\n--->"))
print("Seu carro está novinho" if tempo <= 3 else "Seu carro tá todo bagaçado")
a = sorted("amor")
print(a)