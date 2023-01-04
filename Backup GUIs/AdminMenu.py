from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame1 = QtWidgets.QFrame(self.centralwidget)
        self.Frame1.setGeometry(QtCore.QRect(0, 0, 71, 841))
        self.Frame1.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
        self.Frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame1.setObjectName("Frame1")
        self.BackButton = QtWidgets.QPushButton(self.Frame1)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.BackButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.864, y1:0.892045, x2:0.124591, y2:0.165, stop:0 rgba(0, 104, 113, 255), stop:1 rgba(7, 7, 9, 210));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 10px;\n"
"border-color: rgb(135, 135, 135);\n"
"border-radius: 10px;\n"
"")
        self.BackButton.setObjectName("BackButton")
        self.Frame1_2 = QtWidgets.QFrame(self.centralwidget)
        self.Frame1_2.setGeometry(QtCore.QRect(70, 0, 871, 71))
        self.Frame1_2.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
        self.Frame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame1_2.setObjectName("Frame1_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 60, 891, 761))
        self.frame.setStyleSheet("border-width: 3px;\n"
"background-color: rgb(26, 26, 26);\n"
"border-radius: 10px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 621, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(48)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(237, 237, 237);\n"
"background-color: qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(23, 25, 23, 158));")
        self.textBrowser.setObjectName("textBrowser")
        self.functionlabel = QtWidgets.QLabel(self.frame)
        self.functionlabel.setGeometry(QtCore.QRect(10, 120, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.functionlabel.setFont(font)
        self.functionlabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.functionlabel.setObjectName("functionlabel")
        self.resetButton = QtWidgets.QPushButton(self.frame)
        self.resetButton.setGeometry(QtCore.QRect(90, 290, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.resetButton.setObjectName("resetButton")
        self.recordsButton = QtWidgets.QPushButton(self.frame)
        self.recordsButton.setGeometry(QtCore.QRect(480, 290, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.recordsButton.setFont(font)
        self.recordsButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.recordsButton.setObjectName("recordsButton")
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(280, 420, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.closeButton.setObjectName("closeButton")
        self.resetlabel = QtWidgets.QLabel(self.frame)
        self.resetlabel.setGeometry(QtCore.QRect(310, 550, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.resetlabel.setFont(font)
        self.resetlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n"
"color: rgb(217, 27, 27);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.resetlabel.setObjectName("resetlabel")
        self.closelabel = QtWidgets.QLabel(self.frame)
        self.closelabel.setGeometry(QtCore.QRect(310, 550, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.closelabel.setFont(font)
        self.closelabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.501, y1:0.897727, x2:0.528, y2:0, stop:0 rgba(140, 171, 174, 255), stop:1 rgba(225, 225, 219, 255));\n"
"color: rgb(217, 27, 27);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;")
        self.closelabel.setObjectName("closelabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Admin:</p></body></html>"))
        self.functionlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Select a function below:</p></body></html>"))
        self.resetButton.setText(_translate("MainWindow", "Reset all room booking status"))
        self.recordsButton.setText(_translate("MainWindow", "Access booking records"))
        self.closeButton.setText(_translate("MainWindow", "Close booking program"))
        self.resetlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">All booking status reset</span></p></body></html>"))
        self.closelabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Closing Program</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
