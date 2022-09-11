import json
import os

def append_contact(contact_name, country_code, number, filename = "phone_book.json"):
    if os.path.exists(filename): 
        with open(filename, "r") as file: 
            data = file.read() 
            json_data = json.loads(data) 
            
        with open(filename, "w") as new_file: 
            entry = {"Name" : contact_name, "Country_code" : country_code, "Number": number}
            json_data["PhoneBook"].append(entry)
            json.dump(json_data, new_file, indent=3) 
    else:
        with open(filename, "w") as json_file:
            json_list = { "PhoneBook" : [] } 
            entry = {"Name" : contact_name, "Country_code" : country_code, "Number": number}
            json_list["PhoneBook"].append(entry)
            json.dump(json_list, json_file, indent=3) 

def find_contact_from_json(filename = "phone_book.json"):
    with open(filename, "r") as file:
        data = file.read() 
        data_json =json.loads(data)
        find = input("Enter a name to find: ") 

    for keyval in data_json["PhoneBook"]:
        if find.lower() == keyval["Name"].lower():
            print("Searched name: ", keyval["Name"])
            print("Country code: ", keyval["Country_code"])
            print("Phone number: ", keyval["Number"])
            successMsg = "Found in PhoneBook!"
            return successMsg
    unsuccessMsg = "Not found in PhoneBook!"
    return unsuccessMsg
            
def storing_finding_details(user):
    if user == "Yes":
        while True:
            contact_name = input("Enter a name: ")
            country_code = input("Enter a country code: ")
            number = input("Enter a phone number: ")
            append_contact(contact_name, country_code, number)
            print("Sucessfully saved in 'Phone_Book'!")
            print("Want to add another number?")

            again = input("Yes or No: ")   
            if again != "Yes":
                print("Okay, Thanks!")
                break
    elif user == "Find":
        print(find_contact_from_json())
    else:
        print("Wrong answer!, Answer should be either 'Yes' or 'Find'")

if __name__  == "__main__":
    print("Would you like to save a New number or Find a number from PhoneBook? \nTo save a new number, enter 'Yes'")
    print("To find a saved number, enter 'Find'?: ")
    user = input("Enter answer: ")  
    storing_finding_details(user)