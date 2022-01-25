#palindromo

def palindromo():
    print('''
    
    Bienvenido al juego del palindromo
    Escribe una palabra y te diré si lo es o no
    
    ''')

    palabra = input('Escribe una palabra: ')
    palabra = palabra.lower()
    palabra = palabra.replace(' ','')

    if palabra == palabra[::-1]:
        print('Es un palindromo')
    else:
        print('No es un palindromo')


if __name__ == '__main__':
    palindromo()