"""Operaciones de gestión de países."""

from utils.input import pedir_texto
from utils.formatting import formato_numero
from utils.prompts import PROMPT_BUSCAR_PAIS, LABEL_LISTA_PAISES, LABEL_PAIS, LABEL_POBLACION, LABEL_SUPERFICIE, FORMAT_KM2, LABEL_CONTINENTE
from utils.error_messages import MSG_NO_PAISES_CARGADOS, MSG_ERROR_PAIS_NO_ENCONTRADO
from utils.validaciones import validar_no_vacio
from typing import List, Dict


def buscar_pais_por_nombre(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """buscar_pais_por_nombre: Busca países por nombre (coincidencia parcial, case-insensitive)."""
    try: 
        paises_a_buscar = pedir_texto(PROMPT_BUSCAR_PAIS).lower()
        paises_encontrados: List[Dict[str, int | str]] = []
        
        for pais in paises:
            if paises_a_buscar in pais["nombre"].lower():
                paises_encontrados.append(pais)
        
        if len(paises_encontrados) == 0:
            raise ValueError(MSG_ERROR_PAIS_NO_ENCONTRADO)
        
        return paises_encontrados
    except ValueError:
        raise


def mostrar_paises(paises: List[Dict[str, int | str]]) -> None:
    """mostrar_paises: Muestra todos los países con formato legible."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    print(f"\n{LABEL_LISTA_PAISES}")
    for pais in paises:
        print(f"\n{LABEL_PAIS} {pais['nombre']}")
        print(f"{LABEL_POBLACION} {formato_numero(pais['poblacion'])}")
        print(f"{LABEL_SUPERFICIE} {formato_numero(pais['superficie'])}{FORMAT_KM2}")
        print(f"{LABEL_CONTINENTE} {pais['continente']}")
        print("-----------------------------")
