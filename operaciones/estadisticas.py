from utils.formatting import formato_numero

def estadistica_max_min_poblacion(paises):
    """Muestra país con mayor y menor población."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    max_pais = max(paises, key=lambda p: p["poblacion"])
    min_pais = min(paises, key=lambda p: p["poblacion"])
    
    print("\n--- Mayor Población ---")
    print(f"País: {max_pais['nombre']}")
    print(f"Población: {formato_numero(max_pais['poblacion'])}")
    print(f"Superficie: {formato_numero(max_pais['superficie'])} km2")
    print(f"Continente: {max_pais['continente']}")
    
    print("\n--- Menor Población ---")
    print(f"País: {min_pais['nombre']}")
    print(f"Población: {formato_numero(min_pais['poblacion'])}")
    print(f"Superficie: {formato_numero(min_pais['superficie'])} km2")
    print(f"Continente: {min_pais['continente']}")
    
    diferencia = max_pais["poblacion"] - min_pais["poblacion"]
    print(f"\nDiferencia: {formato_numero(diferencia)}")

def estadistica_promedio_poblacion(paises):
    """Calcula y muestra promedio de población."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    total = sum(p["poblacion"] for p in paises)
    promedio = total / len(paises)
    
    print(f"\nPromedio Población: {formato_numero(round(promedio, 2))}")

def estadistica_promedio_superficie(paises):
    """Calcula y muestra promedio de superficie."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    total = sum(p["superficie"] for p in paises)
    promedio = total / len(paises)
    
    print(f"\nPromedio Superficie: {formato_numero(round(promedio, 2))} km2")

def estadistica_cantidad_por_continente(paises):
    """Muestra cantidad de países por continente (ordenado alfabéticamente)."""
    if not paises:
        raise ValueError("No hay paises cargados")
    
    # Agrupar por continente
    continentes = {}
    for pais in paises:
        continente = pais["continente"].strip()
        continentes[continente] = continentes.get(continente, 0) + 1
    
    # Ordenar alfabéticamente para visualización
    continentes_ordenados = sorted(continentes.items())
    
    print("\nCantidad de Países por Continente:")
    for continente, count in continentes_ordenados:
        print(f"  {continente}: {count}")
    
    total = sum(continentes.values())
    print(f"\nTotal: {total} países")
