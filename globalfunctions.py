#imports
import json

# re-json-dump
def jsonrefill(parameter):
    file = open("rooms.json", 'w')
    file.close()
    file = open("rooms.json", "w")
    file.write(json.dumps(parameter))
    file.close()

# linear search
def linearsearch(editlist, room, searchitem):
    finallist = []
    for i in range(len(editlist) - 1):
        if editlist[i]['Status'] == 'Available':
            if editlist[i][searchitem] == room:
                finallist.append(editlist[i])
    return finallist