import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_01 import es_mayor

def test_es_mayor():
    assert es_mayor(18) =="eres mayor de edad"
    assert es_mayor(16) =="eres menor de edad"