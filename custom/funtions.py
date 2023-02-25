#suma los numeros de una lista
def suma(a: list[int]):
    return sum(a)

#Buscando a los aprobados y dandoles un valor 1, todo lo demas quedaria en 0 (Reprobado) y creamos una nueva columna para este valor nuevo.
def set_int_aprobado(estado ):
    if(estado == 'A'):
        return 1
    else:
        return 0