import pandas as pd
import json,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QItemDelegate, QTableWidgetItem,QTableWidget,QTableView
from PyQt5.QtCore import QAbstractTableModel,Qt

def editdatabase(roomnumber,bookingname,startdate,enddate):
	file = open("record.json","r")
	data = file.read()
	editlist = json.loads(data)
	file.close()
	bookingnum = len(editlist)+1
	toAppend = {"BookingNumber":bookingnum, "Roomnum":roomnumber, "BookingName":bookingname, "StartDate":startdate, "EndDate":enddate}
	file = open("record.json",'r')
	data = file.read()
	file.close()
	editlist = json.loads(data)
	editlist.append(toAppend)
	data = json.dumps(editlist)
	file = open("record.json","w")
	file.write(data)
	file.close()
	#dataframe = pd.DataFrame(editlist)
	#print(dataframe.head())

#recordsmenu
#def recordsmenu():
#	file = open("record.json","r")
#	data = file.read()
#	editlist = json.loads(data)
#	file.close()
#	while True:
#		menuchoice = int(input("1. View all records\n2. Make a record query\n3. Back\nEnter your choice: "))
#		if menuchoice == 1:
#			dataframe = pd.DataFrame(editlist)
#			print(dataframe.head(),"\n")
#		elif menuchoice == 2:
#			choice = int(input("1. Booking Number\n2. Room Number\n3. Booking Name\n4. Start Date\n5. End Date\nEnter the variable you would like to query: "))
#			dataframe = pd.DataFrame(editlist)
#			if choice == 1:
#				queryvar = int(input("Enter the booking number to query: "))
#				loadrecords = dataframe.query("BookingNumber == @queryvar")
#			elif choice == 2:
#				queryvar = int(input("Enter the room number to query: "))
#				loadrecords = dataframe.query("Roomnum == @queryvar")
#			elif choice == 3:
#				queryvar = input("Enter the room number to query: ")
#				loadrecords = dataframe.query("BookingName == @queryvar")
#			elif choice == 4:
#				queryvar = input("Enter the start date to query (dd/mm/yy): ")
#				loadrecords = dataframe.query("StartDate == @queryvar")
#			elif choice == 5:
#				queryvar = input("Enter the end date to query (dd/mm/yy): ")
#				loadrecords = dataframe.query("EndDate == @queryvar")
#			if dataframe.empty():
#				print("No records found matching preferences")
#				time.sleep(1)
#			else:
#				print(loadrecords,"\n")
#		else:
#			return None

#TABLE
class PandasModel(QtCore.QAbstractTableModel):
	def __init__(self,data):
		QAbstractTableModel.__init__(self)
		self._data = data
	def rowCount(self,parent=None):
		return self._data.shape[0]
	def columnCount(self,parent=None):
		return self._data.shape[1]
	def data(self,index,role=Qt.DisplayRole):
		if index.isValid():
			if role == Qt.DisplayRole:
				return str(self._data.iloc[index.row(),index.column()])
	def headerData(self,col,orientation,role):
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return self._data.columns[col]
		return None

