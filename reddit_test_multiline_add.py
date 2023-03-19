import math

AREA_RATES = {
    "bedroom": 15,
    "bathroom": 20,
    "office space": 20,
    "utility room": 15,
    "kitchen": 25,
    "living / family room": 15,
    "dining area": 15,
}

print("To estimate hours needed please enter ")

total_minutes = 0
for area, rate in AREA_RATES.items():
    total_minutes += int(input(f"    Number of {area}s: ")) * rate

print(f"\nHours needed: {math.ceil(total_minutes / 60 * 4) / 4}")

Extracting a specific type from a list

 I have a list like this:  [{'Name':'Elsa', 'Characteristic': 'Pretty'}, {'Name':'Lisa', 'Characteristic':'Good-looking'}, .....\]  

&#x200B;

In this case, how should I code to create a new list by extracting only the {'name':'who'} information?

Python Assistance

Hi there! I need assistance with where I went wrong with creating a code. I am trying to generate a code that output states: My dog's name is: "Champ Johnson" \[\[WITH THE QUOTATION MARKS\]\]

The code that I created is: 

myDogsFirstName = "Champ"
myDogsLastName = "Johnson"
myDogsFullName = myDogsFirstName + " " + myDogsLastName 

print(f'''My Dog's name is "{myDogsFirstName} {myDogsLastName}".''')