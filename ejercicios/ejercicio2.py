'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''


palabra = input("ingrese una palabra")

frase = "Python es un lenguaje de programación poderoso"


if palabra in frase:
    print("la palabra si esta")
else:
    print("la palabra no esta") 
 
 
frase_2 = "Python es un lenguaje de programación poderoso"

palabra_2 =input("ingrese una palabra a buscar ")

print(palabra_2 in frase_2)