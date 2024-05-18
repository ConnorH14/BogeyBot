from pages.SearchPage import SearchPage
from playwright.async_api import async_playwright, Playwright


async def searchReservation(page, user, reservation):
    search_page = SearchPage(page)

    await search_page.selectCourse(reservation.course)
    return
