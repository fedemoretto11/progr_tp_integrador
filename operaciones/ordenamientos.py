from utils.input import pedir_entero
from utils.prompts import PROMPT_ORDEN_DIRECCION
from utils.messages import (
    MSG_NO_PAISES_CARGADOS,
    MSG_OPCION_INVALIDA,
)
from typing import List, Dict

def ordenar_por_nombre(paises: List[Dict[str, int | str]], descendente: bool = False) -> List[Dict[str, int | str]]:
    """Sorts countries by name (case-insensitive)."""
    if not paises:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    
    return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)

def ordenar_por_poblacion(paises: List[Dict[str, int | str]], descendente: bool = False) -> List[Dict[str, int | str]]:
    """Sorts countries by population."""
    if not paises:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

def ordenar_por_superficie(paises: List[Dict[str, int | str]], descendente: bool = False) -> List[Dict[str, int | str]]:
    """Sorts countries by surface area."""
    if not paises:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

def pedir_direccion_orden() -> bool:
    """Prompts user for sort direction."""
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
