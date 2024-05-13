import re
import time
import random
import pytest
from funciones import Funciones_globales
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#https://docs.pytest.org/en/8.2.x/how-to/parametrize.html

#Ejecuta el test
#pytest ParametrizarDataDupla.py -s -v

#Ejecutar en paralelo
#pytest ParametrizarDataDupla.py -s -v --browser-channel=chrome -n 4

#Se parametriza los datos
data = [("gino","pass"),
        ("mario","pass"),
        ("chino","pass"),
        ("nacho","pass")]
@pytest.mark.parametrize("usr,passw",data)
def test_login_parametrizado(set_up_parametrizar,usr,passw) -> None:
    page = set_up_parametrizar
    F=Funciones_globales(page)
    F.EscribirTexto("//input[@id='user-name']",usr,0.1)
    F.EscribirTexto("//input[@id='password']",passw,0.1)
    F.clickElement("//input[@id='login-button']",0.1)
    F.Esperar(2)