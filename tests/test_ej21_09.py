import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_09_1 import precio_entrada

def test_precio_entrada():
    assert precio_entrada(2) == "entra gratis"    
    assert precio_entrada(4) == "paga 5€"        
    assert precio_entrada(10) == "paga 5€"        
    assert precio_entrada(18) == "paga 10€"      
    assert precio_entrada(25) == "paga 10€"