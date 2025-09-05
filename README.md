# Errores encontrados

### estructura codigo ('estructura.py')

**codigo original:**

def maximo(lista):
    max = lista[0]          # la funcion max sobre escribe la funcion interna de nuenstro programa
    for i in range(1, len(lista)):  
        if lista[i] > max:
            max = lista[i]
    return max

nums = [3, 7, 2, 9, 5]
print(maximo(nums) # falta cerrar el parentesis para asi poder ejecutar el codigo

**correcion del codigo**
def maximo(lista):
    if len(lista) == 0: 
        return none
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] >mayor:
            mayor = lista[i]
    return mayor
nums = [3,7,2,9,5]
print(maximo(nums))

# justificacion 

- Se cambió max → mayor para no sobrescribir la función interna max().

- Se corrigió el print(...) cerrando el paréntesis.

- Se añadió validación de lista vacía para evitar IndexError.

