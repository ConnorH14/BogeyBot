def verifyPhoneNumber(input_phone_number):
    if len(input_phone_number) != 10:
        return False

    return containsOnlyDigits(input_phone_number)


def verifyDateFormat(input_date):

    if len(input_date) != 10:
        return False

    if input_date[2] != "/" and input_date[5] != "/":
        return False

    number_input = input_date.replace("/", "")

    return containsOnlyDigits(number_input)


def containsOnlyDigits(number_input):
    return all(char.isdigit() for char in number_input)


def verifyTimeFormat(time_input):
    if (
        len(time_input) == 8
        and time_input[2] == ":"
        and (time_input[4] == "0" or time_input[4] == "5")
    ):
        meridiem_time = time_input[6:]
        if meridiem_time in {"am", "pm"}:
            time_digits = time_input[:2] + time_input[3:5]
            return containsOnlyDigits(time_digits)
    return False
