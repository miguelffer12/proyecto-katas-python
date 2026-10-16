"""PROYECTO LÓGICA: Katas de Python.

Cada ejercicio va encabezado con un comentario con su enunciado.
Al final del archivo hay una función main() que comprueba todos los ejercicios.
Los ejercicios que piden datos al usuario se ejecutan solo si el usuario lo desea.
"""

import math
from functools import reduce


# ---------------------------------------------------------------------------
# 1. Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
# ---------------------------------------------------------------------------
def frecuencia_letras(texto):
    """Devuelve un diccionario {letra: nº de apariciones}, ignorando espacios."""
    frecuencias = {}
    for caracter in texto:
        if caracter != " ":
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias


# ---------------------------------------------------------------------------
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada
# valor. Usa la función map()
# ---------------------------------------------------------------------------
def doble_de_cada_valor(numeros):
    """Devuelve una lista con el doble de cada número."""
    return list(map(lambda numero: numero * 2, numeros))


# ---------------------------------------------------------------------------
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo
# como parámetros. La función debe devolver una lista con todas las palabras de
# la lista original que contengan la palabra objetivo.
# ---------------------------------------------------------------------------
def palabras_que_contienen(palabras, objetivo):
    """Devuelve las palabras de la lista que contienen la palabra objetivo."""
    return [palabra for palabra in palabras if objetivo in palabra]


# ---------------------------------------------------------------------------
# 4. Genera una función que calcule la diferencia entre los valores de dos
# listas. Usa la función map()
# ---------------------------------------------------------------------------
def diferencia_listas(lista_a, lista_b):
    """Resta elemento a elemento: lista_a[i] - lista_b[i]."""
    return list(map(lambda a, b: a - b, lista_a, lista_b))


