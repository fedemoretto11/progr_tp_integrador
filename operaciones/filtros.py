from utils.input import pedir_entero, pedir_opcion_menu
from utils.prompts import (
    PROMPT_FILTRO_CONTINENTE, PROMPT_FILTRO_POBLACION_MINIMA,
    PROMPT_FILTRO_POBLACION_MAXIMA, PROMPT_FILTRO_SUPERFICIE_MINIMA,
    PROMPT_FILTRO_SUPERFICIE_MAXIMA, LABEL_CONTINENTES_DISPONIBLES, FORMAT_CONTADOR
)
from utils.error_messages import (
    MSG_NO_PAISES_CARGADOS,
    MSG_ERROR_PAISES_RANGO_POBLACION,
    MSG_ERROR_PAISES_RANGO_SUPERFICIE,
)
from utils.validaciones import (
    validar_no_vacio,
    validar_rango_poblacion,
    validar_rango_superficie,
)
from typing import List, Dict

def filtrar_por_continente(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """filtrar_por_continente: Filtra países por continente seleccionado."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    continentes = []
    for pais in paises:
        continente = pais["continente"].strip()
        if continente not in continentes:
            continentes.append(continente)
    
    print(LABEL_CONTINENTES_DISPONIBLES)
    
    opciones_formateadas = []
    for continente in continentes:
        count = sum(1 for p in paises if p["continente"].strip() == continente)
        opciones_formateadas.append(f"{continente}{FORMAT_CONTADOR.format(count=count)}")
    
    opcion = pedir_opcion_menu(opciones_formateadas, PROMPT_FILTRO_CONTINENTE)
    continente_seleccionado = continentes[opcion - 1]
    paises_filtrados = [p for p in paises if p["continente"].strip() == continente_seleccionado]
    
    validar_no_vacio(paises_filtrados, f"No hay paises en {continente_seleccionado}")
    
    return paises_filtrados

def filtrar_por_rango_poblacion(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """filtrar_por_rango_poblacion: Filtra países por rango de población (inclusivo)."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    while True:
        try:
            poblacion_min = pedir_entero(PROMPT_FILTRO_POBLACION_MINIMA)
            poblacion_max = pedir_entero(PROMPT_FILTRO_POBLACION_MAXIMA)
            
            validar_rango_poblacion(poblacion_min, poblacion_max)
            
            paises_filtrados = [p for p in paises if poblacion_min <= p["poblacion"] <= poblacion_max]
            
            validar_no_vacio(
                paises_filtrados, 
                MSG_ERROR_PAISES_RANGO_POBLACION.format(min=poblacion_min, max=poblacion_max)
            )
            
            return paises_filtrados
        except ValueError as error:
            print(f"Error: {error}")

def filtrar_por_rango_superficie(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """filtrar_por_rango_superficie: Filtra países por rango de superficie (inclusivo)."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    while True:
        try:
            superficie_min = pedir_entero(PROMPT_FILTRO_SUPERFICIE_MINIMA)
            superficie_max = pedir_entero(PROMPT_FILTRO_SUPERFICIE_MAXIMA)
            
            validar_rango_superficie(superficie_min, superficie_max)
            
            paises_filtrados = [p for p in paises if superficie_min <= p["superficie"] <= superficie_max]
            
            validar_no_vacio(
                paises_filtrados, 
                MSG_ERROR_PAISES_RANGO_SUPERFICIE.format(min=superficie_min, max=superficie_max)
            )
            
            return paises_filtrados
        except ValueError as error:
            print(f"Error: {error}")
