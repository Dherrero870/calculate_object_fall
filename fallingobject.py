# introducción de datos
altura = float (input("introduce la altura inicial en m:"))
gravedad = float (input("introduce la gravedad en m/s^2:"))
momento = float (input("introduce el momento exacto en s:"))
velocidad_inicial = float (input("introduce la velocidad inicial en m:"))
# calculo de la posición en un momento determinado
posición_exacta = float(altura + (velocidad_inicial * momento) - (1/2 * gravedad  * (momento ** 2)))
# normalmente la velocidad introducida es 0 si no participan fuerzas externas 
# resultado
if posición_exacta>=0:
    print ("la posición en m es:",posición_exacta) 
else:
    print ("la posición es 0")