# ---------------------------------------------------------------------------
# 5. Ecribe una función que tome una lista de números como parámetro y un
# valor opcional nota_aprobado, que por defecto es 5. La función debe calcular
# la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario,
# será "suspenso". La función debe devolver una tupla que contenga la media y
# el estado.
# ---------------------------------------------------------------------------
def media_y_estado(numeros, nota_aprobado=5):
    """Devuelve la tupla (media, estado) según la nota de aprobado."""
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# ---------------------------------------------------------------------------
# 6. Escribe una función que calcule el factorial de un número de manera
# recursiva.
# ---------------------------------------------------------------------------
def factorial(n):
    """Calcula n! de forma recursiva."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


# ---------------------------------------------------------------------------
# 7. Genera una función que convierta una lista de tuplas a una lista de
# strings. Usa la función map()
# ---------------------------------------------------------------------------
def tuplas_a_strings(lista_tuplas):
    """Convierte cada tupla de la lista en su representación como string."""
    return list(map(str, lista_tuplas))


# ---------------------------------------------------------------------------
# 8. Escribe un programa que pida al usuario dos números e intente
# dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por
# cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un
# mensaje indicando si la división fue exitosa o no.
# ---------------------------------------------------------------------------
def dividir_dos_numeros():
    """Pide dos números al usuario y los divide gestionando los errores."""
    try:
        dividendo = float(input("Introduce el primer número: "))
        divisor = float(input("Introduce el segundo número: "))
        resultado = dividendo / divisor
    except ValueError:
        print("Error: debes introducir valores numéricos.")
        print("La división NO fue exitosa.")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
        print("La división NO fue exitosa.")
    else:
        print(f"La división fue exitosa: {dividendo} / {divisor} = {resultado}")


# ---------------------------------------------------------------------------
# 9. Escribe una función que tome una lista de nombres de mascotas como
# parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas
# en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()
# ---------------------------------------------------------------------------
MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


def excluir_mascotas_prohibidas(mascotas):
    """Devuelve las mascotas que no están prohibidas en España."""
    return list(filter(lambda mascota: mascota not in MASCOTAS_PROHIBIDAS, mascotas))


# ---------------------------------------------------------------------------
# 10. Escribe una función que reciba una lista de números y calcule su
# promedio. Si la lista está vacía, lanza una excepción personalizada y maneja
# el error adecuadamente.
# ---------------------------------------------------------------------------
class ListaVaciaError(Exception):
    """Se lanza al intentar calcular el promedio de una lista vacía."""


def calcular_promedio(numeros):
    """Calcula el promedio; lanza ListaVaciaError si la lista está vacía."""
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


# ---------------------------------------------------------------------------
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el
# usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
# ---------------------------------------------------------------------------
class EdadFueraDeRangoError(ValueError):
    """Se lanza cuando la edad no está entre 0 y 120."""


def pedir_edad():
    """Pide la edad hasta que el usuario introduzca un valor válido."""
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 0 or edad > 120:
                raise EdadFueraDeRangoError("La edad debe estar entre 0 y 120.")
        except EdadFueraDeRangoError as error:
            print(f"Error: {error}")
        except ValueError:
            print("Error: debes introducir un número entero.")
        else:
            print(f"Tu edad es {edad} años.")
            return edad


# ---------------------------------------------------------------------------
# 12. Genera una función que al recibir una frase devuelva una lista con la
# longitud de cada palabra. Usa la función map()
# ---------------------------------------------------------------------------
def longitud_de_palabras(frase):
    """Devuelve la longitud de cada palabra de la frase."""
    return list(map(len, frase.split()))


# ---------------------------------------------------------------------------
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una
# lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no
# pueden estar repetidas. Usa la función map()
# ---------------------------------------------------------------------------
def letras_mayuscula_minuscula(caracteres):
    """Devuelve [(MAYÚSCULA, minúscula), ...] sin letras repetidas."""
    letras_unicas = sorted({c.lower() for c in caracteres if c.isalpha()})
    return list(map(lambda letra: (letra.upper(), letra), letras_unicas))


# ---------------------------------------------------------------------------
# 14. Crea una función que retorne las palabras de una lista de palabras que
# comience con una letra en especifico. Usa la función filter()
# ---------------------------------------------------------------------------
def palabras_que_comienzan_con(palabras, letra):
    """Devuelve las palabras que empiezan por la letra indicada."""
    return list(filter(lambda p: p.lower().startswith(letra.lower()), palabras))


# ---------------------------------------------------------------------------
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
# ---------------------------------------------------------------------------
sumar_tres = lambda lista: [numero + 3 for numero in lista]  # noqa: E731


# ---------------------------------------------------------------------------
# 16. Escribe una función que tome una cadena de texto y un número entero n
# como parámetros y devuelva una lista de todas las palabras que sean más
# largas que n. Usa la función filter()
# ---------------------------------------------------------------------------
def palabras_mas_largas_que(texto, n):
    """Devuelve las palabras del texto con más de n caracteres."""
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# ---------------------------------------------------------------------------
# 17. Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos
# setenta y dos (572). Usa la función reduce()
# ---------------------------------------------------------------------------
def digitos_a_numero(digitos):
    """Convierte una lista de dígitos en el número que representan."""
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos, 0)


# ---------------------------------------------------------------------------
# 18. Escribe un programa en Python que cree una lista de diccionarios que
# contenga información de estudiantes (nombre, edad, calificación) y use la
# función filter para extraer a los estudiantes con una calificación mayor o
# igual a 90. Usa la función filter()
# ---------------------------------------------------------------------------
def estudiantes_sobresalientes():
    """Crea una lista de estudiantes y devuelve los de calificación >= 90."""
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 78},
        {"nombre": "Marta", "edad": 21, "calificacion": 90},
        {"nombre": "Pablo", "edad": 23, "calificacion": 64},
    ]
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))


# ---------------------------------------------------------------------------
# 19. Crea una función lambda que filtre los números impares de una lista dada.
# ---------------------------------------------------------------------------
filtrar_impares = lambda lista: list(filter(lambda n: n % 2 != 0, lista))  # noqa: E731


# ---------------------------------------------------------------------------
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista
# sólo con los valores int. Usa la función filter()
# ---------------------------------------------------------------------------
def solo_enteros(elementos):
    """Devuelve únicamente los elementos de tipo int."""
    return list(filter(lambda e: isinstance(e, int) and not isinstance(e, bool), elementos))


# ---------------------------------------------------------------------------
# 21. Crea una función que calcule el cubo de un número dado mediante una
# función lambda
# ---------------------------------------------------------------------------
def cubo(numero):
    """Calcula el cubo de un número usando una lambda."""
    calcular_cubo = lambda x: x ** 3  # noqa: E731
    return calcular_cubo(numero)


# ---------------------------------------------------------------------------
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha
# lista. Usa la función reduce().
# ---------------------------------------------------------------------------
def producto_total(numeros):
    """Multiplica todos los valores de la lista."""
    return reduce(lambda a, b: a * b, numeros, 1)


# ---------------------------------------------------------------------------
# 23. Concatena una lista de palabras. Usa la función reduce().
# ---------------------------------------------------------------------------
def concatenar_palabras(palabras):
    """Concatena todas las palabras de la lista en un único string."""
    return reduce(lambda a, b: a + b, palabras, "")


# ---------------------------------------------------------------------------
# 24. Calcula la diferencia total en los valores de una lista. Usa la función
# reduce().
# ---------------------------------------------------------------------------
def diferencia_total(numeros):
    """Resta consecutivamente todos los valores: n0 - n1 - n2 - ..."""
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return reduce(lambda a, b: a - b, numeros)


# ---------------------------------------------------------------------------
# 25. Crea una función que cuente el número de caracteres en una cadena de
# texto dada.
# ---------------------------------------------------------------------------
def contar_caracteres(texto):
    """Devuelve el número de caracteres del texto."""
    return len(texto)


# ---------------------------------------------------------------------------
# 26. Crea una función lambda que calcule el resto de la división entre dos
# números dados.
# ---------------------------------------------------------------------------
resto_division = lambda a, b: a % b  # noqa: E731


# ---------------------------------------------------------------------------
# 27. Crea una función que calcule el promedio de una lista de números.
# ---------------------------------------------------------------------------
def promedio(numeros):
    """Devuelve el promedio de una lista de números."""
    return sum(numeros) / len(numeros)


# ---------------------------------------------------------------------------
# 28. Crea una función que busque y devuelva el primer elemento duplicado en
# una lista dada.
# ---------------------------------------------------------------------------
def primer_duplicado(elementos):
    """Devuelve el primer elemento que aparece repetido, o None si no hay."""
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# ---------------------------------------------------------------------------
# 29. Crea una función que convierta una variable en una cadena de texto y
# enmascare todos los caracteres con el carácter '#', excepto los últimos
# cuatro.
# ---------------------------------------------------------------------------
def enmascarar(variable):
    """Convierte a texto y sustituye por '#' todo salvo los últimos 4 caracteres."""
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]


# ---------------------------------------------------------------------------
# 30. Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.
# ---------------------------------------------------------------------------
def son_anagramas(palabra_1, palabra_2):
    """Indica si las dos palabras tienen las mismas letras (ignora mayúsculas y espacios)."""
    normalizar = lambda p: sorted(p.replace(" ", "").lower())  # noqa: E731
    return normalizar(palabra_1) == normalizar(palabra_2)


# ---------------------------------------------------------------------------
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y
# luego solicite un nombre para buscar en esa lista. Si el nombre está en la
# lista, se imprime un mensaje indicando que fue encontrado, de lo contrario,
# se lanza una excepción.
# ---------------------------------------------------------------------------
class NombreNoEncontradoError(Exception):
    """Se lanza cuando el nombre buscado no está en la lista."""


def buscar_nombre():
    """Pide una lista de nombres y un nombre a buscar."""
    entrada = input("Introduce una lista de nombres separados por comas: ")
    nombres = [nombre.strip() for nombre in entrada.split(",") if nombre.strip()]
    buscado = input("Introduce el nombre a buscar: ").strip()

    if buscado in nombres:
        print(f"¡El nombre '{buscado}' fue encontrado!")
    else:
        raise NombreNoEncontradoError(f"El nombre '{buscado}' no está en la lista.")


# ---------------------------------------------------------------------------
# 32. Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre completo en la lista y devuelve el puesto del empleado si
# está en la lista, de lo contrario, devuelve un mensaje indicando que la
# persona no trabaja aquí.
# ---------------------------------------------------------------------------
def buscar_puesto(nombre_completo, empleados):
    """Busca al empleado por nombre completo y devuelve su puesto."""
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."


# ---------------------------------------------------------------------------
# 33. Crea una función lambda que sume elementos correspondientes de dos
# listas dadas.
# ---------------------------------------------------------------------------
sumar_listas = lambda lista_a, lista_b: [a + b for a, b in zip(lista_a, lista_b)]  # noqa: E731


# ---------------------------------------------------------------------------
# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como
# atributos. Los métodos disponibles son: crecer_tronco, nueva_rama,
# crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos
# métodos para manipular la estructura del árbol.
#
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de
#    ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco
#    en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud
#    1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la
#    longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición
#    específica.
# 6. Implementar el método info_arbol para devolver información sobre la
#    longitud del tronco, el número de ramas y las longitudes de las mismas.
#
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.
# ---------------------------------------------------------------------------
class Arbol:
    """Árbol genérico con un tronco y una lista de ramas."""

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Añade una nueva rama de longitud 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama situada en la posición indicada."""
        if not 0 <= posicion < len(self.ramas):
            raise IndexError(f"No existe ninguna rama en la posición {posicion}.")
        self.ramas.pop(posicion)

    def info_arbol(self):
        """Devuelve la longitud del tronco, el nº de ramas y sus longitudes."""
        return {
            "longitud_tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitud_ramas": list(self.ramas),
        }


