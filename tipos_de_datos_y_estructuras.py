'''
TIPOS DE DATOS
strings: cadenas de texto <class 'str'>

'''

dato="Enca24"
dato_2='Enca24'

#print(type(dato))
#print(type(dato_2))


#Concatenacion de string

texto_1 = "programa"
texto_2 = "desarrollador junior"

enunciado=texto_1 = texto_2
#print(enunciado)

#Indexacion de string 
#la indexacion se refiere a acceder a un elemento de una cadena en una posicion
nombre = "julian andres"

#print(nombre[0])
'''
python es un lenguaje indexado en 0
'''
#print(nombre[2])

#slicing de cadenas ( porcion de la cadena)

#print(nombre[:])war
#print(nombre[0:3]) #esta forma no inlucye el lado derecho 
#print(nombre[0-5])

'''
tipos de datos numericos
<class 'int': se refiere a numero enteros
<class "float: se refiere a numeros flotantres que contienen decimales

'''

x=5
print(type(x))
y=5.0
print(type(y))


'''
datos boolean
'''

asistencia= True
print(type(asistencia))



'''
TIPOS DE ESTRUCTURAS

sets: se definen en python con {,,,,,}
tuplas: se definen en python con (,,,,,)
listas: se definen en python con [,,,,,]

diccionarios: se definen en python con {'clave': 'valor' ,,,}
'''


#Sets o conjuntos

'''
se utilizan para almacenar informacion no interesa el orden ni la posicion
no permite valores duplicados
'''

conjunto_1 ={"a", "b", "c"}

conjunto_2 ={"d", "e", "f"}

print(type(conjunto_1))

print(conjunto_1)
'''
los metodos indican las cosas que podemos hacer con los objetos
'''

#Metodos de los conjuntos

conjunto_1.add("h")
print(conjunto_1)

conjunto_2.remove("f")
print(conjunto_2)

conjunto_3 =conjunto_1.union(conjunto_2)
print(conjunto_3)

#eplicar un metodo
conjunto_2.update(conjunto_1)
print(conjunto_2)


# '''
# Tuplas 
# son estructuras en python mas rigidas,
# son inmutables,
# almacen distintos tipos de datos
# '''

tupla_1 =(1, "b", True)
print(type(tupla_1))

tupla_1.count("b") #devuele numero de ocurrencias de un valor
print(tupla_1)

print(tupla_1.index('b'))


'''
uso de listas []
'''

mi_lista = [9,5,8,15,True]
print(mi_lista)
print(len(mi_lista)) #Funcion python de len
(mi_lista.append(False)) #Aplicando un metodo a la slita 
print(mi_lista)
print(sum(mi_lista))#funcion de python sum


'''
uso de diccionarios
{clave:valor,clave:valor}
'''

estudiantes={"carlos": {"edad":10, "ciudad": "medellin"},"maria":10,"sofia":10,"devora":10,"eula":10,}





