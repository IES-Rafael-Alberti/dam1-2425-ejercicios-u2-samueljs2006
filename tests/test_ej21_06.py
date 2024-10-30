import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_06_1 import  determinar_grupo

def test_determinar_grupo():
    assert determinar_grupo("Ana", "mujer") == "Grupo A (mujer)"
    assert determinar_grupo("Zara", "mujer") == "Grupo B"
    assert determinar_grupo("Pedro", "hombre") == "Grupo A (hombre)"
    assert determinar_grupo("Carlos", "hombre") == "Grupo B"
