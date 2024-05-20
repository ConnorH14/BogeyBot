from helpers.BuildUrl import buildUrl
from playwright.async_api import async_playwright, Playwright


async def createReservationLater(user, url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print("Launching Browser")
        print("Found " + await page.title())

    return
