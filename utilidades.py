def mostrar_titulo(t):
    """Muestra un título bonito con líneas por consola.

    Args:
        t: El texto que queremos poner como título.
    """
    print("\n============================")
    print(t)
    print("============================")


def pedir_numero(mensaje):
    """Pide un número al usuario por teclado y controla que no ponga letras.

    Args:
        mensaje: El texto que ve el usuario para pedirle el número.

    Returns:
        El número entero que ha escrito o un 0 si se ha equivocado.
    """
    valor = input(mensaje)
    try:
        return int(valor)
    except ValueError:
        print("Número no válido. Se usará 0")
        return 0


def formatear_moneda(x):
    """Redondea un número y le añade el símbolo del euro al final.

    Args:
        x: El número con los decimales.

    Returns:
        El texto con el dinero bien puesto y el €.
    """
    return str(round(x, 2)) + " €"
