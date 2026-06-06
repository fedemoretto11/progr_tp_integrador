from utils.input import pedir_entero
from utils.csv import leer_paises_csv
from operaciones.gestion import agregar_pais, buscar_pais_por_nombre, mostrar_paises
from menus import (
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
        
        
if __name__ == "__main__":
    main()