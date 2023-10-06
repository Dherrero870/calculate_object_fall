def calcular_area(base,altura):
    area = base * altura /2
    return area
# pido altura y base al usuario
altura = float (input("¿Cuál es la altura?"))
base = float (input("¿Cuál es la base?"))
#guardo el area
area_calculada = calcular_area(base,altura)
#imprime el area
print(area_calculada)