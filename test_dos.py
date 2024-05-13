import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#pytest --slowmo 200 --headed test_dos.py

#def test_dos (page: Page):
def test_dos(playwright: Playwright)->None:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    #context = browser.new_context()
    context = browser.new_context(record_video_dir="video/input")
    context = browser.new_context(
        viewport={'width':1500, 'height':800}
    )

    time.sleep(5)
    page = context.new_page()

    page.goto("https://demoqa.com/")
    expect(page).to_have_title("DEMOQA")

    botonElements = page.locator("text=Elements")
    botonElements.click()

    botonTextBox = page.locator("text=Text Box")
    botonTextBox.click()

    tbName = page.locator("#userName")
    tbName.fill("Gino")

    tbName = page.locator("#userEmail")
    tbName.fill("ginomariojt@gmail.com")

    taAdress = page.locator("//textarea[@id='currentAddress']")
    taAdress.fill("Mensaje de prueba")

    taAdressP = page.locator("//textarea[@id='permanentAddress']")
    taAdressP.fill("Mensaje de prueba permanente")
