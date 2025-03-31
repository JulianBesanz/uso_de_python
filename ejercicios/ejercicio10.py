'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''


productos = {
    "pera": 3.000,
    "manzana": 1.500,
    "banano": 500,
    "limon": 400,
    "sandia": 7000

}

nombre = input("cual producto desea agregar")
precio = float(input("ingrese el valor "))

productos[nombre] = precio #agregaria un nuevo producto al diccionario ya creado

print("productos:", productos) #muestra la el diccionario actualizado
