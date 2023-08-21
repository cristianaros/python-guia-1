def main():
    numero_ingresado = int(input("Ingrese un numero entero: "))

    if numero_ingresado < 2:    #si el numero ingresado es menor a 2 no es primo
        print(f"{numero_ingresado} no es un numero primo.")
    elif numero_ingresado == 2: #si el numero ingresado es igual a 2 es primo
        print(f"{numero_ingresado} es un numero primo.")
    else:
        for i in range(2, numero_ingresado):
            if numero_ingresado % i == 0:   #si el numero ingresado su residuo es 0 no es un numero primo
                print(f"{numero_ingresado} no es un numero primo.")
                break
        else:   #sino es primo
            print(f"{numero_ingresado} es un numero primo.")

if __name__ == "__main__":
    main()