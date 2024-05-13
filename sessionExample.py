import re
import time
import random
from funciones import Funciones_globales
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#pytest sessionExample.py -s -v

def test_session1(set_up)-> None:
    page = set_up

def test_session2(set_up)-> None:
    page = set_up
    F = Funciones_globales(page)
    F.clickElement("//button[@id='add-to-cart-sauce-labs-backpack']")
    F.clickElement("//button[@id='add-to-cart-sauce-labs-bike-light']")

