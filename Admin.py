# imports
import json,time,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from globalfunctions import jsonrefill
from database import  recordsmenu
truepass = "ADMIN123"

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