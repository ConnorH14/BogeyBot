import time
import asyncio
from scripts.UserInfo import createUser
from scripts.ReservationInfo import createReservation
from playwright.async_api import async_playwright

# Print the title for the Application
print('''
 ____                         ____        _   
|  _ \                       |  _ \      | |  
| |_) | ___   __ _  ___ _   _| |_) | ___ | |_ 
|  _ < / _ \ / _` |/ _ \ | | |  _ < / _ \| __|
| |_) | (_) | (_| |  __/ |_| | |_) | (_) | |_ 
|____/ \___/ \__, |\___|\__, |____/ \___/ \__|
              __/ |      __/ |                
             |___/      |___/                 \n''')

print("Welcome to BogeyBot.\n")

# Define new user and get user info
current_user = createUser()

# Get info for golf reservation
current_reservation = createReservation()


# TODO Debug line to verify user -- remove
print(current_user.email, current_user.first_name, current_user.last_name, current_user.phone_number)



