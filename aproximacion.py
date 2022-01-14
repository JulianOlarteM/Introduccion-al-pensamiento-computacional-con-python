#Vamos a tratar de encontrar la raiz cudrada de cualquier numero
# A diferencia de la tecnica de enumeracion exhaustiva ahora cualquier numero tendra su raiz a si sea aproximada
#las raizes no exactas tendran su aproximación
objetivo = int(input('Escoge un numero: '))
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
 