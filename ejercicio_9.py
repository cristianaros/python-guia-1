def main():
    
    def palabra_mas_larga(lista_palabras):
        palabra_mas_larga = ""
        for palabra in lista_palabras:
            if len(palabra) > len(palabra_mas_larga):
                palabra_mas_larga = palabra
        return palabra_mas_larga
    
    lista_palabras = ["Hola","buenos","dias"]
    palabra = palabra_mas_larga(lista_palabras)
    print(f"La palabra más larga es '{palabra}'")

if __name__ == "__main__":
    main()