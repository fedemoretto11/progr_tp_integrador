from utils.input import pedir_entero, pedir_texto
from utils.csv import guardar_paises_csv

def buscar_pais_no_existe(nombre, paises):
    """Valida que un país no exista ya en la lista."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            raise ValueError("El pais ya existe")

def mostrar_paises(paises):
    """Muestra la lista de países con formato legible."""
    if len(paises) == 0:
        raise ValueError("No hay paises cargados")
    print("\n--- Lista de Paises ---")
    for pais in paises:
        print(f"\nPais: {pais['nombre']}")
        print(f"Poblacion: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km2")
        print(f"Continente: {pais['continente']}")
        print("-----------------------------")

def buscar_pais_por_nombre(paises):
    """Busca países por nombre (coincidencia parcial, case-insensitive)."""
    try: 
        paises_a_buscar = pedir_texto("Ingrese el pais a buscar: ").lower()
        paises_encontrados = []
        
        for pais in paises:
            if paises_a_buscar in pais["nombre"].lower():
                paises_encontrados.append(pais)
        
        if len(paises_encontrados) == 0:
            raise ValueError("No se encontraron paises con ese nombre")
        
        return paises_encontrados
    except ValueError:
        raise

def agregar_pais(paises):
    """Agrega un nuevo país a la lista y guarda en CSV.
    
    Valida:
    - País no existe (case-insensitive)
    - Población > 0
    - Superficie > 0
    - Campos no vacíos
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
        
        # FASE 0: Guardar cambios en CSV con manejo de errores
        try:
            guardar_paises_csv(paises)
            print("Pais agregado correctamente y guardado en CSV")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Advertencia: No se pudo guardar en CSV: {error}")
            print("El pais fue agregado en memoria pero no se guardaró permanentemente")
            
    except ValueError:
        raise
