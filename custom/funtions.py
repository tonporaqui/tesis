#suma los numeros de una lista
def suma(a: list[int]):
    return sum(a)

#Buscando a los aprobados y dandoles un valor 1, todo lo demas quedaria en 0 (Reprobado) y creamos una nueva columna para este valor nuevo.
def set_int_aprobado(estado ):
    if(estado == 'A'):
        return 1
    else:
        return 0
    
#Utilizando la regla de mayor a 3.999 esta aprobado, significa que retornara un 1 para aprobado
def set_in_aprobado_nota(nota):
    if(nota > 3.999):
        return 1
    else:
        return 0