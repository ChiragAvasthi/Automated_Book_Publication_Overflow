from playwright.sync_api import sync_playwright

def scrape_chapter(url, screenshot_name="chapter.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=60000)
        content = page.inner_text("body")
        page.screenshot(path=f"static/images/{screenshot_name}")
        browser.close()
        return content
