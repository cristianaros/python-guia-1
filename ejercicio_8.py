def main():

    def calcular_area_circulo(radio):
        return 3.14 * radio ** 2

    def calcular_volumen_cilindro(radio, altura):
        area_base = calcular_area_circulo(radio)
        return area_base * altura
    
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))

    volumen = calcular_volumen_cilindro(radio, altura)
    print(f"El volumen del cilindro de radio {radio} y altura {altura} es {volumen}")

if __name__ == "__main__":
    main()