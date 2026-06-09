from utils.csv import leer_paises_csv
from utils.input import pedir_opcion_menu
from utils.menus import get_opciones_menu_principal, get_titulo_menu_principal
from utils.menu_handlers import (
    menu_agregar_pais, menu_actualizar_pais, menu_buscar_pais,
    menu_filtrar, menu_ordenar, menu_estadisticas, menu_mostrar_todos, menu_salir
)


def main():
    paises = leer_paises_csv()
    print("\n=== Gestor de Países ===\n")

    while True:
        opciones = get_opciones_menu_principal()
        opcion = pedir_opcion_menu(opciones, "Selecciona una opción: ")
        
        if opcion == 1:
            menu_agregar_pais(paises)
        elif opcion == 2:
            menu_actualizar_pais(paises)
        elif opcion == 3:
            menu_buscar_pais(paises)
        elif opcion == 4:
            menu_filtrar(paises)
        elif opcion == 5:
            menu_ordenar(paises)
        elif opcion == 6:
            menu_estadisticas(paises)
        elif opcion == 7:
            menu_mostrar_todos(paises)
        elif opcion == 8:
            menu_salir()

if __name__ == "__main__":
    main()
