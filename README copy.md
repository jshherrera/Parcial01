# 📝 Parcial – Paradigmas de Programación

Este repositorio contiene la resolución del **parcial de Paradigmas de Programación**, dividido en dos ejercicios:

- **Programación Estructurada** (`estructural.py`)
- **Programación Orientada a Objetos (OOP)` (`oop.py`)

El objetivo es **detectar y corregir errores de sintaxis y lógica**, documentando cada cambio con comentarios detallados.

---

## 📂 Archivos

- `estructural.py` → Ejercicio que busca el valor máximo en una lista de números.
- `oop.py` → Ejercicio que modela animales y sus comportamientos.

---

## 🎯 Objetivos

- Identificar errores comunes en código Python.  
- Evitar malas prácticas como el uso de nombres que sobrescriben funciones internas.  
- Comprender las diferencias entre paradigmas **estructural** y **orientado a objetos**.  
- Documentar con comentarios detallados las correcciones.  

---

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