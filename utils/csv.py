import csv
import os
from typing import List, Dict
from utils.messages import (
    MSG_ERROR_ESCRIBIR_CSV,
    MSG_ERROR_PERMISOS_CSV,
    MSG_ERROR_CSV_CAMPOS_VACIOS,
    MSG_ERROR_CSV_NO_ENCONTRADO,
    MSG_ERROR_CSV_COLUMNAS,
    MSG_ERROR_CSV_DATOS_INVALIDOS,
)

def obtener_ruta_csv() -> str:
    """Retorna la ruta relativa al archivo CSV."""
    return os.path.join("datos", "paises.csv")

def guardar_paises_csv(paises: List[Dict[str, int | str]]) -> None:
    """Guarda la lista de países en el archivo CSV.

    Implememnta manejo de errores
    """
    ruta = obtener_ruta_csv()
    fieldnames = ["nombre", "poblacion", "superficie", "continente"]
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(paises)
    except FileNotFoundError:
        raise FileNotFoundError(MSG_ERROR_ESCRIBIR_CSV.format(ruta=ruta))
    except PermissionError:
        raise PermissionError(MSG_ERROR_PERMISOS_CSV.format(ruta=ruta))

def leer_paises_csv() -> List[Dict[str, int | str]]:
    """Lee la lista de países desde el archivo CSV.
    
    Retorna: Lista de diccionarios con datos de países

    Implementa manejo de errores
    """
    ruta = obtener_ruta_csv()
    paises: List[Dict[str, int | str]] = []
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                nombre = fila["nombre"].strip()
                poblacion = int(fila["poblacion"])
                superficie = int(fila["superficie"])
                continente = fila["continente"].strip()
        
                if nombre == "" or continente == "":
                    raise ValueError(MSG_ERROR_CSV_CAMPOS_VACIOS)
                
                pais = {
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                }
                
                paises.append(pais)
             
            return paises
    except FileNotFoundError:
        raise FileNotFoundError(MSG_ERROR_CSV_NO_ENCONTRADO)
    except KeyError:
        raise ValueError(MSG_ERROR_CSV_COLUMNAS)
    except ValueError:
        raise ValueError(MSG_ERROR_CSV_DATOS_INVALIDOS)
