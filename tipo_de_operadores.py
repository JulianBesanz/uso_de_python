''' 
operadores aritmeticos
20 de marzo 



'''

#operador suma

# print(2+6)


# #operador resta

x=4
y=6
# print(x*y)

#operador division 

z =12/4
# print(z)
# print(type(z)) #el resultado de la division siempre es flotante "float"


#operador division piso(floor)
# print(10/3) #division tradicional
# print(10//3) #division
# print(14.5/3)
# print(14.5//3) # division piso siempre devuelve el entero mas proximo hacia abajo

#operador modulo
print(20%3) #es el residuo de la division 
print(8//-3)
print(8/-3)


#operador potencia 
print(x**2)

'''
operadores de comparacion 

Este tipo de operadores los usamos cuando deseamos comparar expresiones o 
variables. Python evalúa si se cumple la comparación y nos devuelve (retorna) un 
valor True o False
'''

# #es igual a 
# print("enca" == "Enca")

# print(8==8)

# print(3==3.0)

#es diferente de 
print("palabra" != "Palabra")


'''
operadores de asignacion
'''
#asignacion de igualdad o definicion
w=5

#incremento
saldo=100
# saldo= saldo + 1
saldo+=8
print(saldo)


#decrecimiento

saldo_b=200
# saldo= saldo + 1
saldo_b-=8
print(saldo_b)

#se piden datos
'''
operadores logicos
and: comprueba si todas las condiciones se cumplen, true, false de lo contrario
or: comprueba si alguna de las condiciones se cumple, ture, false de lo contrario
not: negar el estado de una variable
'''
print(x==4 and y==6)
print(x==4 or y==8)

usuario_logueado=True
click_logout=True
print(not usuario_logueado)
