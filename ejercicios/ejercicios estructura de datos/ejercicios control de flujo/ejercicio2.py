'''
solicitar una edad y clasificarla 
en menores de edad (0-17), adultos (18-64) y
adultos mayores(65+)
para este ejercicio usar if elif else
y tambien usar match/case
'''

edad = int(input("ingrese la edad"))

if edad == 17 or edad < 17:
    print("es menor de edad")
elif edad >= 18 and edad <= 64:
    print("adultos")
elif edad >= 65:
    print("adultos mayores")