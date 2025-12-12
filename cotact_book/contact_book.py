import os

FILENAME = "contacts.txt"

contacts = {}

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        for line in file:
            name, number = line.strip().split(",")
            contacts[name] = number

def save_contacts():
    with open(FILENAME, "w") as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")
            


while True:
    print("\n----Contact Book----\n")
    print("\n1. Add contact")
    print("\n2. Search contact")
    print("\n3. Delete contact")
    print("\n4. show all contact")
    print("\n5. Exit contact Book")
    
    choice=int(input("Enter your choice(1-5): "))
    
    if(choice==1):
        name=input("Enter name: ")
        number=input("Enter number: ")
        contacts[name]=number 
        print(f"{name}->saved successfully")
    elif(choice==2):
        name=input("Enter name: ")
        if name in contacts:
            print(f"{name}->{contacts[name]}")
        else:
            print("contact not found.")
    elif(choice==3):
        name=input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted successfully.")
        else:
            print("conatct not found.")
    elif(choice==4):
        if contacts:
            for name, number in contacts.items():
                print(f"{name:<15} {number}")
        else:
            print("No conatacts")
    elif(choice==5):
        print("Good Bye!!")
        break
    else:
        print("Not valid")