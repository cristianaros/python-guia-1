def main():
    cesta_compra = {}   #diccionario vacio donde se guardaran los articulos y sus precios
    num_articulos = int(input("Ingrese el número de artículos que desea agregar: "))    #numero de articulos que se agregaran
    
    for i in range(num_articulos):
        articulo = input(f"Ingrese el artículo {i+1}: ")
        precio = float(input("Ingrese el precio: "))
        cesta_compra[articulo] = precio

    print("Lista de la compra")
    total = 0
    for articulo, precio in cesta_compra.items():
        print(f"{articulo} {precio}")
        total += precio
    print(f"Total: {total}")

if __name__ == "__main__":
    main()