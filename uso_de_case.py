dia=input("ingrese el dia de la semana").lower()
match dia: 
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case "lunes":
        print(f"{dia} es el dia mas dificil")
    case "martes" | "miercoles" | "jueves":
        print("es un dia normal")
    case _:
        print("e; texto no es un dia de la semana")