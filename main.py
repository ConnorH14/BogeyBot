import asyncio
from scripts.UserInfo import createUser
from scripts.ReservationInfo import createReservation
from scripts.SearchReservation import searchReservation
from helpers.ClearConsole import clear
from playwright.async_api import async_playwright, Playwright

# TODO - For test data
from objects.Reservation import Reservation
from objects.User import User

clear()

print("Welcome to BogeyBot.\n")
input("Press Enter to get Started ")

clear()

# Define new user and get user info
# current_user = createUser()
current_user = User("Connor", "Hines", "test@test.com", "2088095016")

# Get info for golf reservation
# current_reservation = createReservation()
current_reservation = Reservation("2", "05/20/2024", "4", "09:15 am", "2", "1")


# TODO Debug lines to verify user and reservation-- remove
# print(
#     current_user.email,
#     current_user.first_name,
#     current_user.last_name,
#     current_user.phone_number,
# )
# print(
#     current_reservation.course,
#     current_reservation.date,
#     current_reservation.player_count,
#     current_reservation.time,
#     current_reservation.holes,
#     current_reservation.start_now,
# )

url = "https://web2.myvscloud.com/wbwsc/idboisewt.wsc/search.html?module=gr&display=detail&secondarycode=1"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print("Launching Browser")
        print("Found " + await page.title())

        await searchReservation(page, current_user, current_reservation)


asyncio.run(main())
