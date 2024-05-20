import datetime


def waitForNextDay():

    start_date = datetime.datetime.now().strftime("%m/%d/%Y")
    print("Waiting until midnight...")

    while True:
        current_date = datetime.datetime.now().strftime("%m/%d/%Y")
        if current_date != start_date:
            return
