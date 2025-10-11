from playwright.sync_api import sync_playwright

def get_page_content(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport = { "width": 1920, "height": 1080 })
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state(state="domcontentloaded", timeout=10000)
        page.wait_for_timeout(3000)
        return page.content()