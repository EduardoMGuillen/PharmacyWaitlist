def generador_farmacia():
    for x in range(1, 100000):
        yield x


def generador_cosmeticos():
    for x in range(1, 100000):
        yield x


def generador_perfumeria():
    for x in range(1, 100000):
        yield x


f = generador_farmacia()
c = generador_cosmeticos()
p = generador_perfumeria()


def decorador(area):
    print("\n" + "*" * 23)
    print("Su turno es:")
    if area == "P":
        print(area + " - " + str(next(p)))
    if area == "C":
        print(area + " - " + str(next(c)))
    if area == "F":
        print(area + " - " + str(next(f)))
    print("Aguarde y sera atendido!")
    print("*" * 23 +"\n")

    return decorador
