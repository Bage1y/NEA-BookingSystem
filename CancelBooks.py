# imports
import json,time
from PyQt5 import QtCore, QtGui, QtWidgets
from globalfunctions import jsonrefill

# cancelbooking
def cancelbooking():
    roomnumtest = int(input("Enter the room number: "))
    nametest = input("Enter the name of booking: ")
    file = open("record.json", 'r')
    data = file.read()
    file.close()
    editlist = json.loads(data)
    finallist = []
    for i in range(len(editlist)):
        if editlist[i]['Roomnum'] == roomnumtest and editlist[i]['BookingName'] == nametest:
            finallist.append(editlist[i])
    if not finallist:
        print("No bookings match entered details")
        time.sleep(1.5)
    else:
        recentbooking = finallist[len(finallist)]
        print("*Selected Booking details*\nRoom number: ", (recentbooking['Roomnum']), "\nBooking end date: ",
              (recentbooking['EndDate']))
        input()