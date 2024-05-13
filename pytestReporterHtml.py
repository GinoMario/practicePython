#pytest reporter html
#https://pypi.org/project/pytest-reporter-html1/

#Instalar
#pip install pytest-reporter-html1

#Ejecutar
#pytest pytestReporterHtml.py -s -v -n 4 --template=html1/index.html --report=reporte3.html
import re
import time
import random
import pytest
from funciones import Funciones_globales
from playwright.sync_api import Page, expect, Playwright, sync_playwright


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