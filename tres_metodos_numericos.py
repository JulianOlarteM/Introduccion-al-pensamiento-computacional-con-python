def enum_exhaustivo(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta=respuesta+1
    if respuesta**2 == objetivo:
        print('La raiz cuadrada de'+' '+str(objetivo)+' '+'es'+' '+str(respuesta))
    else:
        print(str(objetivo)+' '+'no tiene una raiz cuadrada exacta ')
    
def aproximacion(objetivo):
    epsilon = 0.01
    paso=epsilon**2
    respuesta =0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta = respuesta + paso
        print(str(abs(respuesta**2 - objetivo)),str(respuesta))

    if abs(respuesta**2 - objetivo) >= epsilon: 
        print('no se encontro la raiz cudrada del'+' '+str(objetivo))
    else:
        print('la raiz cudradada de'+' '+str(objetivo)+' '+'es'+' '+str(respuesta))
    
def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo=0.0
    alto=max(1.0,objetivo)
    respuesta = (alto+bajo)/2

    while abs(respuesta**2 - objetivo)>= epsilon :
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}') 
        if respuesta**2 < objetivo:
            bajo= respuesta
        else:  
            alto = respuesta 
        respuesta = (alto+bajo)/2
    print('La raiz cuadrada de '+str(objetivo)+' es '+ str(respuesta))

def run():
    tipo_metodo=int(input('''
        1. Enumeracion exhaustiva
        2. Aproximacion 
        3. Busqueda Binaria
        '''))
    num=int(input('Ingrese el numero que desea operar. '))
    if tipo_metodo == 1:
        enum_exhaustivo(num)
    elif tipo_metodo == 2:
        aproximacion(num)
    elif tipo_metodo == 3:
        busqueda_binaria(num)
    else:
        print('Ingrese una opcion valida')

if __name__ == "__main__":
    run()