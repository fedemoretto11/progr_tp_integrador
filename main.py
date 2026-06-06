from utils.input import pedir_entero
from utils.csv import leer_paises_csv
from operaciones.gestion import agregar_pais, buscar_pais_por_nombre, mostrar_paises, actualizar_pais
from operaciones.filtros import filtrar_por_continente, filtrar_por_rango_poblacion, filtrar_por_rango_superficie
from operaciones.ordenamientos import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie, pedir_direccion_orden
from operaciones.estadisticas import estadistica_max_min_poblacion, estadistica_promedio_poblacion, estadistica_promedio_superficie, estadistica_cantidad_por_continente
from utils.menus import (
    mostrar_menu_principal,
    mostrar_submenu_filtro,
    mostrar_submenu_orden,
    mostrar_submenu_estadisticas,
    mostrar_submenu_tipo_orden
)





def main():
    opcion = 0
    
    try:
        paises = leer_paises_csv()
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
                actualizar_pais(paises)
            elif opcion == 3:
                paises_encontrados = buscar_pais_por_nombre(paises)
                mostrar_paises(paises_encontrados)
            elif opcion == 4:
                mostrar_submenu_filtro()
                try:
                    sub_opcion = pedir_entero("Ingrese una opcion: ")
                    if sub_opcion == 1:
                        paises_filtrados = filtrar_por_continente(paises)
                        mostrar_paises(paises_filtrados)
                    elif sub_opcion == 2:
                        paises_filtrados = filtrar_por_rango_poblacion(paises)
                        mostrar_paises(paises_filtrados)
                    elif sub_opcion == 3:
                        paises_filtrados = filtrar_por_rango_superficie(paises)
                        mostrar_paises(paises_filtrados)
                    elif sub_opcion == 4:
                        pass
                    else:
                        raise ValueError("Seleccione una opcion valida")
                except ValueError as error:
                    print(f"Error: {error}")
            elif opcion == 5:
                mostrar_submenu_orden()
                try:
                    sub_opcion = pedir_entero("Ingrese una opcion: ")
                    if sub_opcion in [1, 2, 3]:
                        mostrar_submenu_tipo_orden()
                        descendente = pedir_direccion_orden()
                        
                        if sub_opcion == 1:
                            paises_ordenados = ordenar_por_nombre(paises, descendente)
                        elif sub_opcion == 2:
                            paises_ordenados = ordenar_por_poblacion(paises, descendente)
                        elif sub_opcion == 3:
                            paises_ordenados = ordenar_por_superficie(paises, descendente)
                        
                        mostrar_paises(paises_ordenados)
                    elif sub_opcion == 4:
                        pass
                    else:
                        raise ValueError("Seleccione una opcion valida")
                except ValueError as error:
                    print(f"Error: {error}")
            elif opcion == 6:
                mostrar_submenu_estadisticas()
                try:
                    sub_opcion = pedir_entero("Ingrese una opcion: ")
                    if sub_opcion == 1:
                        estadistica_max_min_poblacion(paises)
                    elif sub_opcion == 2:
                        estadistica_promedio_poblacion(paises)
                    elif sub_opcion == 3:
                        estadistica_promedio_superficie(paises)
                    elif sub_opcion == 4:
                        estadistica_cantidad_por_continente(paises)
                    elif sub_opcion == 5:
                        pass
                    else:
                        raise ValueError("Seleccione una opcion valida")
                except ValueError as error:
                    print(f"Error: {error}")
            elif opcion == 7:
                mostrar_paises(paises)
            elif opcion == 8:
                print("Saliendo del sistema...")
            else:
                raise ValueError("Seleccione una opcion entre 1 y 8")
        except ValueError as error:
            print(f"Error: {error}")
        
        
if __name__ == "__main__":
    main()