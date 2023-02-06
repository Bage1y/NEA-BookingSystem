# imports
import json,time,sys,random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from globalfunctions import jsonrefill,recordjsonrefill
from database import Ui_RecordsWindow
from datetime import datetime
truepass = "ADMIN123"

class Ui_AdminWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("AdminWindow")
        self.resize(938, 821)
        #details
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
        #details
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
        #simple label
        self.functionlabel = QtWidgets.QLabel(self.frame)
        self.functionlabel.setGeometry(QtCore.QRect(10, 120, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.functionlabel.setFont(font)
        self.functionlabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.functionlabel.setObjectName("functionlabel")
        #reset all rooms button
        self.resetButton = QtWidgets.QPushButton(self.frame)
        self.resetButton.setGeometry(QtCore.QRect(90, 290, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetrooms)
        #booking records button
        self.recordsButton = QtWidgets.QPushButton(self.frame)
        self.recordsButton.setGeometry(QtCore.QRect(480, 290, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.recordsButton.setFont(font)
        self.recordsButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.recordsButton.setObjectName("recordsButton")
        self.recordsButton.clicked.connect(self.records)
        #close program button
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(280, 420, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.shutdown)
        #reset comfirmation label
        self.resetlabel = QtWidgets.QLabel(self.frame)
        self.resetlabel.setGeometry(QtCore.QRect(310, 550, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.resetlabel.setFont(font)
        self.resetlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n""color: rgb(217, 27, 27);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.resetlabel.setObjectName("resetlabel")
        self.resetlabel.hide()
        #close program confirmation label
        self.closelabel = QtWidgets.QLabel(self.frame)
        self.closelabel.setGeometry(QtCore.QRect(310, 550, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.closelabel.setFont(font)
        self.closelabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n""color: rgb(217, 27, 27);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
        self.closelabel.setObjectName("closelabel")
        self.closelabel.hide()
        #widget levels
        self.closelabel.raise_()
        self.resetlabel.raise_()
        self.retranslateUi(self)
        #QtCore.QMetaObject.connectSlotsByName(self)
    #usage functions
    def backfunc(self):
        self.close()
    def resetrooms(self):
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
        # record.json
        file = open("record.json", 'r')
        data = file.read()
        file.close()
        recordlist = json.loads(data)
        currdate = datetime.today()
        currdate = currdate.strftime("%d-%m-%Y")
        for i in range(len(recordlist)):
            if recordlist[i]['EndDate'] >= currdate and recordlist[i]['BookStatus'] == 'Ongoing':
                recordlist[i]['BookStatus'] = 'Admin Force Reset'
        recordjsonrefill(recordlist)
        print("All rooms reset")
        self.resetlabel.show()
        time.sleep(1.5)
        self.resetlabel.hide()
    def shutdown(self):
        self.closelabel.show()
        print("Program shutting down")
        countdown = 4
        for i in range(3):
            countdown -= 1
            print(countdown)
            time.sleep(0.5)
        sys.exit()
    def records(self):
        Ui_AdminWindow.hide(self)
        dlg = Ui_RecordsWindow()
        dlg.setWindowTitle("RecordsWindow")
        dlg.exec()
        Ui_AdminWindow.show(self)
    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "AdminWindow"))
        self.BackButton.setText(_translate("AdminWindow", "Back"))
        self.textBrowser.setHtml(_translate("AdminWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:48pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Admin:</p></body></html>"))
        self.functionlabel.setText(_translate("AdminWindow", "<html><head/><body><p align=\"justify\">Select a function below:</p></body></html>"))
        self.resetButton.setText(_translate("AdminWindow", "Reset all room booking status"))
        self.recordsButton.setText(_translate("AdminWindow", "Access booking records"))
        self.closeButton.setText(_translate("AdminWindow", "Close booking program"))
        self.resetlabel.setText(_translate("AdminWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">All booking status reset</span></p></body></html>"))
        self.closelabel.setText(_translate("AdminWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Closing Program</span></p></body></html>"))