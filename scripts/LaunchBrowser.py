from playwright.async_api import async_playwright, Playwright

url = "https://web2.myvscloud.com/wbwsc/idboisewt.wsc/search.html?module=gr&display=detail&secondarycode=1"


async def launchBrowser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print("Launching Browser")
        print("Found " + await page.title())
        await browser.close()
