# imports
import json,time
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta
from database import editdatabase
from globalfunctions import jsonrefill,linearsearch

def backgroundbooking(room,bookingname,booklength):
    dateObj = datetime.today()
    enddate = dateObj + timedelta(days=booklength)
    enddate = enddate.strftime("%d-%m-%Y")
    enddate = enddate.split(' ')[0]
    startdate = dateObj.strftime("%d-%m-%Y")
    # validation
    if booklength > 0:
        roomtypes = {1: 'Single', 2: 'Twin', 3: 'Couple', 4: 'Family'}
        file = open("rooms.json", 'r')
        data = file.read()
        file.close()
        fulldata = json.loads(data)
        room = roomtypes[room]
        editlist = fulldata
        editlist = linearsearch(editlist, room, 'Type')
        if not editlist:
            return False
        else:
            selectedroom = editlist[0]
            file = open("rooms.json", 'r')
            data = file.read()
            file.close()
            fulldata = json.loads(data)
            fulldata[selectedroom['Roomnum'] - 1]['Status'] = "Unavailable"
            fulldata[selectedroom['Roomnum'] - 1]['Date'] = enddate
            jsonrefill(fulldata)
            roomnumber = fulldata[selectedroom['Roomnum'] - 1]['Roomnum']
            editdatabase(roomnumber, bookingname, startdate, enddate)
            print("Room succesfully booked")
            return True
    else:
        print("Invalid input")

# all preferences search function
def typesearch(room):
    roomtypes = {1: 'Single', 2: 'Twin', 3: 'Couple', 4: 'Family'}
    file = open("rooms.json", 'r')
    data = file.read()
    file.close()
    fulldata = json.loads(data)
    room = roomtypes[room]
    editlist = fulldata
    editlist = linearsearch(editlist, room, 'Type')
    if not editlist:
        print("No available rooms of selected type")
    else:
        return editlist[0]

