from time import sleep

produtorio = 0
valor1 = 2
valor2 = 1
resultado = 2
while produtorio < 1000000:
    resultado *= valor1/valor2
    valor2 += 2
    resultado *= valor1/valor2
    valor1 += 2
    produtorio += 1
    if produtorio / 100 == produtorio // 100:
        sleep(0.01)
        print(resultado)