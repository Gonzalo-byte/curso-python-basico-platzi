

def convertir_moneda():
    """
    Convierte una cantidad de una moneda a otra.
    """
    bol = True
    while bol==True:

        monedaOrigen = int(input('Ingrese el numero de la moneda origen:\n'
                        '1. USD \n'
                        '2. ARS \n'
                        '3. EUR \n'))
        
        monedaDestino  = int(input('Ingrese el numero de la moneda destino:\n'
                        '1. USD \n'
                        '2. ARS \n'
                        '3. EUR \n'))
        if monedaOrigen == monedaDestino :
            print('No puede ser la misma moneda')
        else:
            bol = False
    
    cantidad = float(input('Ingrese la cantidad a convertir:\n'))
    
    if monedaOrigen == 1:
        if monedaDestino  == 2:
            print(str(cantidad) + ' USD a ARS: ', cantidad * 200)
        elif monedaDestino  == 3:
            print(str(cantidad) + ' USD a EUR: ', cantidad * 0.87)

    if monedaOrigen == 2:
        if monedaDestino  == 1:
            print(str(cantidad) + ' ARS a USD: ', cantidad / 200)
        elif monedaDestino  == 3:
            print(str(cantidad) + ' ARS a EUR: ', cantidad / 230)
    
    if monedaOrigen == 3:
        if monedaDestino  == 1:
            print(str(cantidad) + ' EUR a USD: ', cantidad * 1.15)
        elif monedaDestino  == 2:
            print(str(cantidad) + ' EUR a ARS: ', cantidad * 230)

if __name__ == '__main__':

    convertir_moneda()

    
    
    
