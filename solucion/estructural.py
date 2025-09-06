

def maximo(lista):

    if len(lista) == 0:
        return "La lista está vacía"  


    mayor = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i] 
    return mayor  

nums = [3, 7, 2, 9, 5]
print("El máximo es:", maximo(nums))  