def caso_de_uso_arbol():
    """Ejecuta el caso de uso del enunciado y devuelve la información final."""
    arbol = Arbol()            # 1. Crear un árbol
    arbol.crecer_tronco()      # 2. Crecer el tronco una unidad
    arbol.nueva_rama()         # 3. Añadir una rama
    arbol.crecer_ramas()       # 4. Crecer todas las ramas una unidad
    arbol.nueva_rama()         # 5. Añadir dos ramas nuevas
    arbol.nueva_rama()
    arbol.quitar_rama(2)       # 6. Retirar la rama de la posición 2
    return arbol.info_arbol()  # 7. Obtener información


# ---------------------------------------------------------------------------
# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su
# nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para
# realizar operaciones como retirar dinero, transferir dinero desde otro
# usuario y agregar dinero al saldo.
#
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta
#    corriente mediante True y False.
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del
#    usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia
#    desde otro usuario al usuario actual. Lanzará un error en caso de no
#    poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del
#    usuario.
#
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo
#    inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".
# ---------------------------------------------------------------------------
class ErrorBancario(Exception):
    """Error al realizar una operación bancaria."""


class UsuarioBanco:
    """Usuario de un banco con nombre, saldo y cuenta corriente (True/False)."""

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Retira dinero del saldo; lanza ErrorBancario si no es posible."""
        if cantidad <= 0:
            raise ErrorBancario("La cantidad a retirar debe ser mayor que cero.")
        if not self.cuenta_corriente:
            raise ErrorBancario(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ErrorBancario(
                f"Saldo insuficiente: {self.nombre} tiene {self.saldo} y quiere retirar {cantidad}."
            )
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro_usuario hacia este usuario."""
        if not self.cuenta_corriente:
            raise ErrorBancario(f"{self.nombre} no tiene cuenta corriente para recibir la transferencia.")
        otro_usuario.retirar_dinero(cantidad)  # Si falla, no se modifica ningún saldo
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        """Añade dinero al saldo del usuario."""
        if cantidad <= 0:
            raise ErrorBancario("La cantidad a agregar debe ser mayor que cero.")
        self.saldo += cantidad

    def __str__(self):
        return f"{self.nombre}: saldo = {self.saldo}"


