# def run():
#     print("Comienzo")
#     cuenta = 0
#     for i in range(1, 1000):
#         cuenta = pow(i, 2)
#         print(f"Raiz cuadra de {i} es {cuenta}")


# if __name__ == "__main__":
#     run()




def run():
    LIMIT  = 1000000

    count = 0
    power_2 = 2**count
    while power_2 < LIMIT:
        print(f"2 elevado a {count} es igual a {power_2}")
        count = count + 1
        power_2 = 2**count


if __name__ == "__main__":
    run()