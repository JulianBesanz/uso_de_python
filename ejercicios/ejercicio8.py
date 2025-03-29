'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''

#map(int, ...) convierte cada numero a entero
#.split() se para los numeros ingresado por espacio
#set() crea el conjunto eliminando duplicados    
conjunto1 = set(map(int, input("ingrese los numeros del primero conjunto: ").split()))
conjunto2 = set(map(int, input("ingrese los numeros del primero conjunto: ").split()))
  

print(conjunto1)
print(conjunto2)

#union de conjunto

union = conjunto1 | conjunto2
interseccion = conjunto1 & conjunto2


print("la union es", union)
print("la interseccion es", interseccion)