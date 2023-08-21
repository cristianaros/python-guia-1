def main():
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    if len(palabra1) < 3 or len(palabra2) < 3:
        print("Las palabras deben tener al menos tres letras.")
    else:
        if palabra1[-3:] == palabra2[-3:]:  #si las ultimas 3 letras son iguales estas rimaran
            print("Las palabras riman.")
        elif palabra1[-2:] == palabra2[-2:]:    #si las ultimas 2 letras son iguales estas rimaran un poco
            print("Las palabras riman un poco.")
        else:   #de lo contrario no riman si no son iguales
            print("Las palabras no riman.")

if __name__ == "__main__":
    main()