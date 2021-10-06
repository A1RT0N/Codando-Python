idade = int(input("Quantos anos você tem? --->"))

if idade > 18:
    print("Você pode entrar nessa porcaria")

else:
    print(f"Sinto muito, você tem apenas {idade} anos")
    print(f"Faltam {18 - idade} anos")
