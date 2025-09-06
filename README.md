# Errores encontrados

### estructura codigo ('estructura.py')

**codigo original:**

# 🔎 Ejercicio 1 – Programación Estructural

### 📌 Descripción
El ejercicio busca el **máximo valor** dentro de una lista de números.  
Ejemplo: encontrar la nota más alta de un grupo de estudiantes.

---

### ❌ Código original (con errores)
```python
def maximo(lista):  
    max = lista[0]  # el  max podria sobrescribir la funcion
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

nums = [3, 7, 2, 9, 5]
print(maximo(nums)  # falta cerrar el parentesis 
```


**correcion del codigo**
```python
def maximo(lista): # se valida si la lista esta vacia
    if len(lista) == 0: #retorna la lista en caso de que este vacia
        return "La lista está vacía"# se cambio la funcion max para que se pueda dar una validacion a la lista 
    mayor = lista[0] # se cambia la variable max por mayor para que este no sobrescriba la funcion
    for i in range(1, len(lista)):  #recorrere la lista 
        if lista[i] >mayor: #se compara correctamente para encontrar el el mayor
            mayor = lista[i]  # se actualiza el valor maximo cuando este corresponde 
    return mayor        #retorna a el valor maximo encontrado
nums = [3, 7, 2, 9, 5]
print(maximo(nums)) #secerro el parentesis  
```
# justificacion 

- Se cambió max → mayor para no sobrescribir la función interna max().

- Se corrigió el print(...) cerrando el paréntesis.

- Se añadió validación de lista vacía para evitar IndexError.

### estructura codigo('oop.py')

**codigo original:**
```python
class Animal:
    def __init__(self, especie):
        self.especie = especie
    def hablar(self):
        print('Hace un sonido')

class Perro(Animal):
    def hablar(self):
        print('miau')

p = Perro('Canino')
p.hablar   # falta agregarle el parentesis
```

**correcion del cogigo**
```python

class Animal:
    def __init__(self, especie):
        self.especie = especie
    def hablar(self):
        print('Hace un sonido')

class Gato(Animal):
    def hablar(self):
        print('MIAU')

g = Gato('MIAU')
g.hablar()  # Arreglo del problema
```
# Errores encontrados
- p.hablar → no se podia ejecutar el metodo por que faltaba el ()

