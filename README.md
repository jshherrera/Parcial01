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
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

nums = [3, 7, 2, 9, 5]
print(maximo(nums)
```


**correcion del codigo**
```python
def maximo(lista):
    if len(lista) == 0: 
        return none
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] >mayor:
            mayor = lista[i]
    return mayor
nums = [3,7,2,9,5]
print(maximo(nums))'''
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
        print('Guau!')

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

class Perro(Animal):
    def hablar(self):
        print('Guau!')

p = Perro('Canino')
p.hablar()  # Arreglo del problema
```
# Errores encontrados
- p.hablar → no se podia ejecutar el metodo por que faltaba el ()

