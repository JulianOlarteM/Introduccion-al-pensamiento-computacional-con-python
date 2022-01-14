''' Ciclo While

'''
#contador=0
#while contador < 10:
#    print(contador)
#    contador = contador +1

#contador de uno a 100 utilizando dos ciclos while
contador_externo = 0
contador_interno = 0
while contador_externo < 10 :
    while contador_interno < 10:
        print(contador_externo,contador_interno)
        contador_interno=contador_interno+1
    contador_externo=contador_externo+1
    contador_interno=0