import time
import asyncio
from scripts.UserInfo import createUser
from scripts.ReservationInfo import createReservation
from helpers.ClearConsole import clear
from playwright.async_api import async_playwright

clear()

print("Welcome to BogeyBot.\n")
input("Press Enter to get Started ")

clear()

# Define new user and get user info
current_user = createUser()

# Get info for golf reservation
current_reservation = createReservation()


# TODO Debug lines to verify user and reservation-- remove
print(
    current_user.email,
    current_user.first_name,
    current_user.last_name,
    current_user.phone_number,
)
print(
    current_reservation.course,
    current_reservation.date,
    current_reservation.player_count,
    current_reservation.time,
    current_reservation.holes,
    current_reservation.start_now,
)
