from playwright.sync_api import sync_playwright

def test_google_search():

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto("https://www.google.com")

        page.locator("textarea[name='q']").fill("Playwright")

        page.locator("textarea[name='q']").press("Enter")

        page.wait_for_timeout(3000)

        # Capture d'écran des résultats
        page.screenshot(path="google.png")

        assert "Playwright" in page.title()

        browser.close()
