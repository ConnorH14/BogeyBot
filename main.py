import asyncio
from scripts.UserInfo import createUser
from scripts.ReservationInfo import createReservation
from scripts.CreateReservation import launchReservation
from helpers.BuildUrl import buildUrl
from helpers.WaitNextDay import waitForNextDay
from helpers.ClearConsole import clear

clear()

print("Welcome to BogeyBot.\n")
input("Press Enter to get Started ")

clear()

# Define new user and get user info
current_user = createUser()

# Get info for golf reservation
current_reservation = createReservation()

# Determine which flow the bot needs to go into
# Two different flows are starting now or making a fast midnight reservation

url = buildUrl(current_reservation)

if current_reservation.start_now == "1":
    print("Creating Reservation Now.")
    asyncio.run(launchReservation(current_user, url))
else:
    print("Creating Reservation at Midnight.")
    waitForNextDay()
    asyncio.run(launchReservation(current_user, url))
