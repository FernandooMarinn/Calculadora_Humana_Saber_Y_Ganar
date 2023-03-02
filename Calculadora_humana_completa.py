import random


def fallo(contador):
    return print("Has fallado. Has conseguido {} veces seguidas.".format(contador))

def preguntar_numero():
    respuesta = input()
    while not comprobar_si_numero(respuesta):
        print("No has introducido un numero.")
        respuesta = input("")
    return int(respuesta)

def comprobar_si_numero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

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
            print("Por {} \n".format(mult))
            respuesta = preguntar_numero()
            if respuesta == mult * inicio:
                contador += 1
                inicio *= mult
            else:
                fallo(contador)
                stop = False
        elif inicio > 150:
            resta = random.randint(1, 150)
            print("Menos {} \n".format(resta))
            respuesta = preguntar_numero()
            if respuesta == inicio - resta:
                contador += 1
                inicio -= resta
            else:
                fallo(contador)
                stop = False
        else:
            sumar = random.randint(1, 50)
            print("Más {} \n".format(sumar))
            respuesta = preguntar_numero()
            if respuesta == inicio + sumar:
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
        print("Menos {} \n".format(resta))
        respuesta = preguntar_numero()
        if respuesta < 30 and respuesta == inicio - resta:
            inicio -= respuesta
            r = random.randint(3, 6)
            print("Y {} * {} son {} ".format(respuesta, r, respuesta * r))
            inicio = respuesta * r
        elif respuesta == inicio - resta:
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
        print("Más {} \n".format(sumar))
        respuesta = preguntar_numero()
        if respuesta == inicio + sumar and respuesta < 200:
            inicio += sumar
            contador += 1
        elif respuesta == inicio + sumar and respuesta >= 200:
            contador += 1
            print("Y {} menos 150 son {}".format(respuesta, respuesta - 150))
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
        numero_a_sumar = random.randint(50, 301)
        if primo(int(inicio)) == True:
            inicio = random.randint(50, 150)
            print("El numero era primo, seguimos con", inicio)
        if inicio % dividir == 0 and int(inicio / dividir) > 1:
            operacion = int(input("Entre {} \n".format(dividir)))
            if operacion == inicio / dividir:
                contador += 1
                inicio /= dividir
                if operacion < 30:
                    print("Y {} + {} son {}".format(int(inicio), numero_a_sumar, int(inicio + numero_a_sumar)))
                    inicio += numero_a_sumar
            else:
                fallo(contador)
                stop = False
        else:
            continue


def main():
    barra = "*" * 90
    print(barra)
    print("\nBienvenido al juego para entrenar el calculo mental: ¡La calculadora humana! \n"
          "Este juego puede correr en diferentes maneras, selecciona uno de los siguientes: \n\n"
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
