import asyncio
from scripts.UserInfo import createUser
from scripts.ReservationInfo import createReservation
from scripts.CreateReservation import createReservation
from helpers.BuildUrl import buildUrl
from helpers.WaitNextDay import waitForNextDay
from helpers.ClearConsole import clear

# TODO - For test data
from objects.Reservation import Reservation
from objects.User import User

clear()

print("Welcome to BogeyBot.\n")
# input("Press Enter to get Started ")

clear()

# Define new user and get user info
# current_user = createUser()
current_user = User("Chad", "Johnson", "chadjohnson4169@gmail.com", "2484345508")

# Get info for golf reservation
# current_reservation = createReservation()
current_reservation = Reservation("1", "05/27/2024", "4", "01:00 am", "18", "1")

# Determine which flow the bot needs to go into
# Two different flows are starting now or making a fast midnight reservation

url = buildUrl(current_reservation)

if current_reservation.start_now == "1":
    print("Creating Reservation Now.")
    asyncio.run(createReservation(current_user, url))
else:
    print("Creating Reservation at Midnight.")
    waitForNextDay()
    asyncio.run(createReservation(current_user, url))
