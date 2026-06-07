from utils.messages import MSG_ERROR_ENTERO, MSG_ERROR_CAMPO_VACIO

def pedir_entero(mensaje: str) -> int:
    """Solicita un número entero al usuario."""
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        raise ValueError(MSG_ERROR_ENTERO)

def pedir_texto(mensaje: str) -> str:
    """Solicita un texto no vacío al usuario."""
    try:
        texto = input(mensaje).strip()
        if texto == "":
            raise ValueError(MSG_ERROR_CAMPO_VACIO)
        return texto
    except ValueError:
        raise
