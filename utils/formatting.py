
def formato_numero(n: int | float) -> str:
    """formato_numero: Formatea número con separadores de miles."""
    return f"{n:,}".replace(",", ".")

