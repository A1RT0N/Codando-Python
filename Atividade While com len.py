while True:
    usuario = input("Qual é o seu usuario ---> ")
    if 5 < len(usuario) < 16 and not "@" in usuario and not "!" in usuario and not "," in usuario:
        print("Sua conta foi criada!")
        break

    elif len(usuario) < 5:
        print(f"Sua conta necessita ter mais caracteres, falta: {5 - len(usuario)}")
        continue

    elif len(usuario) > 16:
        print(f"Sua conta necessita ter menos caracteres, tire: {len(usuario) - 16}")
        continue

    elif "@" in usuario or "!" in usuario or "," in usuario:
        print("O sistema não aceita caracteres especiais!")
        continue


