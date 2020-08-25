def exchanges(moneda,cantidad):
    result = 0
    if moneda == 1:
        result = moneda*0.0013
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dolares')
    elif moneda == 2:
        result = cantidad*0.00027
        print(f'Los {cantidad} pesos colombianos equivalen a {result} dolares')
    elif moneda == 3:
        result = cantidad*0.014
        print(f'Los {cantidad} pesos argeninos equivalen a {result} dolares')
    elif moneda == 4:
        result = cantidad*0.044
        print(f'Los {cantidad} pesos mexicano equivalen a {result} dolares')
    else:
        print('Ingrese un numero de la seleccion')

""" pesos = input("¿Cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes  $" + dolares + " dólares") """


if __name__ == "__main__":
    try:
        moneda = int(input('''
        Selecciona la monida que quieres convertir a dolares:
            [1] Peso Chileno a Dolar
            [2] Peso Colombiano a Dolar
            [3] Peso Argentino a Dolar
            [4] Peso Mexicano a Dolar
        Selecciona: '''))
        print('===========================')
        cantidad = int(input('Ingresa la cantidad a convertir: '))
        exchanges(moneda,cantidad)
    except:
        print('!!!!!!!!!E R R O R!!!!!!!!!!')
        print('Ingrese valores numerorico unicamente')