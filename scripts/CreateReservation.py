from playwright.async_api import async_playwright, Playwright


async def createReservation(user, url):
    async with async_playwright() as p:
        print("Launching Browser.")
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print("Found " + await page.title())

        # Try to create a reservation and throw an error if unable

        try:
            # Click first reservation available on the page
            await page.locator("//*[@id='grwebsearch_output_table']/tbody/tr[1]/td[1]/a").click()

            # Fill out user info in the form
            await page.locator("//*[@id='processingprompts_dailyfirstname']").fill(user.first_name)
            await page.locator("//*[@id='processingprompts_dailylastname']").fill(user.last_name)
            await page.locator("//*[@id='processingprompts_dailyphone']").fill(user.phone_number)
            await page.locator("//*[@id='processingprompts_dailyemail']").fill(user.email)

            # Click continue on form
            # await page.locator("//*[@id='processingprompts_buttononeclicktofinish']").click()

        except:
            print("Unable to create reservation.")
            print("Please verify a valid time and date was entered.")

        print("ping")

    return
