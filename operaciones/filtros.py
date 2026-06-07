from utils.input import pedir_entero
from utils.prompts import (
    PROMPT_FILTRO_CONTINENTE, PROMPT_FILTRO_POBLACION_MINIMA,
    PROMPT_FILTRO_POBLACION_MAXIMA, PROMPT_FILTRO_SUPERFICIE_MINIMA,
    PROMPT_FILTRO_SUPERFICIE_MAXIMA, LABEL_CONTINENTES_DISPONIBLES, FORMAT_CONTADOR
)
from utils.messages import (
    MSG_NO_PAISES_CARGADOS,
    MSG_OPCION_INVALIDA,
    MSG_SELECCION_INVALIDA,
    MSG_ERROR_POBLACION_POSITIVA,
    MSG_ERROR_RANGO_POBLACION,
    MSG_ERROR_PAISES_RANGO_POBLACION,
    MSG_ERROR_SUPERFICIE_POSITIVA,
    MSG_ERROR_RANGO_SUPERFICIE,
    MSG_ERROR_PAISES_RANGO_SUPERFICIE,
)
from typing import List, Dict

def filtrar_por_continente(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """Filtra países por continente seleccionado."""
    if not paises:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    
    continentes = []
    for pais in paises:
        continente = pais["continente"].strip()
        if continente not in continentes:
            continentes.append(continente)
    
    print(LABEL_CONTINENTES_DISPONIBLES)
    for i, continente in enumerate(continentes, 1):
        count = sum(1 for p in paises if p["continente"].strip() == continente)
        print(f"{i}. {continente}{FORMAT_CONTADOR.format(count=count)}")
    
    try:
        opcion = pedir_entero(PROMPT_FILTRO_CONTINENTE)
        if opcion < 1 or opcion > len(continentes):
            raise ValueError(MSG_OPCION_INVALIDA)
        
        continente_seleccionado = continentes[opcion - 1]
        paises_filtrados = [p for p in paises if p["continente"].strip() == continente_seleccionado]
        
        if not paises_filtrados:
            raise ValueError(f"No hay paises en {continente_seleccionado}")
        
        return paises_filtrados
    except (ValueError, IndexError) as e:
        raise ValueError(f"{MSG_SELECCION_INVALIDA}: {str(e)}")

def filtrar_por_rango_poblacion(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """Filtra países por rango de población (inclusivo)."""
    if not paises:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    
    poblacion_min = pedir_entero(PROMPT_FILTRO_POBLACION_MINIMA)
    poblacion_max = pedir_entero(PROMPT_FILTRO_POBLACION_MAXIMA)
    
    if poblacion_min <= 0 or poblacion_max <= 0:
        raise ValueError(MSG_ERROR_POBLACION_POSITIVA)
    
    if poblacion_min > poblacion_max:
        raise ValueError(MSG_ERROR_RANGO_POBLACION)
    
    paises_filtrados = [p for p in paises if poblacion_min <= p["poblacion"] <= poblacion_max]
    
    if not paises_filtrados:
        raise ValueError(MSG_ERROR_PAISES_RANGO_POBLACION.format(min=poblacion_min, max=poblacion_max))
    
    return paises_filtrados

def filtrar_por_rango_superficie(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """Filtra países por rango de superficie (inclusivo)."""
    if not paises:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    
    superficie_min = pedir_entero(PROMPT_FILTRO_SUPERFICIE_MINIMA)
    superficie_max = pedir_entero(PROMPT_FILTRO_SUPERFICIE_MAXIMA)
    
    if superficie_min <= 0 or superficie_max <= 0:
        raise ValueError(MSG_ERROR_SUPERFICIE_POSITIVA)
    
    if superficie_min > superficie_max:
        raise ValueError(MSG_ERROR_RANGO_SUPERFICIE)
    
    paises_filtrados = [p for p in paises if superficie_min <= p["superficie"] <= superficie_max]
    
    if not paises_filtrados:
        raise ValueError(MSG_ERROR_PAISES_RANGO_SUPERFICIE.format(min=superficie_min, max=superficie_max))
    
    return paises_filtrados
