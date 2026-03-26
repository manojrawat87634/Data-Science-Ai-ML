import json
import os

def load_contact():
    if not os.path.exists('file.json'):
        return []
    
    with open('file.json', 'r') as file:
        return json.load(file)
def show_contacts():
    for i in load_contact():
        print(i)
def save_contact():
    contacts = load_contact()
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    contacts.append({"name": name, "email": email, "phone": phone})
    
    with open('file.json', 'w') as file:
        json.dump(contacts, file, indent=4)

#save_contact()
show_contacts()
