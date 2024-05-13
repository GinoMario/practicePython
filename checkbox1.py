import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def test_checkbox(playwright: Playwright)-> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")


    cb1 = page.locator("//button[contains(@aria-label,'Toggle')]")
    expect(cb1).to_be_visible()
    cb1.click()

    cb2 = page.locator("(//button[contains(@aria-label,'Toggle')])[3]")
    expect(cb2).to_be_visible()
    cb2.click()

    cb3 = page.locator("text=WorkSpace")
    expect(cb3).to_be_visible()
    cb3.click()

    #Cerrar context y navegador
    context.close()