from playwright.sync_api import sync_playwright
import pytest
import os


def test_without_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        os.makedirs("output", exist_ok=True)
        page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/1.png")
        browser.close()
