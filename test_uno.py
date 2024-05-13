import re
from playwright.sync_api import Page, expect

def test_uno(page: Page):
    page.goto("http://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    page.screenshot(path="imagenes/test1.jpg")
    buton_uno = page.locator("text=Get started")
    #expect(buton_uno.title).to_have_attribute("href","/docs/intro")
    buton_uno.click()

    page.screenshot(path="imagenes/test2.jpg")
    expect(page).to_have_url(re.compile("https://playwright.dev/docs/intro"))