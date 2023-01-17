# imports
import json,time,random
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from globalfunctions import jsonrefill

class Ui_CancelBookingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("CancelBookingWindow")
        self.resize(938, 821)
        #detail
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.BackButton.clicked.connect(self.backfunc)
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
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 621, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(48)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(237, 237, 237);\n""background-color: qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(23, 25, 23, 158));")
        self.textBrowser.setObjectName("textBrowser")
        #room number label
        self.roomnumlabel = QtWidgets.QLabel(self.frame)
        self.roomnumlabel.setGeometry(QtCore.QRect(10, 320, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.roomnumlabel.setFont(font)
        self.roomnumlabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.roomnumlabel.setObjectName("roomnumlabel")
        #name label
        self.Namelabel = QtWidgets.QLabel(self.frame)
        self.Namelabel.setGeometry(QtCore.QRect(10, 240, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.Namelabel.setFont(font)
        self.Namelabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.Namelabel.setObjectName("Namelabel")
        #name entry
        self.nameentry = QtWidgets.QTextEdit(self.frame)
        self.nameentry.setGeometry(QtCore.QRect(190, 250, 241, 41))
        self.nameentry.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.nameentry.setObjectName("nameentry")
        #room number entry
        self.roomnumbox = QtWidgets.QSpinBox(self.frame)
        self.roomnumbox.setGeometry(QtCore.QRect(160, 330, 61, 41))
        self.roomnumbox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.roomnumbox.setObjectName("roomnumbox")
        #detail
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 120, 461, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.label.setObjectName("label")
        #confirm cancellation button
        self.confirmbutton = QtWidgets.QPushButton(self.frame)
        self.confirmbutton.setGeometry(QtCore.QRect(250, 630, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.confirmbutton.setFont(font)
        self.confirmbutton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.confirmbutton.setObjectName("confirmbutton")
        self.confirmbutton.clicked.connect(self.cancellation)
        #no matching bookings error label
        self.errorlabel = QtWidgets.QLabel(self.frame)
        self.errorlabel.setGeometry(QtCore.QRect(270, 550, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.errorlabel.setFont(font)
        self.errorlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n""color: rgb(176, 0, 0);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.errorlabel.setObjectName("errorlabel")
        self.errorlabel.hide()
        #cancellation success label
        self.successlabel = QtWidgets.QLabel(self.frame)
        self.successlabel.setGeometry(QtCore.QRect(230, 420, 391, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.successlabel.setFont(font)
        self.successlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n""color: rgb(176, 0, 0);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.successlabel.setObjectName("successlabel")
        self.successlabel.hide()
        #extras
        self.retranslateUi(self)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #usage functions
    def cancellation(self):
        currdate = datetime.today()
        currdate = currdate.strftime("%d-%m-%Y")
        roomnumtest = self.roomnumbox.value()
        nametest = self.nameentry.toPlainText()
        # record.json
        file = open("record.json", 'r')
        data = file.read()
        file.close()
        editlist = json.loads(data)
        # rooms.json
        file = open("rooms.json", 'r')
        data = file.read()
        file.close()
        roomslist = json.loads(data)
        # function main
        finallist = []
        numlist = []
        for i in range(len(editlist)):
            if editlist[i]['Roomnum'] == roomnumtest and editlist[i]['BookingName'] == nametest and editlist[i]['EndDate'] >= currdate:
                finallist.append(editlist[i])
                numlist.append(i)
        if not finallist:
            self.errorlabel.show()
            print("No matching bookings")
            time.sleep(2)
            self.errorlabel.hide()
        else:
            x = numlist[len(numlist) - 1]
            recentbooking = finallist[len(finallist) - 1]
            selectedroom = recentbooking['Roomnum']
            selectedroom -= 1
            editlist[x]['BookingName'] = str(recentbooking['BookingName']) + " - CANCELLED" + " - Validation:" + str(random.randint(1,10000000))# (random validation number prevents cancellation of a booking already cancelled)
            roomslist[selectedroom]['Status'] = "Available"
            roomslist[selectedroom]['Date'] = " "
            jsonrefill(roomslist)
            file = open("record.json", 'w')
            file.close()
            file = open("record.json", "w")
            file.write(json.dumps(editlist))
            file.close()
            print("Booking cancelled, room now vacant")
            self.successlabel.show()
            time.sleep(3)
            self.close()
    def backfunc(self):
        self.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("CancelBookingWindow", "CancelBookingWindow"))
        self.BackButton.setText(_translate("CancelBookingWindow", "Back"))
        self.textBrowser.setHtml(_translate("CancelBookingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:48pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cancel Booking:</p></body></html>"))
        self.roomnumlabel.setText(_translate("CancelBookingWindow", "Room number:"))
        self.Namelabel.setText(_translate("CancelBookingWindow", "Name under booking:"))
        self.label.setText(_translate("CancelBookingWindow", "<html><head/><body><p align=\"center\">Please enter the details of your existing booking below:</p></body></html>"))
        self.confirmbutton.setText(_translate("CancelBookingWindow", "Confirm cancellation"))
        self.errorlabel.setText(_translate("CancelBookingWindow", "<html><head/><body><p align=\"center\">No bookings found matching entered details</p></body></html>"))
        self.successlabel.setText(_translate("CancelBookingWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Booking cancelled successfully</span></p></body></html>"))
