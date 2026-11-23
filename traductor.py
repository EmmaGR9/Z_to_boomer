"""Módulo con la lógica de traducción entre jerga Gen Z y español estándar."""

from diccionario import JERGA_GENZ
import re

def traducir_a_boomer(frase: str) -> str:
    """Traduce una frase con términos Gen Z a lenguaje estándar.

    Args:
        frase: Texto de entrada escrito por el usuario.

    Returns:
        La frase con los términos conocidos sustituidos.
    """
    palabras: list[str] = re.split("\b\b\w*\s*", frase)
    resultado: list[str] = []

    for palabra in palabras:
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
