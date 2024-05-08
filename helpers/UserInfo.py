
from helpers.ValidResponse import getValidResponse
from objects.User import User

def createUser():
  current_user = User
  current_user.email = getUserEmail()
  user_name = getUserName()
  current_user.first_name = user_name['first']
  current_user.last_name = user_name['last']

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

  return user_email

def getUserName():
  full_name = {'first': '', 'last': ''}
  
  full_name['first'] = getName('First')
  full_name['last'] = getName('Last')

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

  return name