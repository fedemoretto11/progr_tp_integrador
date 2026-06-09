from utils.prompts import (
    LABEL_SECTION_MAIN_MENU, LABEL_OPCION_AGREGAR_PAIS, LABEL_OPCION_ACTUALIZAR_PAIS,
    LABEL_OPCION_BUSCAR_PAIS, LABEL_OPCION_FILTRAR, LABEL_OPCION_ORDENAR,
    LABEL_OPCION_ESTADISTICAS, LABEL_OPCION_MOSTRAR_TODOS, LABEL_OPCION_SALIR
)

def get_opciones_menu_principal():
    """get_opciones_menu_principal: Retorna lista de opciones del menú principal."""
    return [
        LABEL_OPCION_AGREGAR_PAIS,
        LABEL_OPCION_ACTUALIZAR_PAIS,
        LABEL_OPCION_BUSCAR_PAIS,
        LABEL_OPCION_FILTRAR,
        LABEL_OPCION_ORDENAR,
        LABEL_OPCION_ESTADISTICAS,
        LABEL_OPCION_MOSTRAR_TODOS,
        LABEL_OPCION_SALIR,
    ]

def get_titulo_menu_principal():
    """get_titulo_menu_principal: Retorna el título del menú principal."""
    return f"\n{LABEL_SECTION_MAIN_MENU}"

def get_opciones_submenu_filtro():
    """get_opciones_submenu_filtro: Retorna opciones del submenú de filtros."""
    return ["Por Continente", "Por Rango de poblacion", "Por Rango de superficie", "Volver al menu principal"]

def get_opciones_submenu_orden():
    """get_opciones_submenu_orden: Retorna opciones del submenú de ordenamientos."""
    return ["Por Nombre", "Por Poblacion", "Por Superficie", "Volver al menu principal"]

def get_opciones_submenu_estadisticas():
    """get_opciones_submenu_estadisticas: Retorna opciones del submenú de estadísticas."""
    return [
        "Paises con mayor y menor poblacion",
        "Promedio poblacion",
        "Promedio superficie",
        "Cantidad de paises por continente",
        "Volver al menu principal"
    ]

def get_opciones_submenu_tipo_orden():
    """get_opciones_submenu_tipo_orden: Retorna opciones para tipo de orden (asc/desc)."""
    return ["Ascendente", "Descendente"]
