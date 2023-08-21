def main():
    palabra = ""
    while palabra != "salir":
        palabra = input("Ingrese una palabra (o 'salir' para terminar): ")
        if palabra != "salir":
            palabra_al_reves = palabra[::-1]
            print(f"La palabra al revés es: {palabra_al_reves}")

if __name__ == "__main__":
    main()