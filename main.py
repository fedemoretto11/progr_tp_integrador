import csv


#Funciones auxiliares
def pedir_entero(mensaje):
  try:
    numero = int(input(mensaje))
    return numero
  except ValueError:
    raise ValueError("Debe ingresar un numero entero")
  
def pedir_texto(mensaje):
  try:
    texto = input(mensaje).strip()
    if texto == "":
      raise ValueError("El campo no puede estar vacio")
    return texto
  except ValueError:
    raise

def buscar_pais_no_existe(nombre, paises):
  for pais in paises:
      if pais["nombre"].lower() == nombre.lower():
        raise ValueError("El pais ya existe")




#Funciones
def leer_paises_csv(ruta):
  paises = []
  
  try:
    with open(ruta, "r", encoding="utf-8") as archivo:
      lector = csv.DictReader(archivo)
      
      for fila in lector:
        nombre = fila["nombre"].strip()
        poblacion = int(fila["poblacion"])
        superficie = int(fila["superficie"])
        continente =fila["continente"].strip()
    
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

def mostrar_paises(paises):
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
    print("Pais agregado correctamente")    
  except ValueError:
    raise




#Funciones de impresion en pantalla
def mostrar_menu_principal():
  print("\n----- Gestor de Paises -----")
  print("Ingrese una opcion: ")
  print("1 - Agregar Pais")
  print("2 - Actualizar poblacion y superficie")
  print("3 - Buscar pais por nombre")
  print("4 - Filtrar paises")
  print("5 - Ordenar Paises")
  print("6 - Mostrar estadisticas")
  print("7 - Mostrar todos los paises")
  print("8 - Salir")

def mostrar_submenu_filtro():
  print("\n-- Filtros --")
  print("Ingrese una opcion: ")
  print("1 - Por Continente")
  print("2 - Por Rango de poblacion")
  print("3 - Por Rango de superficie")
  print("4 - Volver al menu principal")

def mostrar_submenu_orden():
  print("\n-- Ordenar --")
  print("Ingrese una opcion: ")
  print("1 - Por Nombre")
  print("2 - Por Poblacion")
  print("3 - Por Superficie")
  print("4 - Volver al menu principal")

def mostrar_submenu_estadisticas():
  print("\n-- Estadisticas --")
  print("Ingrese una opcion: ")
  print("1 - Paises con mayor y menor poblacion")
  print("2 - Promedio poblacion")
  print("3 - Promedio superficie")
  print("4 - Cantidad de paises por continente")
  print("5 - Volver al menu principal")

def mostrar_submenu_tipo_orden():
  print("\n-- Tipo de orden --")
  print("Ingrese una opcion:")
  print("1 - Ascendente")
  print("2 - Descendente")





#Funcion main  
def main():
  ruta = "datos/paises.csv"
  opcion = 0
  
  try:
    paises = leer_paises_csv(ruta)
    print("Paises cargados correctamente")
  except Exception as error:
    print(f"Error al cargar el CSV: {error}")
    paises = []
  
  while opcion != 8:    
    mostrar_menu_principal()    
    try:
      opcion = pedir_entero("\nIngrese una opcion: ")

      if opcion == 1:
        agregar_pais(paises)
      elif opcion == 2:
        print("Actualizar pais")
      elif opcion == 3:
        paises_encontrados = buscar_pais_por_nombre(paises)
        mostrar_paises(paises_encontrados)
      elif opcion == 4:
        print("Filtrar paises")
      elif opcion == 5:
        print("Ordenar paises")
      elif opcion == 6:
        print("Mostrar estadisticas")
      elif opcion == 7:
        mostrar_paises(paises)
      elif opcion == 8:
        print("Saliendo del sistema...")
      else:
        raise ValueError("Seleccione una opcion entre 1 y 8")
    except ValueError as error:
      print(f"Error: {error}")
      
      
main()