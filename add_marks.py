import json

print("System: Only making this to add 1 subject at a time.")
subject = input("Name of the subject: ")
if input("Is the name correct? y/n: ").lower() != 'y':
    print("System: 'Yes' not detected exiting!")
    exit(0)
else:
    subject = subject.lower()

sem = input("What semester is this: ")
file = f"sem{sem}.json"

try:
    with open(file, 'r') as fp:
        data = json.load(fp)
except FileNotFoundError:
    data = {}
    print("System: Making a new file for this semester.")
except json.JSONDecodeError:
    data = {}
    print("System: Somehow you fucked up the data so start again lmao.")

if subject in data.keys():
    print("System: This subject is already there:")
    print(f"Marks: {data[subject]["marks"]}\nCredits: {
          data[subject]["credits"]}")
    choice = input(
        "Do you want to update or delete it? d:delete, u:update, e:exit ").lower()
    if choice == 'd':
        del data[subject]
        exit(0)
    elif choice == 'e':
        exit(0)
    else:
        print("Updating even if you did not want to :)")

else:
    data[subject] = {}

data[subject]["marks"] = float(input("How many marks out (/10): "))
data[subject]["credits"] = float(input("How many credits: "))

print(data)

with open(file, 'w') as fp:
    json.dump(data, fp, indent=1)
