import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Ingresa un numero de 1 a 100: '))
    vidas = 5
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Ingresa un numero mas grande')
            vidas -= 1
        elif numero_elegido > numero_aleatorio:
            print('ingresa un numero mas pequeño')
            vidas -= 1
        if vidas == 0:
            print('Juego terminado')
            break
        print(f'Te quedan {vidas} vidas')
        numero_elegido = int(input('Ingresa otro numero: '))
    print('¡¡¡ ganaste !!!')


if __name__ == "__main__":
    run()