def main():
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese una letra: ")

    contador = 0

    for caracter in palabra:
        if caracter == letra:
            contador += 1
    print(f"La letra '{letra}' aparece {contador} veces en la palabra '{palabra}'.")

if __name__ == "__main__":
    main()