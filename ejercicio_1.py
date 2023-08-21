import random

def main():
    numero_aleatorio = random.randint(1, 100)   #se genera el numero aleatorio entre el 1 y el 100

    numero_ingresado = int(input("Ingrese un número entre 1 y 100: "))
    while numero_ingresado != numero_aleatorio: #mientras el numero ingresado sea distinto al numero aleatorio se usara el while
        if numero_ingresado < numero_aleatorio:
            print("El número ingresado es bajo.")   #indica de que el numero ingresado esta por debajo del aleatorio
        elif numero_ingresado > numero_aleatorio:
            print("El número ingresado es alto.")   #indicar de que el numero ingresado esta por encima del aleatorio
        numero_ingresado = int(input("Ingrese otro número: "))

    print(f"El número aleatorio era: {numero_aleatorio}")

if __name__ == "__main__":
    main()