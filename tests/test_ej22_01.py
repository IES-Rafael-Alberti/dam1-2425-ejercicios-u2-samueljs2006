import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucles.ej22_01_1 import monstra_mas_veces

def test_monstra_mas_veces():
    assert monstra_mas_veces("hola") == ["hola"] * 10