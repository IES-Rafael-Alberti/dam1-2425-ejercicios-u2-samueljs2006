import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_02 import comprobar_contraseña

def test_comprobar_contraseña():
    assert comprobar_contraseña("123abc") == "correcta"
    assert comprobar_contraseña("password") == "incorrecto"