def caso_de_uso_banco():
    """Ejecuta el caso de uso del enunciado mostrando el estado en cada paso."""
    alicia = UsuarioBanco("Alicia", 100, True)  # 1. Crear usuarios
    bob = UsuarioBanco("Bob", 50, True)
    print(alicia, "|", bob)

    bob.agregar_dinero(20)                      # 2. Agregar 20 a Bob
    print("Tras agregar 20 a Bob:", bob)

    try:                                        # 3. Transferencia de 80 de Bob a Alicia
        alicia.transferir_dinero(bob, 80)
        print("Transferencia realizada:", alicia, "|", bob)
    except ErrorBancario as error:
        print(f"No se pudo realizar la transferencia: {error}")

    try:                                        # 4. Retirar 50 a Alicia
        alicia.retirar_dinero(50)
        print("Retirada realizada:", alicia)
    except ErrorBancario as error:
        print(f"No se pudo retirar el dinero: {error}")


# ---------------------------------------------------------------------------
# 37. Crea una función llamada procesar_texto que procesa un texto según la
# opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra.
# Estas opciones son otras funciones que tenemos que definir primero y llamar
# dentro de la función procesar_texto.
#
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que
#    aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original
#    del texto por una palabra_nueva. Tiene que devolver el texto con el
#    remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto.
#    Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción (entre
#    "contar", "reemplazar", "eliminar") y un número de argumentos variable
#    según la opción indicada.
#
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
# ---------------------------------------------------------------------------
def contar_palabras(texto):
    """Devuelve un diccionario {palabra: nº de apariciones}."""
    conteo = {}
    for palabra in texto.lower().split():
        palabra = palabra.strip(".,;:!?¡¿\"'()")
        if palabra:
            conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Devuelve el texto sustituyendo palabra_original por palabra_nueva."""
    return " ".join(
        palabra_nueva if palabra == palabra_original else palabra
        for palabra in texto.split()
    )


def eliminar_palabra(texto, palabra):
    """Devuelve el texto sin la palabra indicada."""
    return " ".join(p for p in texto.split() if p != palabra)


def procesar_texto(texto, opcion, *args):
    """Procesa el texto según la opción: "contar", "reemplazar" o "eliminar"."""
    if opcion == "contar":
        return contar_palabras(texto)
    if opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("La opción 'reemplazar' necesita palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, *args)
    if opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("La opción 'eliminar' necesita la palabra a eliminar.")
        return eliminar_palabra(texto, *args)
    raise ValueError(f"Opción no válida: '{opcion}'. Usa 'contar', 'reemplazar' o 'eliminar'.")


# ---------------------------------------------------------------------------
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la
# hora proporcionada por el usuario.
# ---------------------------------------------------------------------------
def momento_del_dia(hora):
    """Clasifica una hora (0-23): noche (21-5), día (6-11) o tarde (12-20)."""
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if hora < 6 or hora >= 21:
        return "de noche"
    elif hora < 12:
        return "de día"
    else:
        return "tarde"


def programa_momento_del_dia():
    """Pide una hora al usuario y muestra el momento del día."""
    try:
        hora = int(input("Introduce la hora (0-23): "))
        print(f"A las {hora}h es {momento_del_dia(hora)}.")
    except ValueError as error:
        print(f"Error: {error if 'entre' in str(error) else 'introduce un número entero.'}")


# ---------------------------------------------------------------------------
# 39. Escribe un programa que determine qué calificación en texto tiene un
# alumno en base a su calificación numérica. Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
# ---------------------------------------------------------------------------
def calificacion_en_texto(nota):
    """Convierte una nota numérica (0-100) en su calificación en texto."""
    if not 0 <= nota <= 100:
        raise ValueError("La nota debe estar entre 0 y 100.")
    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"


def programa_calificacion():
    """Pide una nota al usuario y muestra su calificación en texto."""
    try:
        nota = float(input("Introduce la calificación numérica (0-100): "))
        print(f"Calificación: {calificacion_en_texto(nota)}")
    except ValueError as error:
        print(f"Error: {error if 'entre' in str(error) else 'introduce un número.'}")


# ---------------------------------------------------------------------------
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede
# ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos
# necesarios para calcular el área de la figura).
# ---------------------------------------------------------------------------
def calcular_area(figura, datos):
    """Calcula el área de una figura.

    - "rectangulo": datos = (base, altura)
    - "circulo": datos = (radio,)
    - "triangulo": datos = (base, altura)
    """
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    if figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    if figura == "triangulo":
        base, altura = datos
        return base * altura / 2
    raise ValueError(f"Figura no reconocida: '{figura}'.")


# ---------------------------------------------------------------------------
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que
# utilice condicionales para determinar el monto final de una compra en una
# tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de
#    descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el
#    valor del cupón sea válido (es decir, mayor a cero). Por ejemplo,
#    descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento
#    aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else
#    para llevar a cabo estas acciones en tu programa de Python.
# ---------------------------------------------------------------------------
def calcular_compra():
    """Calcula el precio final de una compra aplicando un cupón si es válido."""
    try:
        precio = float(input("Introduce el precio original del artículo (€): "))
        if precio < 0:
            print("Error: el precio no puede ser negativo.")
            return
        respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        precio_final = precio
        if respuesta in ("si", "sí"):
            descuento = float(input("Introduce el valor del cupón de descuento (€): "))
            if descuento > 0:
                precio_final = max(precio - descuento, 0)
                print(f"Descuento aplicado: {descuento:.2f}€")
            else:
                print("El cupón no es válido (debe ser mayor que cero). No se aplica descuento.")
        elif respuesta == "no":
            print("Compra sin descuento.")
        else:
            print("Respuesta no reconocida. No se aplica descuento.")

        print(f"Precio final de la compra: {precio_final:.2f}€")
    except ValueError:
        print("Error: debes introducir un valor numérico.")


# ---------------------------------------------------------------------------
# Comprobación de los ejercicios
# ---------------------------------------------------------------------------
def titulo(numero, texto):
    """Imprime una cabecera para separar la salida de cada ejercicio."""
    print(f"\n--- Ejercicio {numero}: {texto} ---")


def main():
    """Ejecuta una comprobación de cada ejercicio."""
    titulo(1, "Frecuencia de letras")
    print(frecuencia_letras("hola mundo"))

    titulo(2, "Doble de cada valor")
    print(doble_de_cada_valor([1, 2, 3, 4]))

    titulo(3, "Palabras que contienen el objetivo")
    print(palabras_que_contienen(["casa", "casco", "perro", "cascada"], "cas"))

    titulo(4, "Diferencia entre listas")
    print(diferencia_listas([10, 20, 30], [1, 2, 3]))

    titulo(5, "Media y estado")
    print(media_y_estado([6, 7, 8]))
    print(media_y_estado([2, 3, 4]))
    print(media_y_estado([6, 7, 8], nota_aprobado=8))

    titulo(6, "Factorial recursivo")
    print(f"5! = {factorial(5)}")

    titulo(7, "Tuplas a strings")
    print(tuplas_a_strings([(1, 2), ("a", "b"), (3.5, True)]))

    titulo(9, "Mascotas permitidas")
    print(excluir_mascotas_prohibidas(["Perro", "Tigre", "Gato", "Oso", "Loro"]))

    titulo(10, "Promedio con excepción personalizada")
    for lista in ([4, 8, 12], []):
        try:
            print(f"Promedio de {lista}: {calcular_promedio(lista)}")
        except ListaVaciaError as error:
            print(f"Error: {error}")

    titulo(12, "Longitud de cada palabra")
    print(longitud_de_palabras("Python es un lenguaje genial"))

    titulo(13, "Letras en mayúsculas y minúsculas")
    print(letras_mayuscula_minuscula("Hello World"))

    titulo(14, "Palabras que empiezan por una letra")
    print(palabras_que_comienzan_con(["sol", "luna", "estrella", "Sirio"], "s"))

    titulo(15, "Sumar 3 con lambda")
    print(sumar_tres([1, 2, 3]))

    titulo(16, "Palabras más largas que n")
    print(palabras_mas_largas_que("el elefante cruzó el río lentamente", 4))

    titulo(17, "Dígitos a número con reduce")
    print(digitos_a_numero([5, 7, 2]))

    titulo(18, "Estudiantes con calificación >= 90")
    print(estudiantes_sobresalientes())

    titulo(19, "Filtrar impares con lambda")
    print(filtrar_impares([1, 2, 3, 4, 5, 6, 7]))

    titulo(20, "Solo valores int")
    print(solo_enteros([1, "hola", 2, "mundo", 3]))

    titulo(21, "Cubo con lambda")
    print(cubo(3))

    titulo(22, "Producto total con reduce")
    print(producto_total([1, 2, 3, 4, 5]))

    titulo(23, "Concatenar palabras con reduce")
    print(concatenar_palabras(["Hola", " ", "mundo", "!"]))

    titulo(24, "Diferencia total con reduce")
    print(diferencia_total([100, 20, 5]))

    titulo(25, "Contar caracteres")
    print(contar_caracteres("Python"))

    titulo(26, "Resto con lambda")
    print(resto_division(17, 5))

    titulo(27, "Promedio de una lista")
    print(promedio([2, 4, 6, 8]))

    titulo(28, "Primer elemento duplicado")
    print(primer_duplicado([3, 1, 4, 1, 5, 9, 3]))
    print(primer_duplicado([1, 2, 3]))

    titulo(29, "Enmascarar")
    print(enmascarar(1234567890))
    print(enmascarar("contraseña"))

    titulo(30, "Anagramas")
    print(son_anagramas("Roma", "Amor"))
    print(son_anagramas("hola", "adiós"))

    titulo(32, "Puesto de un empleado")
    empleados = [
        {"nombre": "Ana García", "puesto": "Desarrolladora"},
        {"nombre": "Luis Pérez", "puesto": "Analista de datos"},
    ]
    print(buscar_puesto("Ana García", empleados))
    print(buscar_puesto("Pedro Ruiz", empleados))

    titulo(33, "Sumar listas con lambda")
    print(sumar_listas([1, 2, 3], [10, 20, 30]))

    titulo(34, "Clase Arbol")
    print(caso_de_uso_arbol())

    titulo(36, "Clase UsuarioBanco")
    caso_de_uso_banco()

    titulo(37, "procesar_texto")
    texto = "el gato y el perro juegan con el gato"
    print(procesar_texto(texto, "contar"))
    print(procesar_texto(texto, "reemplazar", "gato", "pájaro"))
    print(procesar_texto(texto, "eliminar", "el"))
    try:
        procesar_texto(texto, "invertir")
    except ValueError as error:
        print(f"Error: {error}")

    titulo(38, "Momento del día (hora 8, 15 y 23)")
    print([momento_del_dia(hora) for hora in (8, 15, 23)])

    titulo(39, "Calificación en texto (65, 75, 85, 95)")
    print([calificacion_en_texto(nota) for nota in (65, 75, 85, 95)])

    titulo(40, "Área de figuras")
    print(f"Rectángulo 4x5: {calcular_area('rectangulo', (4, 5))}")
    print(f"Círculo r=3: {calcular_area('circulo', (3,)):.2f}")
    print(f"Triángulo 6x4: {calcular_area('triangulo', (6, 4))}")

    # Ejercicios interactivos (piden datos por teclado)
    opcion = input("\n¿Quieres probar los ejercicios interactivos (8, 11, 31, 38, 39, 41)? (s/n): ")
    if opcion.strip().lower() in ("s", "si", "sí"):
        titulo(8, "División de dos números")
        dividir_dos_numeros()

        titulo(11, "Pedir edad")
        pedir_edad()

        titulo(31, "Buscar un nombre en una lista")
        try:
            buscar_nombre()
        except NombreNoEncontradoError as error:
            print(f"Error: {error}")

        titulo(38, "Momento del día")
        programa_momento_del_dia()

        titulo(39, "Calificación en texto")
        programa_calificacion()

        titulo(41, "Compra con descuento")
        calcular_compra()


if __name__ == "__main__":
    main()
