from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 818)
        MainWindow.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame1 = QtWidgets.QFrame(self.centralwidget)
        self.Frame1.setGeometry(QtCore.QRect(0, -10, 71, 841))
        self.Frame1.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
        self.Frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame1.setObjectName("Frame1")
        self.pushButton = QtWidgets.QPushButton(self.Frame1)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.864, y1:0.892045, x2:0.124591, y2:0.165, stop:0 rgba(0, 104, 113, 255), stop:1 rgba(7, 7, 9, 210));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.Frame1_2 = QtWidgets.QFrame(self.centralwidget)
        self.Frame1_2.setGeometry(QtCore.QRect(60, 0, 881, 71))
        self.Frame1_2.setStyleSheet("background-color: rgb(36, 37, 37, 252);")
        self.Frame1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame1_2.setObjectName("Frame1_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 891, 761))
        self.frame.setStyleSheet("border-width: 3px;\n"
"border-radius: 10px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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
        self.CancelBookingButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"")
        self.CancelBookingButton.setObjectName("CancelBookingButton")
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
        self.RenewBookingButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"")
        self.RenewBookingButton.setObjectName("RenewBookingButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 331, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(48)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(237, 237, 237);\n"
"background-color: qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(23, 25, 23, 158));")
        self.textBrowser.setObjectName("textBrowser")
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
        self.NewBookingButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n"
"color: rgb(215, 219, 218);\n"
"border-width: 3px;\n"
"border-color: rgb(61, 61, 61);\n"
"border-radius: 10px;\n"
"")
        self.NewBookingButton.setObjectName("NewBookingButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Admin"))
        self.CancelBookingButton.setText(_translate("MainWindow", "Cancel booking"))
        self.RenewBookingButton.setText(_translate("MainWindow", "Renew booking"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI Light\';\">Welcome</span></p></body></html>"))
        self.NewBookingButton.setText(_translate("MainWindow", "Make a new booking"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
