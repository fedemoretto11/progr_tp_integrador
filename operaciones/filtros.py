from utils.input import pedir_entero

def filtrar_por_continente(paises):
    """Filtra países por continente seleccionado."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    # Get unique continents maintaining order
    continentes = []
    for pais in paises:
        continente = pais["continente"].strip()
        if continente not in continentes:
            continentes.append(continente)
    
    print("\nContinentes disponibles:")
    for i, continente in enumerate(continentes, 1):
        count = sum(1 for p in paises if p["continente"].strip() == continente)
        print(f"{i}. {continente} ({count} paises)")
    
    try:
        opcion = pedir_entero("Seleccione continente: ")
        if opcion < 1 or opcion > len(continentes):
            raise ValueError("Opcion invalida")
        
        continente_seleccionado = continentes[opcion - 1]
        paises_filtrados = [p for p in paises if p["continente"].strip() == continente_seleccionado]
        
        if not paises_filtrados:
            raise ValueError(f"No hay paises en {continente_seleccionado}")
        
        return paises_filtrados
    except (ValueError, IndexError) as e:
        raise ValueError(f"Seleccion invalida: {str(e)}")

def filtrar_por_rango_poblacion(paises):
    """Filtra países por rango de población (inclusivo)."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    poblacion_min = pedir_entero("Ingrese poblacion minima: ")
    poblacion_max = pedir_entero("Ingrese poblacion maxima: ")
    
    if poblacion_min <= 0 or poblacion_max <= 0:
        raise ValueError("Poblacion debe ser mayor a 0")
    
    if poblacion_min > poblacion_max:
        raise ValueError("Poblacion minima no puede ser mayor a maxima")
    
    paises_filtrados = [p for p in paises if poblacion_min <= p["poblacion"] <= poblacion_max]
    
    if not paises_filtrados:
        raise ValueError(f"No hay paises en el rango {poblacion_min} - {poblacion_max}")
    
    return paises_filtrados

def filtrar_por_rango_superficie(paises):
    """Filtra países por rango de superficie (inclusivo)."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    superficie_min = pedir_entero("Ingrese superficie minima (km2): ")
    superficie_max = pedir_entero("Ingrese superficie maxima (km2): ")
    
    if superficie_min <= 0 or superficie_max <= 0:
        raise ValueError("Superficie debe ser mayor a 0")
    
    if superficie_min > superficie_max:
        raise ValueError("Superficie minima no puede ser mayor a maxima")
    
    paises_filtrados = [p for p in paises if superficie_min <= p["superficie"] <= superficie_max]
    
    if not paises_filtrados:
        raise ValueError(f"No hay paises en el rango {superficie_min} - {superficie_max} km2")
    
    return paises_filtrados
