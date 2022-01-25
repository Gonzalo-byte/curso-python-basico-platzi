
def numeros_primos(maximo):
    '''
    funcion que devuelve los numeros primos del 1 al n
    '''
    for n in range(1, maximo + 1):

        validador = None
        for i in range(n-1, 1, -1):
            if n % i == 0:
                validador = False
                break
            else:
                validador = True
        if validador == True:
            print(n)


if __name__ == '__main__':
    numeros_primos(100)
