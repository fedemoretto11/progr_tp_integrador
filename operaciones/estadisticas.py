from utils.formatting import formato_numero
from utils.prompts import (
    LABEL_MAYOR_POBLACION, LABEL_MENOR_POBLACION, LABEL_DIFERENCIA,
    LABEL_PAIS, LABEL_POBLACION, LABEL_SUPERFICIE, LABEL_CONTINENTE,
    LABEL_PROMEDIO_POBLACION, LABEL_PROMEDIO_SUPERFICIE,
    LABEL_CANTIDAD_POR_CONTINENTE, LABEL_TOTAL, LABEL_PAISES,
    FORMAT_KM2
)
from utils.messages import MSG_NO_PAISES_CARGADOS
from utils.validaciones import validar_no_vacio
from typing import List, Dict


def _obtener_poblacion(pais: Dict[str, int | str]) -> int:
    """_obtener_poblacion: Obtiene población de un país."""
    return pais["poblacion"]


def estadistica_max_min_poblacion(paises: List[Dict[str, int | str]]) -> None:
    """estadistica_max_min_poblacion: Muestra país con mayor y menor población."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    max_pais = max(paises, key=_obtener_poblacion)
    min_pais = min(paises, key=_obtener_poblacion)
    
    print(f"\n{LABEL_MAYOR_POBLACION}")
    print(f"{LABEL_PAIS} {max_pais['nombre']}")
    print(f"{LABEL_POBLACION} {formato_numero(max_pais['poblacion'])}")
    print(f"{LABEL_SUPERFICIE} {formato_numero(max_pais['superficie'])}{FORMAT_KM2}")
    print(f"{LABEL_CONTINENTE} {max_pais['continente']}")
    
    print(f"\n{LABEL_MENOR_POBLACION}")
    print(f"{LABEL_PAIS} {min_pais['nombre']}")
    print(f"{LABEL_POBLACION} {formato_numero(min_pais['poblacion'])}")
    print(f"{LABEL_SUPERFICIE} {formato_numero(min_pais['superficie'])}{FORMAT_KM2}")
    print(f"{LABEL_CONTINENTE} {min_pais['continente']}")
    
    diferencia = max_pais["poblacion"] - min_pais["poblacion"]
    print(f"{LABEL_DIFERENCIA}{formato_numero(diferencia)}")

def estadistica_promedio_poblacion(paises: List[Dict[str, int | str]]) -> None:
    """estadistica_promedio_poblacion: Calcula y muestra promedio de población."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    total = sum(p["poblacion"] for p in paises)
    promedio = total / len(paises)
    
    print(f"{LABEL_PROMEDIO_POBLACION}{formato_numero(round(promedio, 2))}")

def estadistica_promedio_superficie(paises: List[Dict[str, int | str]]) -> None:
    """estadistica_promedio_superficie: Calcula y muestra promedio de superficie."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    total = sum(p["superficie"] for p in paises)
    promedio = total / len(paises)
    
    print(f"{LABEL_PROMEDIO_SUPERFICIE}{formato_numero(round(promedio, 2))}{FORMAT_KM2}")

def estadistica_cantidad_por_continente(paises: List[Dict[str, int | str]]) -> None:
    """estadistica_cantidad_por_continente: Muestra cantidad de países por continente."""
    validar_no_vacio(paises, MSG_NO_PAISES_CARGADOS)
    
    continentes = {}
    for pais in paises:
        continente = pais["continente"].strip()
        continentes[continente] = continentes.get(continente, 0) + 1
    
    continentes_ordenados = sorted(continentes.items())
    
    print(LABEL_CANTIDAD_POR_CONTINENTE)
    for continente, count in continentes_ordenados:
        print(f"  {continente}: {count}")
    
    total = sum(continentes.values())
    print(f"{LABEL_TOTAL}{total}{LABEL_PAISES}")
