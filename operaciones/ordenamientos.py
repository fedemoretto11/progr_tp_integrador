from utils.input import pedir_entero

def ordenar_por_nombre(paises, descendente=False):
    """Sorts countries by name (case-insensitive)."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)

def ordenar_por_poblacion(paises, descendente=False):
    """Sorts countries by population."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

def ordenar_por_superficie(paises, descendente=False):
    """Sorts countries by surface area."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

def pedir_direccion_orden():
    """Prompts user for sort direction."""
    try:
        opcion = pedir_entero("Seleccione direccion (1=Ascendente, 2=Descendente): ")
        if opcion == 1:
            return False
        elif opcion == 2:
            return True
        else:
            raise ValueError("Opcion invalida (ingrese 1 o 2)")
    except ValueError:
        raise
