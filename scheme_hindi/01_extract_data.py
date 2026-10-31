from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.myscheme.gov.in/hi/schemes/pm-kisan", wait_until="networkidle")
    text = page.inner_text("body")
    browser.close()
print(text[:3000])