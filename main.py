# imports
import json,time,sys
import os
from SearchFunc import typesearch
from datetime import datetime, timedelta
from database import editdatabase, recordsmenu
truepass = "ADMIN123"

# re-json-dump
def jsonrefill(parameter):
    file = open("rooms.json", 'w')
    file.close()
    file = open("rooms.json", "w")
    file.write(json.dumps(parameter))
    file.close()

# room resetting
def roomreset():
    file = open("rooms.json", 'r')
    data = file.read()
    file.close()
    editlist = json.loads(data)
    for i in range(len(editlist) - 1):
        selectedroom = editlist[i]
        if editlist[i]['Status'] == 'Unavailable':
            today = datetime.now()
            now = datetime.now()
            now = now.strftime("%H")
            now = int(now)
            # now+=1 #to change BST to GMT
            if editlist[i]['Date'] <= today.strftime("%d-%m-%Y") and now > 10:
                editlist[selectedroom['Roomnum'] - 1]['Status'] = "Available"
                editlist[selectedroom['Roomnum'] - 1]['Date'] = " "
                jsonrefill(editlist)
# print("Required rooms reset")
# time.sleep(1)
# resets rooms date and status

# total room reset
def totalroomreset():
    file = open("rooms.json", 'r')
    data = file.read()
    file.close()
    editlist = json.loads(data)
    for i in range(len(editlist) - 1):
        selectedroom = editlist[i]
        if editlist[i]['Status'] == 'Unavailable':
            editlist[selectedroom['Roomnum'] - 1]['Status'] = "Available"
            editlist[selectedroom['Roomnum'] - 1]['Date'] = " "
            jsonrefill(editlist)
    print("All rooms reset")
# resets all rooms date and status

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

# adminaccess
def adminaccess():
    tries = 3
    exitstatus = False
    while tries > 0 and exitstatus == False:
        passw = input("Enter administrator password: ")
        if passw == truepass:
            exitstatus = True
            print("Password Accepted")
            time.sleep(1)
            adminmenu()
        else:
            print("Invalid password, try again. \nYou have", tries, "attempts remaining\n")
            print("Attempts expended")

# admin menu
def adminmenu():
    while True:
        print(
            "Admin functions:\n1. Back\n2. Reset all rooms status records\n3. Access booking records\n4. Close the program")
        adminchoice = int(input("Enter the function which you would like to use: "))
        if adminchoice >= 1 and adminchoice <= 4:
            if adminchoice == 1:
                return exit
            elif adminchoice == 2:
                totalroomreset()
                time.sleep(1)
            elif adminchoice == 3:
                recordsmenu()
            elif adminchoice == 4:
                print("Program shutting down")
                countdown = 4
                for i in range(3):
                    countdown -= 1
                    print(countdown)
                    time.sleep(0.5)
                sys.exit()
        else:
            print("Invalid menu choice")
            time.sleep(1)

# txt based start menu
while True:
    roomreset()
    print("Available functions are:\n1. Make new booking\n2. Cancel booking\n3. Renew booking\n4. Admin menu")
    menuchoice = int(input("Enter the function you would like to use: "))
    if menuchoice >= 1 and menuchoice <= 4:
        if menuchoice == 1:
            newbooking()
        elif menuchoice == 2:
            cancelbooking()
        elif menuchoice == 3:
            print("WIP function")
        elif menuchoice == 4:
            adminaccess()
    else:
        print("Invalid menu choice")
