x=600
y=400



'''
Condicional if elif else
if then else

if condicion:
    operacion 1
    operacion 2
    .
    .
    .
    .
    operacion n


'''

if x > y:
    print("x es mmayor a y")

print("ejeccion terminada")


#caso 2

if x < y:
    print("ex es menor que y")
else:
    print("x es mayor que y")

print("ejecuccion terminada")

#caso 3 uso de if elif else 

if x < y:
    print("ex es menor que y")
elif x==y: #condicion
    print("X es igual a y ")
elif x/y==8: #condicion
    print("x divido y es igual a 8")
else: # de lo contrario
    print("x es mayor que y")


#Variante 1

if  x%2==0 and x>500: #multiples condiciones a evaluar
    print("x es par y mayor que 500")


#caso de uso el login a una aplicacion

# usuario=input("ingrese su usuario ")
# password=input("pot favor ingrese su password")

# if usuario=="Vaan" and password=="TodasMienten":
#     print("ingreso exitoso")
# else: 
#     print("usuario o password incorrecto ")
print("FINISH")

usuario=input("ingrese usuario")

if usuario=="Vaan":
    password=input("ingrese el password")
    if password=="1234":
        print("ingreso correcto")
    else:
        print("contrasena incorrectos")
else:
    print("usuario incorrecto")