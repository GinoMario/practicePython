import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

class Funciones_globales:
    #Constructor iniciador
    def __init__(self,page):
        self.page = page

    def Esperar(self,tiempo=0.5):
        time.sleep(tiempo)

    def ScrollYX(self,x,y,tiempo=0.5):
        self.page.mouse.wheel(x,y)
        time.sleep(tiempo)


    def EscribirTexto(self,selector,texto,tiempo=0.5):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.click()
        t.fill(texto)
        time.sleep(tiempo)

    def clickElement(self, selector, tiempo=0.5):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        time.sleep(tiempo)