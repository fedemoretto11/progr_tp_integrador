
def formato_numero(n: int | float) -> str:
    """Formatea número con separadores de miles para visualización."""
    return f"{n:,}".replace(",", ".")

