import random


def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    contador = 0

    while contador <= 5:
        numero_elegido = int(input("""
        
        ADIVINA EL NUMERO SECRETO ENTRE 1 Y 100
        Tienes """ + str(5-contador) + """ intentos
        Numero: """

        ))
        if numero_elegido == numero_secreto:
            print("Has ganado despues de "+contador+" intentos")
            break
        else:
            contador += 1
            if numero_elegido > numero_secreto:
                print("El numero es menor")
            else:
                print("El numero es mayor")


if __name__ == "__main__":
    adivina_el_numero()
