from utils.input import pedir_entero
from utils.prompts import PROMPT_ORDEN_DIRECCION
from utils.messages import (
    MSG_NO_PAISES_CARGADOS,
    MSG_OPCION_INVALIDA,
)
from utils.validaciones import validar_no_vacio
from typing import List, Dict

def ordenar_por_nombre(paises: List[Dict[str, int | str]], descendente: bool = False) -> List[Dict[str, int | str]]:
    """ordenar_por_nombre: Ordena países por nombre (case-insensitive)."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)

def ordenar_por_poblacion(paises: List[Dict[str, int | str]], descendente: bool = False) -> List[Dict[str, int | str]]:
    """ordenar_por_poblacion: Ordena países por población."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

def ordenar_por_superficie(paises: List[Dict[str, int | str]], descendente: bool = False) -> List[Dict[str, int | str]]:
    """ordenar_por_superficie: Ordena países por superficie."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

def pedir_direccion_orden() -> bool:
    """pedir_direccion_orden: Solicita al usuario dirección de ordenamiento."""
    try:
        opcion = pedir_entero(PROMPT_ORDEN_DIRECCION)
        if opcion == 1:
            return False
        elif opcion == 2:
            return True
        else:
            raise ValueError(MSG_OPCION_INVALIDA)
    except ValueError:
        raise
