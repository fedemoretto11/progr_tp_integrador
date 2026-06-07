from utils.input import pedir_entero, pedir_texto
from utils.csv import guardar_paises_csv
from utils.formatting import formato_numero
from utils.prompts import (
    PROMPT_BUSCAR_PAIS, PROMPT_AGREGAR_NOMBRE, PROMPT_AGREGAR_POBLACION,
    PROMPT_AGREGAR_SUPERFICIE, PROMPT_AGREGAR_CONTINENTE,
    PROMPT_ACTUALIZAR_SELECCIONAR, PROMPT_ACTUALIZAR_POBLACION,
    PROMPT_ACTUALIZAR_SUPERFICIE, PROMPT_ACTUALIZAR_VALORES,
    PROMPT_CONFIRMAR_ACTUALIZACION, MSG_SECTION_AGREGAR_PAIS,
    MSG_SECTION_ACTUALIZAR_PAIS, MSG_PAIS_AGREGADO, MSG_PAIS_ACTUALIZADO,
    MSG_OPERACION_CANCELADA, MSG_ADVERTENCIA_CSV, MSG_ADVERTENCIA_MEMORIA,
    MSG_ADVERTENCIA_ACTUALIZAR, LABEL_LISTA_PAISES, LABEL_PAIS,
    LABEL_POBLACION, LABEL_SUPERFICIE, LABEL_CONTINENTE,
    LABEL_PAISES_ENCONTRADOS, LABEL_PAIS_SELECCIONADO,
    LABEL_POBLACION_ACTUAL, LABEL_SUPERFICIE_ACTUAL,
    LABEL_CONFIRMAR_ACTUALIZACION, LABEL_POBLACION_CAMBIO,
    LABEL_POBLACION_ARROW, LABEL_SUPERFICIE_CAMBIO,
    OPCION_SI, FORMAT_KM2
)
from utils.messages import (
    MSG_NO_PAISES_CARGADOS,
    MSG_ERROR_PAIS_EXISTE,
    MSG_ERROR_PAIS_NO_ENCONTRADO,
    MSG_ERROR_POBLACION_POSITIVA,
    MSG_ERROR_SUPERFICIE_POSITIVA,
    MSG_OPCION_INVALIDA,
    MSG_SELECCION_INVALIDA,
)
from typing import List, Dict

