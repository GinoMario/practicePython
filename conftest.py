import re
import time
import random
import pytest
import sys
from funciones import Funciones_globales
from playwright.sync_api import Page, expect, Playwright, sync_playwright

tiempo = 0.2
ruta = "imagenes/upload/"
pdf = ""
url = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def set_up(playwright:  Playwright)-> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=100)
    context = browser.new_context(
        viewport={'width':1500, 'height':800},
        #record_video_dir="video/input"
    )

    #Iniciar trace viewer
    context.tracing.start(screenshots=True, snapshots=True,sources=True)
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(3000)
    F = Funciones_globales(page)

    F.clickElement("//input[@id='user-name']")
    F.EscribirTexto("//input[@id='user-name']","standard_user",0.1)
    F.clickElement("//input[@id='password']")
    F.EscribirTexto("//input[@id='password']","secret_sauce",0.1)
    F.clickElement("//input[@id='login-button']")

    yield page

    #Cerrar trace viewer
    context.tracing.stop(path="trace.zip")
    #Close browser
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def set_up_parametrizar(playwright: Playwright) ->None:
    browser = playwright.chromium.launch(headless=False,slow_mo=100)
    context = browser.new_context(
        viewport={'width':1200, 'height':800}
    )
    #Iniciar trace viewer
    context.tracing.start(screenshots=True, snapshots=True,sources=True)
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(3000)
    yield page
    #Cerrar trace viewer
    context.tracing.stop(path="trace.zip")
    #Close browser
    context.close()
    browser.close()
