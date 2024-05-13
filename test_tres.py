import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def test_tres(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("DEMOQA")