'''
crear una lista de pabras predifinida y pedir al usuario una palabra. 
indicar si esta en lista o no
'''


mi_lista=["enero", "febrero", "marzo"]
consulta=input("ingrese el mes a buscar").lower()

if consulta in mi_lista:
    print("la palaba se encuentra en la lista")

if mi_lista.count(consulta)>0:
    print("la palabra se encuentra en la lista")