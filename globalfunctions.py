#imports
import json

# re-json-dump
def jsonrefill(parameter):
    file = open("rooms.json", 'w')
    file.close()
    file = open("rooms.json", "w")
    file.write(json.dumps(parameter))
    file.close()