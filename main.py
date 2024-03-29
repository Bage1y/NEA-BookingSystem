# imports
import json,random
from PyQt5 import QtCore, QtGui, QtWidgets
from NewBooks import Ui_NewBookingWindow
from datetime import datetime
from Admin import Ui_AdminWindow
from CancelBooks import Ui_CancelBookingWindow
from RenewBooks import Ui_RenewBookingWindow
from globalfunctions import jsonrefill,recordjsonrefill
truepass = "admin"

# room resetting
def roomreset():
    file = open("rooms.json", 'r')
    data = file.read()
    file.close()
    editlist = json.loads(data)
    for i in range(len(editlist)):
        selectedroom = editlist[i]
        if editlist[i]['Status'] == 'Unavailable':
            today = datetime.now()
            now = datetime.now()
            now = now.strftime("%H")
            now = int(now)
            # now+=1 #to change BST to GMT
            # record.json
            file = open("record.json", 'r')
            data = file.read()
            file.close()
            recordlist = json.loads(data)
            finallist = []
            for x in range(len(recordlist)):
                if recordlist[x]['Roomnum'] == selectedroom['Roomnum'] and recordlist[x]['EndDate'] == selectedroom['Date']:
                    finallist.append(recordlist[x])
            if not finallist:
                print("No rooms to reset")
            else:
                recordfinal = finallist[len(finallist)-1]
                if editlist[i]['Date'] <= today.strftime("%d-%m-%Y") and now >= 10:
                    editlist[selectedroom['Roomnum']-1]['Status'] = "Available"
                    editlist[selectedroom['Roomnum']-1]['Date'] = " "
                    recordlist[recordfinal['Roomnum']-1]['BookStatus'] = "Complete"
                    jsonrefill(editlist)
                    recordjsonrefill(recordlist)
    print("Required rooms reset")

while True:
    #GUI
    class Ui_MainMenuWindow(object):
        def setupUi(self, MainMenuWindow):
            MainMenuWindow.setObjectName("MainMenuWindow")
            MainMenuWindow.resize(936, 818)
            MainMenuWindow.setStyleSheet("background-color: rgb(26, 26, 26);\n""")
            self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.Frame1 = QtWidgets.QFrame(self.centralwidget)
            self.Frame1.setGeometry(QtCore.QRect(0, -10, 71, 841))
            self.Frame1.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
            self.Frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Frame1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Frame1.setObjectName("Frame1")

            #admin button
            self.AdminButton = QtWidgets.QPushButton(self.Frame1)
            self.AdminButton.setGeometry(QtCore.QRect(10, 20, 41, 41))
            self.AdminButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.864, y1:0.892045, x2:0.124591, y2:0.165, stop:0 rgba(0, 104, 113, 255), stop:1 rgba(7, 7, 9, 210));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;\n""")
            self.AdminButton.setObjectName("AdminButton")
            self.AdminButton.clicked.connect(self.admin)

            #general gui
            self.Frame1_2 = QtWidgets.QFrame(self.centralwidget)
            self.Frame1_2.setGeometry(QtCore.QRect(60, 0, 881, 71))
            self.Frame1_2.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
            self.Frame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Frame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Frame1_2.setObjectName("Frame1_2")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(50, 50, 891, 761))
            self.frame.setStyleSheet("border-width: 3px;\n""border-radius: 10px;\n""")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")

            #password entry
            self.passbox = QtWidgets.QLineEdit(self.Frame1_2)
            self.passbox.setGeometry(QtCore.QRect(5, 15, 241, 30))
            self.passbox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(36, 37, 37, 252, 158));\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
            self.passbox.setObjectName("passbox")
            self.passbox.setEchoMode(QtWidgets.QLineEdit.Password)

            #cancel booking button
            self.CancelBookingButton = QtWidgets.QPushButton(self.frame)
            self.CancelBookingButton.setGeometry(QtCore.QRect(70, 280, 231, 131))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(17)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setKerning(True)
            self.CancelBookingButton.setFont(font)
            self.CancelBookingButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;\n""")
            self.CancelBookingButton.setObjectName("CancelBookingButton")
            self.CancelBookingButton.clicked.connect(self.cancelbook)

            #renew booking button
            self.RenewBookingButton = QtWidgets.QPushButton(self.frame)
            self.RenewBookingButton.setGeometry(QtCore.QRect(570, 280, 231, 131))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(17)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setKerning(True)
            self.RenewBookingButton.setFont(font)
            self.RenewBookingButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;\n""")
            self.RenewBookingButton.setObjectName("RenewBookingButton")
            self.RenewBookingButton.clicked.connect(self.renewbook)

            #extra details
            self.textBrowser = QtWidgets.QTextBrowser(self.frame)
            self.textBrowser.setGeometry(QtCore.QRect(10, 10, 331, 101))
            font = QtGui.QFont()
            font.setFamily("Yu Gothic")
            font.setPointSize(48)
            self.textBrowser.setFont(font)
            self.textBrowser.setStyleSheet("color: rgb(237, 237, 237);\n""background-color: qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(23, 25, 23, 158));")
            self.textBrowser.setObjectName("textBrowser")

            # new booking button
            self.NewBookingButton = QtWidgets.QPushButton(self.frame)
            self.NewBookingButton.setGeometry(QtCore.QRect(320, 280, 231, 131))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(17)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setKerning(True)
            self.NewBookingButton.setFont(font)
            self.NewBookingButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;\n""")
            self.NewBookingButton.setObjectName("NewBookingButton")
            self.NewBookingButton.clicked.connect(self.newbook)

            #additional main menu
            MainMenuWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainMenuWindow)
            self.statusbar.setObjectName("statusbar")
            MainMenuWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainMenuWindow)
            QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

        def admin(self):
            entered = self.passbox.text()
            self.passbox.clear()
            if entered == truepass:
                MainMenuWindow.hide()
                print("Password Accepted")
                dlg = Ui_AdminWindow()
                dlg.setWindowTitle("AdminWindow")
                dlg.exec()
                MainMenuWindow.show()
            else:
                print("Failed")
        def newbook(self):
            MainMenuWindow.hide()
            dlg = Ui_NewBookingWindow()
            dlg.setWindowTitle("NewBooksWindow")
            dlg.exec()
            MainMenuWindow.show()
        def cancelbook(self):
            MainMenuWindow.hide()
            dlg = Ui_CancelBookingWindow()
            dlg.setWindowTitle("CancelBooksWindow")
            dlg.exec()
            MainMenuWindow.show()
        def renewbook(self):
            MainMenuWindow.hide()
            dlg = Ui_RenewBookingWindow()
            dlg.setWindowTitle("RenewBookingWindow")
            dlg.exec()
            MainMenuWindow.show()

        def retranslateUi(self, MainMenuWindow):
            _translate = QtCore.QCoreApplication.translate
            MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "MainMenuWindow"))
            self.AdminButton.setText(_translate("MainMenuWindow", "Admin"))
            self.CancelBookingButton.setText(_translate("MainMenuWindow", "Cancel booking"))
            self.RenewBookingButton.setText(_translate("MainMenuWindow", "Renew booking"))
            self.textBrowser.setHtml(_translate("MainMenuWindow","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'Yu Gothic\'; font-size:48pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI Light\';\">Welcome</span></p></body></html>"))
            self.NewBookingButton.setText(_translate("MainMenuWindow", "Make a new booking"))


    if __name__ == "__main__":
        roomreset()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainMenuWindow = QtWidgets.QMainWindow()
        ui = Ui_MainMenuWindow()
        ui.setupUi(MainMenuWindow)
        MainMenuWindow.show()
        sys.exit(app.exec_())