import csv
import os

def obtener_ruta_csv():
    """Retorna la ruta relativa al archivo CSV."""
    return os.path.join("datos", "paises.csv")

def guardar_paises_csv(paises):
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
        raise FileNotFoundError(f"No se puede escribir en {ruta}: archivo no encontrado")
    except PermissionError:
        raise PermissionError(f"No tiene permisos de escritura en {ruta}")

def leer_paises_csv():
    """Lee la lista de países desde el archivo CSV.
    
    Retorna: Lista de diccionarios con datos de países

    Implementa manejo de errores
    """
    ruta = obtener_ruta_csv()
    paises = []
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                nombre = fila["nombre"].strip()
                poblacion = int(fila["poblacion"])
                superficie = int(fila["superficie"])
                continente = fila["continente"].strip()
        
                if nombre == "" or continente == "":
                    raise ValueError("El CSV contiene campos vacios")
                
                pais = {
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                }
                
                paises.append(pais)
            
            return paises
    except FileNotFoundError:
        raise FileNotFoundError("No se encontro el archivo CSV")
    except KeyError:
        raise ValueError("El CSV no tiene las columnas esperadas")
    except ValueError:
        raise ValueError("El CSV contiene datos invalidos")
