import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX01.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)

print(f"Total people in the Database: {len(people)}")

for person in people:
   termcolor.cprint("Name: ","green", end="")
   print(person['Firstname'], person['Lastname'])
   termcolor.cprint("Age: ","green", end="")
   print(person['age'])
   phoneNumbers = person['phoneNumber']
   termcolor.cprint("Phone numbers: ","green", end='')
   print(len(phoneNumbers))
   for i, number in enumerate(phoneNumbers):
       termcolor.cprint(" Phone {}:".format(i),"blue")
       termcolor.cprint("Type: ","red", end='')
       print(number['type'])
       termcolor.cprint("Number: ","red", end='')
       print(number['number'])
