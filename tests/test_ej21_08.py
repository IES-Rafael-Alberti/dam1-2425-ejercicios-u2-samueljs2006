import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_08 import nivel

def test_nivel():
    assert nivel(0.0) == "nivel inaceptable 0.0"
    assert nivel(0.4) == "nivel aceptable 960.0"
    assert nivel(0.6) == "nivel meritorio 1440.0"
    assert nivel(1.0) == "nivel meritorio 2400.0"
    