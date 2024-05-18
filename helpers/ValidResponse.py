def getValidResponse():
    valid_response = False
    while not valid_response:
        response = input("Type Yes or No and then Press Enter: ").lower()

        valid_response = response in ["no", "yes"]

    return response
