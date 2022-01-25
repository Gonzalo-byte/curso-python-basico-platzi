def run():

    while True:

        base = input("Ingrese la base: ")
        potencia = input("Ingrese la potencia: ")

        try:
            base = int(base)
            potencia = int(potencia)
            for i in range(potencia):
                    print(str(base) + " elevado a " + str(i) + " es: " + str(base ** i))
            break
                
        except:
            print("Los valores ingresados no son correctos")

    

if __name__ == '__main__':
    run()