import random

def generar_contrasena():
    mayuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['|', '!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡', '¿', '_', '-']

    caracteres = mayuscula + minuscula + simbolos + numeros

    contrasena = []

    for i in range(24):
        caracter_randon = random.choice(caracteres)
        contrasena.append(caracter_randon)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print(f'Tu nueva contraseña es: {contrasena}')


if __name__ == "__main__":
    run()