def run():
    characters = input('Ingrese cadena: ')
    for letter in characters:
        print(letter)

    sentence = input('Escriba una frase: ') 
    for character in sentence:
        print(character.upper())


if __name__ == "__main__":
    run()