def pedir_entero(mensaje):
    """Solicita un número entero al usuario."""
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        raise ValueError("Debe ingresar un numero entero")

def pedir_texto(mensaje):
    """Solicita un texto no vacío al usuario."""
    try:
        texto = input(mensaje).strip()
        if texto == "":
            raise ValueError("El campo no puede estar vacio")
        return texto
    except ValueError:
        raise
