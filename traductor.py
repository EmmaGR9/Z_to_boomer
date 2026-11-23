"""Módulo con la lógica de traducción entre jerga Gen Z y español estándar."""

from diccionario import JERGA_GENZ

def traducir_a_boomer(frase: str) -> str:
    """Traduce una frase con términos Gen Z a lenguaje estándar.

    Args:
        frase: Texto de entrada escrito por el usuario.

    Returns:
        La frase con los términos conocidos sustituidos.
    """
    palabras: list[str] = frase.split()
    resultado: list[str] = []

    for palabra in palabras:
        cap = False
        if palabra[0] == palabra[0].upper():
            cap = True
        if palabra.lower() in JERGA_GENZ:
            res = JERGA_GENZ[palabra]
            if cap:
                res = res[0].upper() + res[1:]
            resultado.append(res)
        else:
            resultado.append(palabra)
        if palabra in JERGA_GENZ:
            resultado.append(JERGA_GENZ[palabra])
        else:
            resultado.append(palabra)

    return " ".join(resultado)


def traducir_a_genz(frase: str) -> str:
    """Traduce una frase estándar a jerga Gen Z.

    Args:
        frase: Texto en español estándar.

    Returns:
        La frase adaptada a jerga juvenil.
    """
    return frase
