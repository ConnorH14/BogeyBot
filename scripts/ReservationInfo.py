from objects.Reservation import Reservation
from helpers.ValidResponse import getValidResponse
from helpers.VerifyDateFormat import verifyDateFormat
from helpers.ClearConsole import clear

def createReservation():
  current_reservation = Reservation(
     getCourse(), 
     getDate(), 
     getPlayerCount(), 
     getStartTime(), 
     getHoleCount(), 
     1)
  
  return current_reservation

def getCourse():
  print('Which course would you like to book your reservation at?')
  print('1. Quail Hollow')
  print('2. Warm Springs')

  while True:
    course = input('Type 1 or 2 to select your course: ')
    if course in ['1', '2']:
        print('Is this the course you selected?')
        match course:
          case '1':
            print('Quail Hollow\n')
          case '2':
            print('Warm Springs\n')
        if getValidResponse() == 'yes':
            break
    else:
       print('Please enter a valid response.')
        
  clear()
  return course

def getDate():
  print('Using mm/dd/yyyy format, please enter the date of your reservation.')

  while True:
    date = input('Reservation Date: ')

    if verifyDateFormat(date) == True:
      print('Is this the date you selected?')
      print(date + '\n')
      if getValidResponse() == 'yes':
        break
      else:
        print('Please enter a valid date: ')
    else:
      print('Please enter a valid date: ')

  clear()
  return date

def getPlayerCount():
  print('Please enter the number of players that will be attending. (Between 1 and 4)')

  while True:
    player_count = input('Number of Players: ')

    if player_count in ['1', '2', '3', '4']:
      print('Is this the correct number of players?')
      print(player_count + '\n')
      if getValidResponse() == 'yes':
        break
      else:
        print('Please enter the number of players attending: ')
    else:
      print('Please enter the number of players attending: ')

  clear()
  return player_count

def getStartTime():
  print()
  return 1

def getHoleCount():
  print('Type 1 or 2 to select the number of holes you will be playing')
  print('1. 9 Holes')
  print('2. 18 Holes')

  while True:
    holes = input('Number of Holes: ')
    if holes in ['1', '2']:
      print('Is this the correct number of holes?')
      match holes:
          case '1':
            print('9 Holes\n')
          case '2':
            print('18 Holes\n')
      if getValidResponse() == 'yes':
        break
      else:
        print('Please select one of the options.')
    else:
      print('Please select one of the options.')

  clear()
  return holes
