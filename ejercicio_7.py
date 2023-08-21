def main():
    numero_ingresado = int(input("Ingrese un numero entero: "))

    if numero_ingresado < 0:
        print("El número ingresado no puede calcular su factorial.")
    elif numero_ingresado == 0:
        print("El factorial de 0 es 1.")
    else:
        factorial = 1
        for i in range(1, numero_ingresado + 1):
            factorial = factorial * i
        print(f"El factorial de {numero_ingresado} es {factorial}.")

if __name__ == "__main__":
    main()