class Ui_RecordsWindow(QDialog):
	file = open("record.json", "r")
	data = file.read()
	editlist = json.loads(data)
	file.close()
	df = pd.DataFrame(editlist)
	def __init__(self):
		super().__init__()
		self.setObjectName("RecordsWindow")
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
		#booking num label
		self.Booknumlabel = QtWidgets.QLabel(self.frame)
		self.Booknumlabel.setGeometry(QtCore.QRect(650, 450, 221, 61))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.Booknumlabel.setFont(font)
		self.Booknumlabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(48, 48, 48, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.Booknumlabel.setObjectName("Booknumlabel")
		#name box
		self.namebox = QtWidgets.QTextEdit(self.frame)
		self.namebox.setGeometry(QtCore.QRect(660, 390, 201, 41))
		self.namebox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.namebox.setObjectName("namebox")
		#details
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(650, 320, 181, 51))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.label.setFont(font)
		self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.label.setObjectName("label")
		#update tables button
		self.continuebutton = QtWidgets.QPushButton(self.frame)
		self.continuebutton.setGeometry(QtCore.QRect(600, 210, 261, 81))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(18)
		self.continuebutton.setFont(font)
		self.continuebutton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.continuebutton.setObjectName("continuebutton")
		self.continuebutton.clicked.connect(self.showtable)
		#booking num box
		self.booknumbox = QtWidgets.QSpinBox(self.frame)
		self.booknumbox.setGeometry(QtCore.QRect(800, 460, 61, 41))
		self.booknumbox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.booknumbox.setObjectName("booknumbox")
		#room number label
		self.roomnumlabel = QtWidgets.QLabel(self.frame)
		self.roomnumlabel.setGeometry(QtCore.QRect(650, 520, 221, 61))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.roomnumlabel.setFont(font)
		self.roomnumlabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(48, 48, 48, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.roomnumlabel.setObjectName("roomnumlabel")
		#room number entry
		self.roomnumbox = QtWidgets.QSpinBox(self.frame)
		self.roomnumbox.setGeometry(QtCore.QRect(790, 530, 61, 41))
		self.roomnumbox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.roomnumbox.setObjectName("roomnumbox")
		#start date label
		self.startdatelabel = QtWidgets.QLabel(self.frame)
		self.startdatelabel.setGeometry(QtCore.QRect(650, 590, 221, 61))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.startdatelabel.setFont(font)
		self.startdatelabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(48, 48, 48, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.startdatelabel.setObjectName("startdatelabel")
		#end date label
		self.enddatelabel = QtWidgets.QLabel(self.frame)
		self.enddatelabel.setGeometry(QtCore.QRect(650, 660, 221, 61))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.enddatelabel.setFont(font)
		self.enddatelabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(48, 48, 48, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.enddatelabel.setObjectName("enddatelabel")
		#booking name label
		self.booknamelabel = QtWidgets.QLabel(self.frame)
		self.booknamelabel.setGeometry(QtCore.QRect(590, 380, 281, 61))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.booknamelabel.setFont(font)
		self.booknamelabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.12, y1:0.489, x2:1, y2:0.517, stop:0.210227 rgba(0, 104, 113, 194), stop:1 rgba(48, 48, 48, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.booknamelabel.setObjectName("booknamelabel")
		#details
		self.detaillabel = QtWidgets.QLabel(self.frame)
		self.detaillabel.setGeometry(QtCore.QRect(580, 310, 301, 421))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.detaillabel.setFont(font)
		self.detaillabel.setStyleSheet("background-color: rgb(48, 48, 48, 150);\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.detaillabel.setText("")
		self.detaillabel.setObjectName("detaillabel")
		#start date entry
		self.startdatebox = QtWidgets.QDateEdit(self.frame)
		self.startdatebox.setGeometry(QtCore.QRect(750, 600, 110, 41))
		self.startdatebox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.startdatebox.setObjectName("startdatebox")
		#end date entry
		self.enddatebox = QtWidgets.QDateEdit(self.frame)
		self.enddatebox.setGeometry(QtCore.QRect(750, 670, 110, 41))
		self.enddatebox.setStyleSheet("background-color: rgb(36, 37, 37, 252);\n""selection-color: rgb(4, 138, 140);\n""selection-background-color: rgb(181, 181, 181);\n""alternate-background-color: qlineargradient(spread:pad, x1:0.949, y1:0.102273, x2:0.42, y2:0.391636, stop:0 rgba(16, 137, 135, 255), stop:1 rgba(36, 37, 37, 252));\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.enddatebox.setObjectName("enddatebox")
		#detail
		self.tablelable = QtWidgets.QLabel(self.frame)
		self.tablelable.setGeometry(QtCore.QRect(20, 130, 541, 591))
		font = QtGui.QFont()
		font.setFamily("Segoe UI Light")
		font.setPointSize(14)
		self.tablelable.setFont(font)
		self.tablelable.setStyleSheet("background-color: rgb(48, 48, 48, 150);\n""color: rgb(215, 219, 218);\n""border-width: 3px;\n""border-color: rgb(61, 61, 61);\n""border-radius: 10px;")
		self.tablelable.setText("")
		self.tablelable.setObjectName("tablelable")
		#dataframe table display - PROBLEM AREA!!
		self.datatable = QtWidgets.QTableView(self.tablelable)
		self.datatable.setGeometry(QtCore.QRect(10, 12, 520, 570))
		self.datatable.setSortingEnabled(True)
		self.datatable.setObjectName("datatable")
		#widget levels
		self.textBrowser.raise_()
		self.continuebutton.raise_()
		self.detaillabel.raise_()
		self.enddatelabel.raise_()
		self.booknamelabel.raise_()
		self.namebox.raise_()
		self.Booknumlabel.raise_()
		self.booknumbox.raise_()
		self.roomnumlabel.raise_()
		self.roomnumbox.raise_()
		self.startdatelabel.raise_()
		self.startdatebox.raise_()
		self.enddatebox.raise_()
		self.label.raise_()
		self.tablelable.raise_()
		self.datatable.raise_()
		self.retranslateUi(self)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
	#usage functions
	def backfunc(self):
		self.close()
	def showtable(self):
		file = open("record.json", "r")
		data = file.read()
		editlist = json.loads(data)
		file.close()
		df = pd.DataFrame(editlist)
		#df = pd.read_json('record.json')
		print(df)
		model = PandasModel(df)
		self.datatable.setModel(model)
	def retranslateUi(self, RecordsWindow):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("RecordsWindow", "RecordsWindow"))
		self.BackButton.setText(_translate("RecordsWindow", "Back"))
		self.textBrowser.setHtml(_translate("RecordsWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:48pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Booking Records:</p></body></html>"))
		self.Booknumlabel.setText(_translate("RecordsWindow", "Booking Number:"))
		self.label.setText(_translate("RecordsWindow", "<html><head/><body><p align=\"justify\">Search by:</p></body></html>"))
		self.continuebutton.setText(_translate("RecordsWindow", "Update table"))
		self.roomnumlabel.setText(_translate("RecordsWindow", "Room Number:"))
		self.startdatelabel.setText(_translate("RecordsWindow", "Start Date:"))
		self.enddatelabel.setText(_translate("RecordsWindow", "End Date:"))
		self.booknamelabel.setText(_translate("RecordsWindow", "Name:"))