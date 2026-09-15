# GitHub-test
from playwright.sync_api import sync_playwright

def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto("https://monsite.com/login")

        page.fill("#username", "test")
        page.fill("#password", "test123")

        page.click("button[type='submit']")

        page.wait_for_timeout(2000)

        assert "Accueil" in page.title()

        browser.close()
