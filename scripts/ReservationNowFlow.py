from playwright.async_api import async_playwright, Playwright


async def createReservationNow(user, url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print("Launching Browser")
        print("Found " + await page.title())

        await page.locator("//*[@id='grwebsearch_output_table']/tbody/tr[1]/td[1]/a").click()
        print("ping")

    return
