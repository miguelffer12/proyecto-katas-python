# PROYECTO LÓGICA: Katas de Python

Colección de katas (ejercicios prácticos de programación) resueltas en Python para
aplicar y consolidar los conocimientos del módulo de Python.



## Estructura del repositorio

```
.
├── README.md          # Este archivo: pasos seguidos durante el proyecto
└── katas_python.py    # Los ejercicios resueltos
```

En `katas_python.py` cada ejercicio va encabezado con un comentario que recoge su
enunciado. Al final del archivo hay una función `main()` que comprueba todos los
ejercicios.

> **Nota:** el enunciado original salta del ejercicio 34 al 36 (no existe el 35).
> Se ha respetado la numeración original.

## Cómo ejecutarlo

Requisitos: Python 3.8 o superior. No hace falta instalar ninguna librería externa.

```bash
python katas_python.py
```

El programa muestra el resultado de todos los ejercicios con datos de ejemplo. Al
final pregunta si se quieren probar los **ejercicios interactivos** (8, 11, 31, 38,
39 y 41), que piden datos por teclado.

## Pasos seguidos durante el proyecto

1. **Lectura y análisis del enunciado.** Se revisaron los 40 ejercicios y se agruparon
   por tema para planificar el trabajo:

   | Ejercicios | Tema |
   |------------|------|
   | 1, 3, 5, 6, 25, 27–30, 32 | Funciones, cadenas, listas y diccionarios |
   | 2, 4, 7, 9, 12–14, 16, 18, 20 | `map()` y `filter()` |
   | 15, 19, 21, 26, 33 | Funciones `lambda` |
   | 17, 22–24 | `reduce()` (módulo `functools`) |
   | 8, 10, 11, 31 | Excepciones (`try/except`, excepciones personalizadas) |
   | 34, 36 | Clases y programación orientada a objetos |
   | 37 | Funciones con argumentos variables (`*args`) |
   | 38–41 | Condicionales (`if/elif/else`) |

2. **Resolución de cada ejercicio** en una función independiente, con nombre
   descriptivo, *docstring* y el enunciado como comentario encima.

3. **Separación de la lógica y la interacción.** Siempre que fue posible, la lógica
   está en funciones que reciben parámetros y devuelven un resultado (fáciles de
   probar), y la entrada por teclado (`input()`) está en funciones aparte.

4. **Gestión de errores.** Se validan los casos límite (listas vacías, divisiones por
   cero, valores no numéricos, rangos inválidos, saldo insuficiente...) y se crearon
   excepciones personalizadas: `ListaVaciaError`, `EdadFueraDeRangoError`,
   `NombreNoEncontradoError` y `ErrorBancario`.

5. **Pruebas.** Se escribió una función `main()` con ejemplos para cada ejercicio, y
   se probaron los programas interactivos con entradas válidas e inválidas.

6. **Revisión de buenas prácticas** (ver más abajo) y documentación en este README.

## Conocimientos demostrados

- **Tipos de datos básicos y funciones incorporadas:** `len`, `sum`, `max`, `sorted`,
  `str`, `int`, `float`, `isinstance`, `zip`...
- **Estructuras de datos y sus métodos:** listas, diccionarios, tuplas y conjuntos
  (`append`, `pop`, `get`, `split`, `join`, `startswith`...).
- **Condicionales:** `if/elif/else` en los ejercicios 38–41 y en el resto de validaciones.
- **Estructuras de iteración:** bucles `for` y `while`, y comprensiones de listas.
- **Funciones:** parámetros opcionales (`nota_aprobado=5`), `*args`, recursividad,
  `lambda`, `map`, `filter` y `reduce`.
- **Clases y POO:** `Arbol` y `UsuarioBanco` con atributos, métodos y `__str__`.
- **Módulos:** `math` (para `pi`) y `functools` (para `reduce`).
- **Buenas prácticas:** nombres descriptivos en `snake_case`, *docstrings*, constantes
  en mayúsculas, funciones pequeñas con una única responsabilidad, uso de
  `if __name__ == "__main__":` y manejo explícito de errores.

## Decisiones de diseño y supuestos

Algunos enunciados admitían varias interpretaciones. Estas son las decisiones tomadas:

- **Ej. 7:** cada tupla se convierte en su representación como texto con `str`
  (por ejemplo, `(1, 2)` → `"(1, 2)"`).
- **Ej. 19:** "filtrar los números impares" se ha interpretado como *quedarse* con los
  impares.
- **Ej. 20:** se excluyen los booleanos, ya que en Python `True` es técnicamente un `int`.
- **Ej. 24:** la diferencia total se calcula como `n0 - n1 - n2 - ...`.
- **Ej. 36:** `transferir_dinero(otro_usuario, cantidad)` mueve dinero *desde*
  `otro_usuario` *hacia* el usuario actual. Si la retirada falla, no se modifica
  ningún saldo. En el caso de uso, Bob tiene 70 tras ingresar 20, así que la
  transferencia de 80 falla por saldo insuficiente; el error se captura y se muestra.
- **Ej. 38:** noche de 21:00 a 5:59, día de 6:00 a 11:59 y tarde de 12:00 a 20:59.
- **Ej. 41:** un cupón no válido (≤ 0) no se aplica, y el precio final nunca baja de 0 €.

## Autor

_Tu nombre_ — Proyecto del módulo de Python.
