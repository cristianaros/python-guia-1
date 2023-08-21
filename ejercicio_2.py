
def main():
        
        print("¿Qué conversión desea realizar?")
        print("1) centímetros -> pulgadas")
        print("2) metros -> kilometros")
        print("3) onzas -> gramos")
        print("4) milla -> kilometro")
        print("5) celcius -> fahrenheit")
        print("6) Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            centimetros = float(input("Ingrese la cantidad de centímetros: "))
            pulgadas = centimetros / 2.54
            print(f"{centimetros} centímetros son {pulgadas} pulgadas.")
        elif opcion == 2:
            metros = float(input("Ingrese la cantidad de metros: "))
            kilometros = metros / 1000
            print(f"{metros} metros son {kilometros} kilómetros.")
        elif opcion == 3:
            onzas = float(input("Ingrese la cantidad de onzas: "))
            gramos = onzas * 28.35
            print(f"{onzas} onzas son {gramos} gramos.")
        elif opcion == 4:
            millas = float(input("Ingrese la cantidad de millas: "))
            kilometros = millas * 1.609
            print(f"{millas} millas son {kilometros} kilómetros.")
        elif opcion == 5:
            celcius = float(input("Ingrese la temperatura en grados Celcius: "))
            fahrenheit = celcius * 1.8 + 32
            print(f"{celcius} grados Celcius son {fahrenheit} grados Fahrenheit.")
        else:
            print("Opcion invalida.")
if __name__ == "__main__":
    main()