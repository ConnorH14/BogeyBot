def verifyDateFormat(input_date):

    if len(input_date) != 10:
        return False

    if input_date[2] != "/" and input_date[5] != "/":
        return False

    number_input = input_date.replace("/", "")

    return containsOnlyDigits(number_input)


def containsOnlyDigits(number_input):
    return all(char.isdigit() for char in number_input)
