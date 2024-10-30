import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_04 import es_impar_o_par 

def test_es_impar_o_par():
    assert es_impar_o_par(4) == "Es par"
