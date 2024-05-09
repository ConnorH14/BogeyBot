from objects.Reservation import Reservation
from helpers.ValidResponse import getValidResponse
from helpers.ClearConsole import clear

def createReservation():
  current_reservation = Reservation(
     getCourse(), 
     getDate(), 
     1, 
     1, 
     1, 
     1)
  
  return current_reservation

def getCourse():
  print('Which course would you like to book your reservation at?')
  print('1. Quail Hollow')
  print('2. Warm Springs')
  course = 0

  while True:
    response = int(input('Type 1 or 2 to select your course: '))
    if response in [1, 2]:
        course = response
        print('Is this the course you selected?')
        match response:
          case 1:
            print('Quail Hollow\n')
          case 2:
            print('Warm Springs\n')
        if getValidResponse() == 'yes':
            break
        
  clear()
  return course

def getDate():
   return 2