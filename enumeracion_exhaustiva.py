# Enumeracion  Exhaustiva: 
#   Si un numero tiene una raiz cuadrada exacta:
 
objetivo= int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
     respuesta=respuesta+1
if respuesta**2 == objetivo:
    print('La raiz cuadrada de'+' '+str(objetivo)+' '+'es'+' '+str(respuesta))
else:
    print(str(objetivo)+' '+'no tiene una raiz cuadrada exacta ')

