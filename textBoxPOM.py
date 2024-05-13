import re
import time
from funciones import Funciones_globales
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#playwright show-trace trace.zip

def test_checkbox(playwright: Playwright)-> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=100)
    context = browser.new_context(
        viewport={'width':1500, 'height':800},
        record_video_dir="video/input"
    )

    #Iniciar trace viewer
    context.tracing.start(screenshots=True, snapshots=True,sources=True)


    #Open new page
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    #Creo objetivo de tipo funciones
    F=Funciones_globales(page)
    F.ScrollYX(0,100,0.5)
    F.EscribirTexto("//input[@id='userName']","Gino Jimenez",0.1)
    F.EscribirTexto("//input[@id='userEmail']","ginomario@gmail.com",0.1)
    F.EscribirTexto("//textarea[@id='currentAddress']","Av hipolito unanue 564",0.1)
    F.EscribirTexto("//textarea[@id='permanentAddress']","Av santa ana 448",0.1)
    F.clickElement("//button[@id='submit']",0.5)
    F.Esperar(3)


    #Cerrar trace viewer
    context.tracing.stop(path="trace.zip")

    #Close browser
    context.close()
    browser.close()