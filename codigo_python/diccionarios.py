def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(mi_diccionario)
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44556789,
        'Brasil': 210123456,
        'Colombia': 50789456
    }

    for pais in poblacion_paises.keys():
        print(pais)

    for valores in poblacion_paises.values():
        print(valores)

    for pais, poblacion in poblacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes')

if __name__ == "__main__":
    run()
