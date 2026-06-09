from typing import List
from utils.error_messages import MSG_ERROR_ENTERO, MSG_ERROR_CAMPO_VACIO, MSG_OPCION_INVALIDA

def pedir_entero(mensaje: str) -> int:
    """pedir_entero: Solicita un número entero al usuario."""
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        raise ValueError(MSG_ERROR_ENTERO)

def pedir_texto(mensaje: str) -> str:
    """pedir_texto: Solicita un texto no vacío al usuario."""
    try:
        texto = input(mensaje).strip()
        if texto == "":
            raise ValueError(MSG_ERROR_CAMPO_VACIO)
        return texto
    except ValueError:
        raise


def pedir_opcion_menu(opciones: List[str], mensaje_prompt: str) -> int:
    """pedir_opcion_menu: Muestra menú y retorna opción seleccionada (1-indexed)."""
    while True:
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        
        try:
            opcion_seleccionada = pedir_entero(mensaje_prompt)
            if opcion_seleccionada not in range(1, len(opciones) + 1):
                print(MSG_OPCION_INVALIDA)
                continue
            return opcion_seleccionada
        except ValueError:
            print(MSG_OPCION_INVALIDA)