def newbooking():
    while True:
        class Ui_NewBookingWindow(object):
            def setupUi(self, NewBookingWindow):
                NewBookingWindow.setObjectName("NewBookingWindow")
                NewBookingWindow.resize(938, 821)
                #detail
                self.centralwidget = QtWidgets.QWidget(NewBookingWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.Frame1 = QtWidgets.QFrame(self.centralwidget)
                self.Frame1.setGeometry(QtCore.QRect(0, 0, 71, 841))
                self.Frame1.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
                self.Frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Frame1.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Frame1.setObjectName("Frame1")
                #back button
                self.BackButton = QtWidgets.QPushButton(self.Frame1)
                self.BackButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
                self.BackButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.864, y1:0.892045, x2:0.124591, y2:0.165, stop:0 rgba(0, 104, 113, 255), stop:1 rgba(7, 7, 9, 210));\n""color: rgb(215, 219, 218);\n""border-width: 10px;\n""border-color: rgb(135, 135, 135);\n""border-radius: 10px;\n""")
                self.BackButton.setObjectName("BackButton")
                self.BackButton.clicked.connect(self.__exit__)
                #detail
                self.Frame1_2 = QtWidgets.QFrame(self.centralwidget)
                self.Frame1_2.setGeometry(QtCore.QRect(70, 0, 871, 71))
                self.Frame1_2.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
                self.Frame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Frame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Frame1_2.setObjectName("Frame1_2")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(50, 60, 891, 761))
                self.frame.setStyleSheet("border-width: 3px;\n""background-color: rgb(26, 26, 26);\n""border-radius: 10px;\n""")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.textBrowser = QtWidgets.QTextBrowser(self.frame)
                self.textBrowser.setGeometry(QtCore.QRect(10, 10, 621, 91))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(48)
                self.textBrowser.setFont(font)
                self.textBrowser.setStyleSheet("color: rgb(237, 237, 237);\n""background-color: qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(23, 25, 23, 158));")
                self.textBrowser.setObjectName("textBrowser")
                self.nightslabel = QtWidgets.QLabel(self.frame)
                self.nightslabel.setGeometry(QtCore.QRect(10, 450, 311, 61))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(14)
                #number-of-nights label
                self.nightslabel.setFont(font)
                self.nightslabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.nightslabel.setObjectName("nightslabel")
                #reference calendar
                self.Calendar = QtWidgets.QCalendarWidget(self.frame)
                self.Calendar.setGeometry(QtCore.QRect(520, 140, 331, 301))
                self.Calendar.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.Calendar.setObjectName("Calendar")
                #name lable
                self.Namelabel = QtWidgets.QLabel(self.frame)
                self.Namelabel.setGeometry(QtCore.QRect(10, 270, 311, 61))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(14)
                self.Namelabel.setFont(font)
                self.Namelabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.Namelabel.setObjectName("Namelabel")
                #room type entry box
                self.roomtypebox = QtWidgets.QComboBox(self.frame)
                self.roomtypebox.setGeometry(QtCore.QRect(130, 370, 151, 41))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(12)
                self.roomtypebox.setFont(font)
                self.roomtypebox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.roomtypebox.setObjectName("roomtypebox")
                self.roomtypebox.addItem("Single")
                self.roomtypebox.addItem("Twin")
                self.roomtypebox.addItem("Couple")
                self.roomtypebox.addItem("Family")
                #room type label
                self.Roomtypelabel = QtWidgets.QLabel(self.frame)
                self.Roomtypelabel.setGeometry(QtCore.QRect(10, 360, 311, 61))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(14)
                self.Roomtypelabel.setFont(font)
                self.Roomtypelabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.Roomtypelabel.setObjectName("Roomtypelabel")
                #Name entry
                self.NameBox = QtWidgets.QTextEdit(self.frame)
                self.NameBox.setGeometry(QtCore.QRect(70, 280, 241, 41))
                self.NameBox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.NameBox.setObjectName("NameBox")
                #number-of-nights entry box
                self.nightsbox = QtWidgets.QSpinBox(self.frame)
                self.nightsbox.setGeometry(QtCore.QRect(230, 460, 61, 41))
                self.nightsbox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.nightsbox.setObjectName("nightsbox")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(10, 110, 251, 101))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.label.setObjectName("label")
                self.continuebutton = QtWidgets.QPushButton(self.frame)
                self.continuebutton.setGeometry(QtCore.QRect(250, 630, 341, 81))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(18)
                #continue-to-payment button
                self.continuebutton.setFont(font)
                self.continuebutton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.continuebutton.setObjectName("continuebutton")
                self.continuebutton.clicked.connect(self.usedata)
                #details (calendar's frame included)
                self.calendaframe = QtWidgets.QLabel(self.frame)
                self.calendaframe.setGeometry(QtCore.QRect(510, 130, 351, 321))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(14)
                self.calendaframe.setFont(font)
                self.calendaframe.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.calendaframe.setText("")
                self.calendaframe.setObjectName("calendaframe")
                #room type label
                self.AvailabilityLabel = QtWidgets.QLabel(self.frame)
                self.AvailabilityLabel.setGeometry(QtCore.QRect(280, 550, 281, 61))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(12)
                #no availability notice
                self.AvailabilityLabel.setFont(font)
                self.AvailabilityLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n""color: rgb(176, 0, 0);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
                self.AvailabilityLabel.setObjectName("AvailabilityLabel")
                self.AvailabilityLabel.hide()
                #widget levels
                self.textBrowser.raise_()
                self.nightslabel.raise_()
                self.Namelabel.raise_()
                self.Roomtypelabel.raise_()
                self.roomtypebox.raise_()
                self.NameBox.raise_()
                self.nightsbox.raise_()
                self.label.raise_()
                self.continuebutton.raise_()
                self.calendaframe.raise_()
                self.Calendar.raise_()
                self.AvailabilityLabel.raise_()
                NewBookingWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(NewBookingWindow)
                self.statusbar.setObjectName("statusbar")
                NewBookingWindow.setStatusBar(self.statusbar)
                self.retranslateUi(NewBookingWindow)
                QtCore.QMetaObject.connectSlotsByName(NewBookingWindow)
            #usage functions
            def usedata(self):
                room = self.roomtypebox.currentText()
                bookingname = self.NameBox.toPlainText()
                booklength = self.nightsbox.value()
                availability = backgroundbooking(room,bookingname,booklength)
                if availability == False:
                    self.AvailabilityLabel.show()
                    time.sleep(3)
                else:
                    print("Booking finalised")
                    Ui_NewBookingWindow.quit()
            def __exit__(self):
                exit(newbooking)
            def retranslateUi(self, NewBookingWindow):
                _translate = QtCore.QCoreApplication.translate
                NewBookingWindow.setWindowTitle(_translate("NewBookingWindow", "NewBookingWindow"))
                self.BackButton.setText(_translate("NewBookingWindow", "Back"))
                self.textBrowser.setHtml(_translate("NewBookingWindow","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:48pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Yu Gothic\'; font-size:36pt;\">New booking:</span></p></body></html>"))
                self.nightslabel.setText(_translate("NewBookingWindow", "Number of nights visiting:"))
                self.Namelabel.setText(_translate("NewBookingWindow", "Name:"))
                self.roomtypebox.setItemText(0, _translate("NewBookingWindow", "Single"))
                self.roomtypebox.setItemText(1, _translate("NewBookingWindow", "Twin"))
                self.roomtypebox.setItemText(2, _translate("NewBookingWindow", "Couple"))
                self.roomtypebox.setItemText(3, _translate("NewBookingWindow", "Family"))
                self.Roomtypelabel.setText(_translate("NewBookingWindow", "Room Type:"))
                self.label.setText(_translate("NewBookingWindow","<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">Please enter your preferences</span></p></body></html>"))
                self.continuebutton.setText(_translate("NewBookingWindow", "Continue to payment"))
                self.AvailabilityLabel.setText(_translate("NewBookingWindow", "No rooms available for selected room type"))
        #problem area!!
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            NewBookingWindow = QtWidgets.QMainWindow()
            ui = Ui_NewBookingWindow()
            ui.setupUi(NewBookingWindow)
            NewBookingWindow.show()
            sys.exit(app.exec_())