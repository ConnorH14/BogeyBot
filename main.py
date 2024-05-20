import asyncio
from scripts.UserInfo import createUser
from scripts.ReservationInfo import createReservation
from scripts.ReservationNowFlow import createReservationNow
from scripts.ReservationLaterFlow import createReservationLater
from helpers.BuildUrl import buildUrl
from helpers.ClearConsole import clear

# TODO - For test data
from objects.Reservation import Reservation
from objects.User import User

clear()

print("Welcome to BogeyBot.\n")
input("Press Enter to get Started ")

clear()

# Define new user and get user info
# current_user = createUser()
current_user = User("Tester", "Testington", "test@test.com", "2088088080")

# Get info for golf reservation
# current_reservation = createReservation()
current_reservation = Reservation("1", "05/27/2024", "4", "09:00 am", "9", "1")

# Determine which flow the bot needs to go into
# Two different flows are starting now or making a fast midnight reservation

url = buildUrl(current_reservation)

print(url)

if current_reservation.start_now == "1":
    print("now")
    asyncio.run(createReservationNow(current_user, url))
else:
    print("later")
    asyncio.run(createReservationLater(current_user, url))
