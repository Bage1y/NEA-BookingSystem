import pandas as pd
import json
import time

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
def recordsmenu():
	file = open("record.json","r")
	data = file.read()
	editlist = json.loads(data)
	file.close()
	while True:
		menuchoice = int(input("1. View all records\n2. Make a record query\n3. Back\nEnter your choice: "))
		if menuchoice == 1:
			dataframe = pd.DataFrame(editlist)
			print(dataframe.head(),"\n")
		elif menuchoice == 2:
			choice = int(input("1. Booking Number\n2. Room Number\n3. Booking Name\n4. Start Date\n5. End Date\nEnter the variable you would like to query: "))
			dataframe = pd.DataFrame(editlist)
			if choice == 1:
				queryvar = int(input("Enter the booking number to query: "))
				loadrecords = dataframe.query("BookingNumber == @queryvar")
			elif choice == 2:
				queryvar = int(input("Enter the room number to query: "))
				loadrecords = dataframe.query("Roomnum == @queryvar")
			elif choice == 3:
				queryvar = input("Enter the room number to query: ")
				loadrecords = dataframe.query("BookingName == @queryvar")
			elif choice == 4:
				queryvar = input("Enter the start date to query (dd/mm/yy): ")
				loadrecords = dataframe.query("StartDate == @queryvar")
			elif choice == 5:
				queryvar = input("Enter the end date to query (dd/mm/yy): ")
				loadrecords = dataframe.query("EndDate == @queryvar")
			if dataframe.empty():
				print("No records found matching preferences")
				time.sleep(1)
			else:
				print(loadrecords,"\n")
		else:
			return None
