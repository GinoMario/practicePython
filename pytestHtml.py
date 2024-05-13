import re
import time
import random
import pytest
from funciones import Funciones_globales
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#Instalar pytest html
#https://pypi.org/project/pytest-html/
#pip install pytest-html

#pytest -s -v pytestHtml.py -n 2 --html=reporte.html
#pytest -s -v pytestHtml.py -n 2 --html=reporte.html --self-contained-html --capture=tee-sys


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