from helpers.ValidResponse import getValidResponse
from objects.User import User
from helpers.ClearConsole import clear

def createUser():
  user_name = getUserName()
  current_user = User(
    getUserEmail(),
    user_name['first'],
    user_name['last'],
    getPhoneNumber()
  )
  
  return current_user

def getUserEmail():
  print("Please enter the email you would like your Golf Reservation to be sent to.")

  user_email = input("Email: ")

  confirm_email = False

  while not confirm_email:
    print("Is this the correct email?")
    print(user_email + "\n")

    if getValidResponse() == 'yes':
      confirm_email = True
    else:
      print("What email should be used?")
      user_email = input("Email: ")

  clear()
  return user_email

def getUserName():
  full_name = {'first': '', 'last': ''}
  
  full_name['first'] = getName('First')
  full_name['last'] = getName('Last')

  clear()
  return  full_name

def getName(name_type):
  print(f"Please enter the {name_type} Name you would like to use.")
  name = input(f"{name_type} Name: ")

  confirm_name = False

  while not confirm_name:
    print(f"Is this the {name_type} Name you would like to use?")
    print(name + "\n")

    if getValidResponse() == 'yes':
      confirm_name = True
    else:
      print(f"What is the {name_type} Name you would like to use?")
      name = input(f"{name_type} Name: ")

  clear()
  return name

def getPhoneNumber():
  print("Please enter the phone number you would like reservation to be associated with.")

  phone_number = input("Phone Number: ")

  confirm_phone_number = False

  while not confirm_phone_number:
    print("Is this the correct phone number?")
    print(phone_number + "\n")

    if getValidResponse() == 'yes':
      confirm_phone_number = True
    else:
      print("What email should be used?")
      phone_number = input("Email: ")

  clear()
  return phone_number