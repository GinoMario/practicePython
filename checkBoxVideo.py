import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def test_checkbox(playwright: Playwright)-> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context(
        viewport={'width':1500, 'height':800},
        record_video_dir="video/input"
    )

    #Open new page
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")


    #Close browser
    context.close()
    browser.close()
