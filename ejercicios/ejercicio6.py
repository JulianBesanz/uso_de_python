'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

#se crea la lista para almacenar numeros
lista = []

for i  in range(5):  #se repetira 4 veces
    numeros = int(input("ingrese el numero")) # solicitar los numeros
    lista.append(numeros) # los agregara a lista

print("lista de numeros ingresados,:", lista) # resultado de la lista final

lista.reverse()
print(lista)
print(sum(lista))

lista.sort(reverse=True) #reverse_True descendente
print(lista)