"""Funciones de validación centralizadas - mejora legibilidad y reutilización."""

from typing import List, Dict, Any, Callable
from utils.messages import *
from utils.formatting import formato_numero
from utils.input import pedir_opcion_menu


def validar_no_vacio(items: List[Any], mensaje_error: str) -> None:
    """validar_no_vacio: Valida que la lista tenga elementos."""
    if not items:
        raise ValueError(mensaje_error)


def validar_condicion(condicion: bool, mensaje_error: str) -> None:
    """validar_condicion: Valida una condición booleana."""
    if not condicion:
        raise ValueError(mensaje_error)


def validar_numero_positivo(numero: int, mensaje_error: str) -> None:
    """validar_numero_positivo: Valida que un número sea mayor a 0."""
    validar_condicion(numero > 0, mensaje_error)


def validar_rango(minimo: int, maximo: int, mensaje_error: str) -> None:
    """validar_rango: Valida que minimo <= maximo y ambos > 0."""
    validar_numero_positivo(minimo, mensaje_error)
    validar_numero_positivo(maximo, mensaje_error)
    validar_condicion(minimo <= maximo, mensaje_error)


def validar_pais_no_existe(nombre: str, paises: List[Dict[str, int | str]]) -> None:
    """validar_pais_no_existe: Valida que un país NO exista en la lista (case-insensitive)."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            raise ValueError(MSG_ERROR_PAIS_EXISTE)


def validar_poblacion_positiva(poblacion: int) -> None:
    """validar_poblacion_positiva: Valida que la población sea mayor a 0."""
    validar_numero_positivo(poblacion, MSG_ERROR_POBLACION_POSITIVA)


def validar_superficie_positiva(superficie: int) -> None:
    """validar_superficie_positiva: Valida que la superficie sea mayor a 0."""
    validar_numero_positivo(superficie, MSG_ERROR_SUPERFICIE_POSITIVA)


def validar_rango_poblacion(min_poblacion: int, max_poblacion: int) -> None:
    """validar_rango_poblacion: Valida que min_poblacion <= max_poblacion y ambas > 0."""
    validar_rango(min_poblacion, max_poblacion, MSG_ERROR_RANGO_POBLACION)


def validar_rango_superficie(min_superficie: int, max_superficie: int) -> None:
    """validar_rango_superficie: Valida que min_superficie <= max_superficie y ambas > 0."""
    validar_rango(min_superficie, max_superficie, MSG_ERROR_RANGO_SUPERFICIE)


# ==================== FUNCIONES GENÉRICAS DE VALIDACIÓN ====================


def validar_no_vacio_string(texto: str, mensaje_error: str = "El valor no puede estar vacío") -> str:
    """validar_no_vacio_string: Valida que un string no esté vacío."""
    if not texto.strip():
        raise ValueError(mensaje_error)
    return texto.strip()


def validar_entero_mayor_a(valor_str: str, minimo: int = 0, mensaje_error: str = None) -> int:
    """validar_entero_mayor_a: Valida y convierte string a entero mayor que minimo."""
    try:
        valor = int(valor_str)
    except ValueError:
        raise ValueError(mensaje_error or "Debe ser un número entero")
    
    if valor <= minimo:
        raise ValueError(mensaje_error or f"Debe ser mayor a {minimo}")
    
    return valor


def pedir_con_reintentos(
    prompt: str,
    validador: Callable[[str], Any]
) -> Any:
    """pedir_con_reintentos: Pide entrada con reintentos hasta obtener valor válido o "salir"."""
    while True:
        try:
            entrada = input(prompt).strip()
            
            if entrada.lower() == "salir":
                raise ValueError("cancelado")
            
            valor_validado = validador(entrada)
            return valor_validado
        except ValueError as error:
            if str(error) == "cancelado":
                raise
            print(f"Error: {error}")
            continue


def crear_validador_nombre_pais(paises: List[Dict[str, int | str]]) -> Callable[[str], str]:
    """crear_validador_nombre_pais: Factory que crea validador de nombre único."""
    def validador(nombre: str) -> str:
        validar_no_vacio_string(nombre, "El nombre del país no puede estar vacío")
        
        for pais in paises:
            if pais["nombre"].lower() == nombre.lower():
                raise ValueError(MSG_ERROR_PAIS_EXISTE)
        
        return nombre.strip()
    
    return validador


def crear_validador_entero(minimo: int = 0, mensaje_error: str = None) -> Callable[[str], int]:
    """crear_validador_entero: Factory que crea validador de entero con mínimo."""
    def validador(valor_str: str) -> int:
        return validar_entero_mayor_a(valor_str, minimo, mensaje_error)
    
    return validador


# ==================== FUNCIONES AUXILIARES PARA MENÚ ====================


def seleccionar_pais_de_lista(paises_lista: List[Dict[str, int | str]]) -> Dict[str, int | str]:
    """seleccionar_pais_de_lista: Permite al usuario seleccionar un país de una lista."""
    print("\nEncontrados varios paises:")
    for i, pais in enumerate(paises_lista, 1):
        print(f"{i}. {pais['nombre']} (Población: {formato_numero(pais['poblacion'])}, Superficie: {formato_numero(pais['superficie'])} km2)")
    
    while True:
        try:
            opcion_str = input("Seleccione el numero del pais (o 'salir' para cancelar): ").strip()
            
            if opcion_str.lower() == "salir":
                raise ValueError("cancelado")
            
            opcion = int(opcion_str)
            if opcion < 1 or opcion > len(paises_lista):
                print("Error: Opción inválida")
                continue
            
            return paises_lista[opcion - 1]
        except ValueError as e:
            if str(e) == "cancelado":
                raise
            print("Error: Debe ingresar un número válido")
            continue


def mostrar_pais_valores_actuales(pais: Dict[str, int | str]) -> None:
    """mostrar_pais_valores_actuales: Muestra un país con sus valores actuales."""
    print(f"\nPais seleccionado: {pais['nombre']}")
    print(f"Poblacion actual: {formato_numero(pais['poblacion'])}")
    print(f"Superficie actual: {formato_numero(pais['superficie'])} km2")


def pedir_nuevos_valores(
    poblacion_actual: int,
    superficie_actual: int
) -> tuple[int, int]:
    """pedir_nuevos_valores: Solicita nuevos valores de población y superficie con validación."""
    print("\nIngrese los nuevos valores:")
    
    poblacion_nueva = pedir_con_reintentos(
        "Ingrese la nueva poblacion (o 'salir' para cancelar): ",
        crear_validador_entero(minimo=0, mensaje_error=MSG_ERROR_POBLACION_POSITIVA)
    )
    
    superficie_nueva = pedir_con_reintentos(
        "Ingrese la nueva superficie (o 'salir' para cancelar): ",
        crear_validador_entero(minimo=0, mensaje_error=MSG_ERROR_SUPERFICIE_POSITIVA)
    )
    
    return poblacion_nueva, superficie_nueva


def pedir_confirmacion_actualizacion(
    pais: Dict[str, int | str],
    poblacion_nueva: int,
    superficie_nueva: int
) -> bool:
    """pedir_confirmacion_actualizacion: Muestra cambios y pide confirmación del usuario."""
    print(f"\n¿Confirmar actualización?")
    print(f"  {pais['nombre']}")
    print(f"  Población: {formato_numero(pais['poblacion'])} → {formato_numero(poblacion_nueva)}")
    print(f"  Superficie: {formato_numero(pais['superficie'])} → {formato_numero(superficie_nueva)} km2")
    
    confirmacion = input("¿Actualizar? (s/n): ").strip().lower()
    return confirmacion == "s"


def actualizar_pais_en_lista(
    pais: Dict[str, int | str],
    poblacion_nueva: int,
    superficie_nueva: int
) -> None:
    """actualizar_pais_en_lista: Actualiza población y superficie de un país en la lista."""
    pais["poblacion"] = poblacion_nueva
    pais["superficie"] = superficie_nueva


# ==================== FUNCIONES AUXILIARES PARA AGREGAR ====================


def pedir_datos_nuevo_pais(paises: List[Dict[str, int | str]]) -> tuple[str, int, int, str]:
    """pedir_datos_nuevo_pais: Solicita y valida datos para un nuevo país."""
    # Pedir nombre
    nombre = pedir_con_reintentos(
        "Ingrese el nombre del pais (o 'salir' para cancelar): ",
        crear_validador_nombre_pais(paises)
    )
    
    # Pedir población
    poblacion = pedir_con_reintentos(
        "Ingrese la poblacion (o 'salir' para cancelar): ",
        crear_validador_entero(minimo=0, mensaje_error=MSG_ERROR_POBLACION_POSITIVA)
    )
    
    # Pedir superficie
    superficie = pedir_con_reintentos(
        "Ingrese la superficie (o 'salir' para cancelar): ",
        crear_validador_entero(minimo=0, mensaje_error=MSG_ERROR_SUPERFICIE_POSITIVA)
    )
    
    # Pedir continente
    continente = pedir_con_reintentos(
        "Ingrese el continente (o 'salir' para cancelar): ",
        lambda c: validar_no_vacio_string(c, "El continente no puede estar vacío")
    )
    
    return nombre, poblacion, superficie, continente


def crear_nuevo_pais(
    nombre: str,
    poblacion: int,
    superficie: int,
    continente: str
) -> Dict[str, int | str]:
    """crear_nuevo_pais: Crea un diccionario con estructura de país."""
    return {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }


def insertar_pais_en_lista(
    pais: Dict[str, int | str],
    paises: List[Dict[str, int | str]]
) -> None:
    """insertar_pais_en_lista: Agrega un país a la lista."""
    paises.append(pais)


# ==================== FUNCIONES AUXILIARES PARA FILTRAR ====================


def pedir_opcion_filtro(opciones_disponibles: List[str]) -> int:
    """pedir_opcion_filtro: Pide al usuario que seleccione un tipo de filtro."""
    print("\n--- Opciones de Filtro ---")
    return pedir_opcion_menu(opciones_disponibles, "Selecciona un filtro: ")


# ==================== FUNCIONES AUXILIARES PARA ORDENAR ====================


def pedir_opcion_ordenamiento(opciones_disponibles: List[str]) -> int:
    """pedir_opcion_ordenamiento: Pide al usuario por qué campo ordenar."""
    print("\n--- Opciones de Ordenamiento ---")
    return pedir_opcion_menu(opciones_disponibles, "¿Cómo deseas ordenar?: ")


def pedir_tipo_orden(opciones_disponibles: List[str]) -> int:
    """pedir_tipo_orden: Pide al usuario si quiere orden ascendente o descendente."""
    print("\n--- Tipo de Orden ---")
    return pedir_opcion_menu(opciones_disponibles, "¿Orden ascendente o descendente?: ")


def determinar_descendente(tipo_orden: int) -> bool:
    """determinar_descendente: Convierte opción de tipo de orden a booleano descendente."""
    return tipo_orden == 2


# ==================== FUNCIONES AUXILIARES PARA ESTADÍSTICAS ====================


def pedir_opcion_estadistica(opciones_disponibles: List[str]) -> int:
    """pedir_opcion_estadistica: Pide al usuario qué estadística desea ver."""
    print("\n--- Opciones de Estadísticas ---")
    return pedir_opcion_menu(opciones_disponibles, "Selecciona una estadística: ")