def buscar_pais_no_existe(nombre: str, paises: List[Dict[str, int | str]]) -> None:
    """Valida que un país no exista ya en la lista."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            raise ValueError(MSG_ERROR_PAIS_EXISTE)

def mostrar_paises(paises: List[Dict[str, int | str]]) -> None:
    """Muestra la lista de países."""
    if len(paises) == 0:
        raise ValueError(MSG_NO_PAISES_CARGADOS)
    print(f"\n{LABEL_LISTA_PAISES}")
    for pais in paises:
        print(f"\n{LABEL_PAIS} {pais['nombre']}")
        print(f"{LABEL_POBLACION} {formato_numero(pais['poblacion'])}")
        print(f"{LABEL_SUPERFICIE} {formato_numero(pais['superficie'])}{FORMAT_KM2}")
        print(f"{LABEL_CONTINENTE} {pais['continente']}")
        print("-----------------------------")

def buscar_pais_por_nombre(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """Busca países por nombre (coincidencia parcial o exacta)."""
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

def agregar_pais(paises: List[Dict[str, int | str]]) -> None:
    """Agrega un nuevo país a la lista y guarda en CSV.
    
    Valida:
    - País no existe (case-insensitive)
    - Población > 0
    - Superficie > 0
    - No hay cmapos vacios
    """
    try:
        print(MSG_SECTION_AGREGAR_PAIS)
        nombre = pedir_texto(PROMPT_AGREGAR_NOMBRE)
        buscar_pais_no_existe(nombre, paises)
        
        poblacion = pedir_entero(PROMPT_AGREGAR_POBLACION)
        superficie = pedir_entero(PROMPT_AGREGAR_SUPERFICIE)
        continente = pedir_texto(PROMPT_AGREGAR_CONTINENTE)
        
        if poblacion <= 0:
            raise ValueError(MSG_ERROR_POBLACION_POSITIVA)

        if superficie <= 0:
            raise ValueError(MSG_ERROR_SUPERFICIE_POSITIVA)
        
        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        
        paises.append(nuevo_pais)

        try:
            guardar_paises_csv(paises)
            print(MSG_PAIS_AGREGADO)
        except (FileNotFoundError, PermissionError) as error:
            print(f"{MSG_ADVERTENCIA_CSV}{error}")
            print(MSG_ADVERTENCIA_MEMORIA)
            
    except ValueError:
        raise

def actualizar_pais(paises: List[Dict[str, int | str]]) -> None:
    """Actualiza población y superficie de un país existente.

    Flujo: Buscar país por nombre -> Mostrar valores actuales -> pedir y validar nuevos valores
     -> confirmar guardado -> guardar en csv
    """
    try:
        print(MSG_SECTION_ACTUALIZAR_PAIS)
        
        # Buscar país
        paises_encontrados = buscar_pais_por_nombre(paises)
        
        # Si hay múltiples matches, mostrar y pedir selección
        if len(paises_encontrados) > 1:
            print(LABEL_PAISES_ENCONTRADOS)
            for i, pais in enumerate(paises_encontrados, 1):
                print(f"{i}. {pais['nombre']} (Población: {formato_numero(pais['poblacion'])}, Superficie: {formato_numero(pais['superficie'])}{FORMAT_KM2})")
            
            try:
                opcion = pedir_entero(PROMPT_ACTUALIZAR_SELECCIONAR)
                if opcion < 1 or opcion > len(paises_encontrados):
                    raise ValueError(MSG_OPCION_INVALIDA)
                pais = paises_encontrados[opcion - 1]
            except (ValueError, IndexError):
                raise ValueError(MSG_SELECCION_INVALIDA)
        else:
            pais = paises_encontrados[0]
        
        # Mostrar valores actuales
        print(f"{LABEL_PAIS_SELECCIONADO}{pais['nombre']}")
        print(f"{LABEL_POBLACION_ACTUAL}{formato_numero(pais['poblacion'])}")
        print(f"{LABEL_SUPERFICIE_ACTUAL}{formato_numero(pais['superficie'])}{FORMAT_KM2}")
        
        # Pedir nuevos valores
        print(f"\n{PROMPT_ACTUALIZAR_VALORES}")
        
        poblacion_nueva = pedir_entero(PROMPT_ACTUALIZAR_POBLACION)
        if poblacion_nueva <= 0:
            raise ValueError(MSG_ERROR_POBLACION_POSITIVA)
        
        superficie_nueva = pedir_entero(PROMPT_ACTUALIZAR_SUPERFICIE)
        if superficie_nueva <= 0:
            raise ValueError(MSG_ERROR_SUPERFICIE_POSITIVA)
        
        # Pedir confirmación
        print(LABEL_CONFIRMAR_ACTUALIZACION)
        print(f"  {pais['nombre']}")
        print(f"  {LABEL_POBLACION_CAMBIO}{formato_numero(pais['poblacion'])}{LABEL_POBLACION_ARROW}{formato_numero(poblacion_nueva)}")
        print(f"  {LABEL_SUPERFICIE_CAMBIO}{formato_numero(pais['superficie'])}{LABEL_POBLACION_ARROW}{formato_numero(superficie_nueva)}{FORMAT_KM2}")
        
        confirmacion = input(PROMPT_CONFIRMAR_ACTUALIZACION).strip().lower()
        
        if confirmacion != OPCION_SI:
            print(MSG_OPERACION_CANCELADA)
            return
        
        # Actualizar valores
        pais["poblacion"] = poblacion_nueva
        pais["superficie"] = superficie_nueva
        
        # Guardar en CSV con manejo de errores
        try:
            guardar_paises_csv(paises)
            print(MSG_PAIS_ACTUALIZADO)
        except (FileNotFoundError, PermissionError) as error:
            print(f"{MSG_ADVERTENCIA_CSV}{error}")
            print(MSG_ADVERTENCIA_ACTUALIZAR)
            
    except ValueError:
        raise



def mostrar_paises(paises: List[Dict[str, int | str]]) -> None:
    """Muestra la lista de países."""
    if len(paises) == 0:
        raise ValueError("No hay paises cargados")
    print("\n--- Lista de Paises ---")
    for pais in paises:
        print(f"\nPais: {pais['nombre']}")
        print(f"Poblacion: {formato_numero(pais['poblacion'])}")
        print(f"Superficie: {formato_numero(pais['superficie'])} km2")
        print(f"Continente: {pais['continente']}")
        print("-----------------------------")

def buscar_pais_por_nombre(paises: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """Busca países por nombre (coincidencia parcial o exacta)."""
    try: 
        paises_a_buscar = pedir_texto("Ingrese el pais a buscar: ").lower()
        paises_encontrados: List[Dict[str, int | str]] = []
        
        for pais in paises:
            if paises_a_buscar in pais["nombre"].lower():
                paises_encontrados.append(pais)
        
        if len(paises_encontrados) == 0:
            raise ValueError("No se encontraron paises con ese nombre")
        
        return paises_encontrados
    except ValueError:
        raise

def agregar_pais(paises: List[Dict[str, int | str]]) -> None:
    """Agrega un nuevo país a la lista y guarda en CSV.
    
    Valida:
    - País no existe (case-insensitive)
    - Población > 0
    - Superficie > 0
    - No hay cmapos vacios
    """
    try:
        print("\nAgregar nuevo pais")
        nombre = pedir_texto("Ingrese el nombre del pais a agregar: ")
        buscar_pais_no_existe(nombre, paises)
        
        poblacion = pedir_entero("Ingrese la poblacion: ")
        superficie = pedir_entero("Ingrese la superficie: ")
        continente = pedir_texto("Ingrese el continente: ")
        
        if poblacion <= 0:
            raise ValueError("La poblacion debe ser mayor a 0")

        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a 0")
        
        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        
        paises.append(nuevo_pais)

        try:
            guardar_paises_csv(paises)
            print("Pais agregado correctamente y guardado en CSV")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Advertencia: No se pudo guardar en CSV: {error}")
            print("El pais fue agregado en memoria pero no se guardaró permanentemente")
            
    except ValueError:
        raise

def actualizar_pais(paises: List[Dict[str, int | str]]) -> None:
    """Actualiza población y superficie de un país existente.

    Flujo: Buscar país por nombre -> Mostrar valores actuales -> pedir y validar nuevos valores
     -> confirmar guardado -> guardar en csv
    """
    try:
        print("\nActualizar pais")
        
        # Buscar país
        paises_encontrados = buscar_pais_por_nombre(paises)
        
        # Si hay múltiples matches, mostrar y pedir selección
        if len(paises_encontrados) > 1:
            print("\nEncontrados varios paises:")
            for i, pais in enumerate(paises_encontrados, 1):
                print(f"{i}. {pais['nombre']} (Población: {formato_numero(pais['poblacion'])}, Superficie: {formato_numero(pais['superficie'])} km2)")
            
            try:
                opcion = pedir_entero("Seleccione el numero del pais a actualizar: ")
                if opcion < 1 or opcion > len(paises_encontrados):
                    raise ValueError("Opcion invalida")
                pais = paises_encontrados[opcion - 1]
            except (ValueError, IndexError):
                raise ValueError("Seleccion invalida")
        else:
            pais = paises_encontrados[0]
        
        # Mostrar valores actuales
        print(f"\nPais seleccionado: {pais['nombre']}")
        print(f"Poblacion actual: {formato_numero(pais['poblacion'])}")
        print(f"Superficie actual: {formato_numero(pais['superficie'])} km2")
        
        # Pedir nuevos valores
        print("\nIngrese los nuevos valores (o deje en blanco para mantener los actuales):")
        
        poblacion_nueva = pedir_entero("Ingrese la nueva poblacion: ")
        if poblacion_nueva <= 0:
            raise ValueError("La poblacion debe ser mayor a 0")
        
        superficie_nueva = pedir_entero("Ingrese la nueva superficie: ")
        if superficie_nueva <= 0:
            raise ValueError("La superficie debe ser mayor a 0")
        
        # Pedir confirmación
        print(f"\n¿Confirmar actualización?")
        print(f"  {pais['nombre']}")
        print(f"  Población: {formato_numero(pais['poblacion'])} → {formato_numero(poblacion_nueva)}")
        print(f"  Superficie: {formato_numero(pais['superficie'])} → {formato_numero(superficie_nueva)} km2")
        
        confirmacion = input("¿Actualizar? (s/n): ").strip().lower()
        
        if confirmacion != "s":
            print("Operacion cancelada")
            return
        
        # Actualizar valores
        pais["poblacion"] = poblacion_nueva
        pais["superficie"] = superficie_nueva
        
        # Guardar en CSV con manejo de errores
        try:
            guardar_paises_csv(paises)
            print("Pais actualizado correctamente y guardado en CSV")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Advertencia: No se pudo guardar en CSV: {error}")
            print("El pais fue actualizado en memoria pero no se guardaró permanentemente")
            
    except ValueError:
        raise

