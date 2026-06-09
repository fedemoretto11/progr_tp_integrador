"""Funciones para manejar cada opción del menú principal."""

import sys
from operaciones.gestion import buscar_pais_por_nombre
from operaciones.filtros import filtrar_por_continente, filtrar_por_rango_poblacion, filtrar_por_rango_superficie
from operaciones.ordenamientos import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
from operaciones.estadisticas import estadistica_max_min_poblacion, estadistica_promedio_poblacion, estadistica_promedio_superficie, estadistica_cantidad_por_continente
from utils.csv import guardar_paises_csv
from utils.formatting import mostrar_lista_paises
from utils.menus import get_opciones_submenu_filtro, get_opciones_submenu_orden, get_opciones_submenu_estadisticas, get_opciones_submenu_tipo_orden
from utils.validaciones import *
from utils.error_messages import (
    MSG_EXITO_PAIS_AGREGADO, MSG_OPERACION_CANCELADA, 
    MSG_ERROR_GUARDAR_CSV, MSG_ADVERTENCIA_GUARDAR_CSV
)


def menu_agregar_pais(paises):
    """menu_agregar_pais: Orquesta el flujo de agregar un nuevo país."""
    print("\n" + "="*50)
    print("AGREGAR NUEVO PAIS")
    print("="*50)
    
    try:
        # 1. Pedir todos los datos con validación (SRP: input + validación)
        nombre, poblacion, superficie, continente = pedir_datos_nuevo_pais(paises)
        
        # 2. Crear diccionario del país (SRP: creación de objeto)
        nuevo_pais = crear_nuevo_pais(nombre, poblacion, superficie, continente)
        
        # 3. Insertar en lista (SRP: modificación de lista)
        insertar_pais_en_lista(nuevo_pais, paises)
        
        # 4. Persistir cambios (SRP: I/O)
        try:
            guardar_paises_csv(paises)
            print("\n" + "="*50)
            print(MSG_EXITO_PAIS_AGREGADO)
            print("="*50)
        except (FileNotFoundError, PermissionError) as error:
            print(f"\n{MSG_ERROR_GUARDAR_CSV}: {error}")
            print(MSG_ADVERTENCIA_GUARDAR_CSV)
            
    except ValueError as error:
        if str(error) == "cancelado":
            print("\n" + "="*50)
            print(MSG_OPERACION_CANCELADA)
            print("="*50)
        else:
            print(f"\n{error}")


def menu_actualizar_pais(paises):
    """menu_actualizar_pais: Orquesta el flujo de actualizar un país existente."""
    
    try:
        print("\nActualizar pais")
        
        # 1. Buscar país por nombre
        paises_encontrados = buscar_pais_por_nombre(paises)
        
        # 2. Si hay múltiples, dejar que usuario seleccione
        if len(paises_encontrados) > 1:
            pais = seleccionar_pais_de_lista(paises_encontrados)
        else:
            pais = paises_encontrados[0]
        
        # 3. Mostrar valores actuales
        mostrar_pais_valores_actuales(pais)
        
        # 4. Pedir nuevos valores
        poblacion_nueva, superficie_nueva = pedir_nuevos_valores(
            pais["poblacion"],
            pais["superficie"]
        )
        
        # 5. Pedir confirmación
        if not pedir_confirmacion_actualizacion(pais, poblacion_nueva, superficie_nueva):
            print("Operacion cancelada")
            return
        
        # 6. Actualizar país
        actualizar_pais_en_lista(pais, poblacion_nueva, superficie_nueva)
        
        # 7. Guardar en CSV
        try:
            guardar_paises_csv(paises)
            print("Pais actualizado correctamente y guardado en CSV")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Advertencia: No se pudo guardar en CSV: {error}")
            print("El pais fue actualizado en memoria pero no se guardaró permanentemente")
            
    except ValueError as error:
        if str(error) == "cancelado":
            print("Operacion cancelada")
        else:
            print(f"Error: {error}")


def menu_buscar_pais(paises):
    """menu_buscar_pais: Busca un país por nombre."""
    try:
        paises_encontrados = buscar_pais_por_nombre(paises)
        mostrar_lista_paises(paises_encontrados, "BÚSQUEDA DE PAÍS")
    except ValueError as error:
        print(f"Error: {error}")



def menu_filtrar(paises):
    """menu_filtrar: Filtra países según criterio seleccionado."""
    try:
        opcion_filtro = pedir_opcion_filtro(get_opciones_submenu_filtro())

        if opcion_filtro == 1:
            paises_filtrados = filtrar_por_continente(paises)
            mostrar_lista_paises(paises_filtrados, "PAÍSES FILTRADOS POR CONTINENTE")
        elif opcion_filtro == 2:
            paises_filtrados = filtrar_por_rango_poblacion(paises)
            mostrar_lista_paises(paises_filtrados, "PAÍSES FILTRADOS POR RANGO DE POBLACIÓN")
        elif opcion_filtro == 3:
            paises_filtrados = filtrar_por_rango_superficie(paises)
            mostrar_lista_paises(paises_filtrados, "PAÍSES FILTRADOS POR RANGO DE SUPERFICIE")
    except ValueError as error:
        print(f"Error: {error}")


def menu_ordenar(paises):
    """menu_ordenar: Ordena países según criterio y dirección seleccionados."""
    try:
        opcion_orden = pedir_opcion_ordenamiento(get_opciones_submenu_orden())

        if opcion_orden in [1, 2, 3]:
            tipo_orden = pedir_tipo_orden(get_opciones_submenu_tipo_orden())
            descendente = determinar_descendente(tipo_orden)

            if opcion_orden == 1:
                paises_ordenados = ordenar_por_nombre(paises, descendente)
                mostrar_lista_paises(paises_ordenados, "PAÍSES ORDENADOS POR NOMBRE")
            elif opcion_orden == 2:
                paises_ordenados = ordenar_por_poblacion(paises, descendente)
                mostrar_lista_paises(paises_ordenados, "PAÍSES ORDENADOS POR POBLACIÓN")
            elif opcion_orden == 3:
                paises_ordenados = ordenar_por_superficie(paises, descendente)
                mostrar_lista_paises(paises_ordenados, "PAÍSES ORDENADOS POR SUPERFICIE")
    except ValueError as error:
        print(f"Error: {error}")


def menu_estadisticas(paises):
    """menu_estadisticas: Calcula y muestra estadísticas según selección."""
    opcion_stats = pedir_opcion_estadistica(get_opciones_submenu_estadisticas())

    if opcion_stats == 1:
        estadistica_max_min_poblacion(paises)
    elif opcion_stats == 2:
        estadistica_promedio_poblacion(paises)
    elif opcion_stats == 3:
        estadistica_promedio_superficie(paises)
    elif opcion_stats == 4:
        estadistica_cantidad_por_continente(paises)


def menu_mostrar_todos(paises):
    """menu_mostrar_todos: Muestra todos los países cargados."""
    print("\n--- Todos los Países ---")
    try:
        validar_no_vacio(paises, "No hay países cargados.")
        for pais in paises:
            print(f"País: {pais['nombre']}")
            print(f"  Población: {formato_numero(pais['poblacion'])}")
            print(f"  Superficie: {formato_numero(pais['superficie'])} km²")
            print(f"  Continente: {pais['continente']}")
            print("-"*50)
    except ValueError as error:
        print(error)


def menu_salir():
    """menu_salir: Cierra el programa."""
    print("¡Hasta luego!")
    sys.exit(0)
