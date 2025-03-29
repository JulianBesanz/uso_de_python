'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''

#se crea la tupla con las ciudades
ciudades = ("palmira", "medellin", "cali")

#se muestra cada ciudad solicitada
print("primera ciudad: ", ciudades[0])
print("ultima ciudad: ", ciudades[2])

for ciudad in ciudades:
    print(f"{ciudad}tiene {len(ciudad)} caracteres.")

