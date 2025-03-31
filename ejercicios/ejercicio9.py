'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

estudiantes = {"juan": 9,
                "julian": 10, 
                "armando": 5,
                "sofia": 3, 
                "cristal": 2}

nombre = input("ingrese nombre  de estudiante  a consultar")

calificacion = estudiantes.get(nombre, "estudiante no encontrado")
print("califacion:", calificacion)