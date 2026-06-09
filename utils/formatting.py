
def formato_numero(n: int | float) -> str:
    """formato_numero: Formatea número con separadores de miles."""
    return f"{n:,}".replace(",", ".")


def mostrar_lista_paises(paises, titulo="RESULTADOS"):
    """mostrar_lista_paises: Muestra lista de países con formato legible."""
    print("\n" + "="*50)
    print(titulo)
    print("="*50)
    for pais in paises:
        print(f"País: {pais['nombre']}")
        print(f"  Población: {formato_numero(pais['poblacion'])}")
        print(f"  Superficie: {formato_numero(pais['superficie'])} km²")
        print(f"  Continente: {pais['continente']}")
        print("-"*50)


