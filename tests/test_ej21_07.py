import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_07 import  tipo_de_impositivo

def test_tipo_de_impositivo():
    assert tipo_de_impositivo(5000) == "tipo de impositivo 5%"