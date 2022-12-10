# imports
import json,time,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from SearchFunc import typesearch
from datetime import datetime, timedelta
from database import editdatabase
from main import jsonrefill

def newbooking():
    # collect room type as input
    file = open("rooms.json", 'r')
    data = file.read()
    file.close()
    fulldata = json.loads(data)
    print("1. Single\n2. Twin\n3. Couple\n4. Family\n")
    room = int(input("Enter the number type of room you would like: "))

    booklength = int(input("Enter number of nights to book for: "))
    bookingname = input("Enter the name to book under: ")
    dateObj = datetime.today()
    enddate = dateObj + timedelta(days=booklength)
    enddate = enddate.strftime("%d-%m-%Y")
    enddate = enddate.split(' ')[0]
    startdate = dateObj.strftime("%d-%m-%Y")
    # validation
    if room >= 1 and room <= 4 and booklength > 0:
        selectedroom = typesearch(room)
        # book selected room y/n input and changing room status
        roomtypes = {1: 'Single', 2: 'Twin', 3: 'Couple', 4: 'Family'}
        print("*Booking details*\nChosen room type: ", roomtypes[room], "\nNumber of nights: ", booklength,
              "\nAssigned room: Room", fulldata[selectedroom['Roomnum'] - 1]['Roomnum'], "\nBooking end date: ",
              enddate)
        bookroom = input("Book room? y/n: ")
        if bookroom == 'y':
            fulldata[selectedroom['Roomnum'] - 1]['Status'] = "Unavailable"
            fulldata[selectedroom['Roomnum'] - 1]['Date'] = enddate
            jsonrefill(fulldata)
            roomnumber = fulldata[selectedroom['Roomnum'] - 1]['Roomnum']
            editdatabase(roomnumber, bookingname, startdate, enddate)
            print("Room succesfully booked")
        elif bookroom == 'n':
            print("Room not booked")
        else:
            print("Invalid input")