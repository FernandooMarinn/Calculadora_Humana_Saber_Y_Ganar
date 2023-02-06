import random


def fallo(contador):
    return print("Has fallado. Has conseguido {} veces seguidas.".format(contador))


def primo(numero):
    lista = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista.append(i)
    if len(lista) < 3:
        return True
    else:
        return False


def calculadora_humana_normal():
    inicio = random.randint(1, 50)
    contador = 0
    stop = True
    print("Empezamos por {}".format(inicio))
    while stop:
        if inicio < 50:
            mult = random.randint(2, 5)
            operacion = int(input("Por {} \n".format(mult)))
            if operacion == mult * inicio:
                contador += 1
                inicio *= mult
            else:
                fallo(contador)
                stop = False
        elif inicio > 150:
            resta = random.randint(1, 150)
            operacion = int(input("Menos {} \n".format(resta)))
            if operacion == inicio - resta:
                contador += 1
                inicio -= resta
            else:
                fallo(contador)
                stop = False
        else:
            sumar = random.randint(1, 50)
            operacion = int(input("Más {} \n".format(sumar)))

            if operacion == inicio + sumar:
                inicio += sumar
                contador += 1
            else:
                fallo(contador)
                stop = False


def calculadora_restas():
    contador = 0
    stop = True
    inicio = random.randint(50, 150)
    print("Empezamos por {}".format(inicio))
    while stop:
        resta = random.randint(1, 30)
        operacion = int(input("Menos {} \n".format(resta)))
        if operacion < 30 and operacion == inicio - resta:
            inicio -= operacion
            r = random.randint(3, 6)
            print("Y {} * {} son {} ".format(operacion, r, operacion * r))
            inicio = operacion * r
        elif operacion == inicio - resta:
            contador += 1
            inicio -= resta
        else:
            fallo(contador)
            stop = False


def calculadora_sumas():
    contador = 0
    stop = True
    inicio = random.randint(1, 150)
    print("Empezamos por {}".format(inicio))
    while stop:
        sumar = random.randint(1, 50)
        operacion = int(input("Más {} \n".format(sumar)))

        if operacion == inicio + sumar and operacion < 200:
            inicio += sumar
            contador += 1
        elif operacion == inicio + sumar and operacion >= 200:
            contador += 1
            print("Y {} menos 150 son {}".format(operacion, operacion - 150))
            inicio += sumar
            inicio -= 150
        else:
            fallo(contador)
            stop = False


def calculadora_divisiones():
    contador = 0
    stop = True
    inicio = random.randint(50, 150)
    print("Empezamos por {}".format(inicio))
    while stop:
        dividir = random.randint(2, 15)
        por = random.randint(50, 301)
        if primo(int(inicio)) == True:
            inicio = random.randint(50, 150)
            print("El numero era primo, seguimos con", inicio)
        if inicio % dividir == 0 and int(inicio / dividir) > 1:
            operacion = int(input("Entre {} \n".format(dividir)))
            if operacion == inicio / dividir:
                contador += 1
                inicio /= dividir
                if operacion < 30:
                    print("Y {} + {} son {}".format(inicio, por, int(inicio + por)))
                    inicio += por
            else:
                fallo(contador)
                stop = False
        else:
            continue


def main():
    barra = "*" * 90
    print(barra)
    print("\nBienvenido al juego para entrenar el calculo mental: ¡La calculadora humana! \n"
          "Este juego puede correr en diferentes maneras, selecciona uno de los siguientes: \n"
          "1 - La calculadora humana normal. \n"
          "2 - La calculadora solo restas. \n"
          "3 - La calculadora solo sumas. \n"
          "4 - La calculadora solo divisones. \n \n")

    print(barra)
    modo = int(input())
    if modo == 1:
        return calculadora_humana_normal()
    elif modo == 2:
        return calculadora_restas()
    elif modo == 3:
        return calculadora_sumas()
    elif modo == 4:
        return calculadora_divisiones()
    else:
        while modo != 1 or modo != 2 or modo != 3 or modo != 4:
            modo = int(input("No has introducido un numero correcto. Las opciones son 1, 2, 3, 4 "))


if __name__ == '__main__':
    main()
