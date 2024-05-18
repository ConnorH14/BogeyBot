from objects.Reservation import Reservation
from helpers.ValidResponse import getValidResponse
from helpers.VerifyFormat import verifyDateFormat, verifyTimeFormat
from helpers.ClearConsole import clear


def createReservation():
    current_reservation = Reservation(
        getCourse(),
        getDate(),
        getPlayerCount(),
        getStartTime(),
        getHoleCount(),
        getStartNow(),
    )

    return current_reservation


def getCourse():
    print("Which course would you like to book your reservation at?")
    print("1. Quail Hollow")
    print("2. Warm Springs")

    while True:
        course = input("Type 1 or 2 to select your course: ")
        if course in ["1", "2"]:
            print("\nIs this the course you selected?")
            match course:
                case "1":
                    print("Quail Hollow\n")
                case "2":
                    print("Warm Springs\n")
            if getValidResponse() == "yes":
                break
        else:
            print("Please enter a valid response.")

    clear()
    return course


def getDate():
    print("Using mm/dd/yyyy format, please enter the date of your reservation.")

    while True:
        date = input("Reservation Date: ")

        if verifyDateFormat(date) == True:
            print("\nIs this the date you selected?")
            print(date + "\n")
            if getValidResponse() == "yes":
                break
            else:
                print("Please enter a valid date. ")
        else:
            print("Please enter a valid date. ")

    clear()
    return date


def getPlayerCount():
    print(
        "Please enter the number of players that will be attending. (Between 1 and 4)"
    )

    while True:
        player_count = input("Number of Players: ")

        if player_count in ["1", "2", "3", "4"]:
            print("\nIs this the correct number of players?")
            print(player_count + "\n")
            if getValidResponse() == "yes":
                break
            else:
                print("Please enter the number of players attending: ")
        else:
            print("Please enter the number of players attending: ")

    clear()
    return player_count


def getStartTime():
    print(
        "Would you like to input a reservation time or take the earliest time available?"
    )
    print(
        "If you select a time and it is not available, it will attempt to get the closest time."
    )
    print("1. Select a time.")
    print("2. Take the earliest time available.")

    while True:
        earliest_time = input("Select Option: ")
        if earliest_time in ["1", "2"]:
            print("\nIs this the option you selected?")
            match earliest_time:
                case "1":
                    print("Select a time.\n")
                case "2":
                    print("Take the earliest time available.\n")
            if getValidResponse() == "yes":
                break
            else:
                print("Please select one of the options.")
        else:
            print("Please select one of the options.")

    if earliest_time == "1":
        clear()
        print("\nUsing the format 00:00 am/pm, please select your time.")
        print("The time must be rounded to the closest quarter hour.")
        print("Example: 09:15 am\n")

        while True:
            start_time = input("Select Time: ").lower()

            if verifyTimeFormat(start_time) == True:
                print("Is this the time you selected?")
                print(start_time + "\n")
                if getValidResponse() == "yes":
                    break
                else:
                    print("Please enter a valid time. ")
            else:
                print("Please enter a valid time. ")
    else:
        start_time = "earliest"

    clear()
    return start_time


def getHoleCount():
    print("Type 1 or 2 to select the number of holes you will be playing.")
    print("1. 9 Holes")
    print("2. 18 Holes")

    while True:
        holes = input("Number of Holes: ")
        if holes in ["1", "2"]:
            print("\nIs this the correct number of holes?")
            match holes:
                case "1":
                    print("9 Holes\n")
                case "2":
                    print("18 Holes\n")
            if getValidResponse() == "yes":
                break
            else:
                print("Please select one of the options.")
        else:
            print("Please select one of the options.")

    clear()
    return holes


def getStartNow():
    print(
        "Would you like BogeyBot to run now and make a reservation or wait until midnight?"
    )
    print("1. I would like to make the reservation right now.")
    print("2. Wait until midnight to get the best time.")

    while True:
        start_now = input("Select Option: ")
        if start_now in ["1", "2"]:
            print("\nIs this the option you chose?")
            match start_now:
                case "1":
                    print("Make the reservation now.\n")
                case "2":
                    print("Wait until midnight.\n")
            if getValidResponse() == "yes":
                break
            else:
                print("Please select one of the options by typing 1 or 2.")
        else:
            print("Please select one of the options by typing 1 or 2.")

    clear()
    return start_now
