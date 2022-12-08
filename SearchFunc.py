import json

# linear search
def linearsearch(editlist, room, searchitem):
    finallist = []
    for i in range(len(editlist) - 1):
        if editlist[i]['Status'] == 'Available':
            if editlist[i][searchitem] == room:
                finallist.append(editlist[i])
    return finallist


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