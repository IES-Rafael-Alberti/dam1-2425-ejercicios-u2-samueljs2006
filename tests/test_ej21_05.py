import sys
import os
import pytest
# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.condicionales.ej21_05 import pedir_edad, pedir_ingreso

def test_pedir_edad():
    assert pedir_edad(15) == False  
    assert pedir_edad(16) == True   
    assert pedir_edad(20) == True  
def test_pedir_ingreso():
    assert pedir_ingreso(500) == False   
    assert pedir_ingreso(1000) == True   
    assert pedir_ingreso(1500) == True    
def test_tributa():
    assert pedir_edad(20) and pedir_ingreso(1200) == "si tributa"   
    assert pedir_edad(15) and pedir_ingreso(1200) == "no tributa"  
    assert pedir_edad(20) and pedir_ingreso(800) == "no tributa"