
phonebook = {}
# display a menu
def menu():
    menu = """

        Electronic Phone Book
        =====================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit

        """
    print(menu)
    user_input = input("What do you want to do (1-5)? ")
    return user_input
    
# look up entry and display name/number
def look_up_entry(name):
    entry_phone = phonebook[name]
    return entry_phone

# add new name and number
def set_entry(name, phone_number):
    phonebook[name] = phone_number
    return None

# delete an entry
def delete_entry(name):
    del phonebook[name]
    return None

# print all entries in phone book
def list_all_entries():
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")
    
def main():

    is_running = True
    while is_running:
        user_input = menu()
        # print(user_input)
        if user_input == "1":
            name_input = input("Enter name for lookup: ")
            if name_input in phonebook:
                lookup_result = look_up_entry(name_input)
                print(lookup_result)
            else:
                print("Name not in phonebook.")
        elif user_input == "2":
            entry_name = input("Enter name: ")
            entry_num2ber = input("Enter phonenumber: ")
            new_entry = set_entry(entry_name, entry_number)
            print(f"Entry stored for {entry_name}.")
        elif user_input == "3":
            entry_name = input("Enter name: ")
            delete_entry(entry_name)
            print(f"Entry deleted for {entry_name}.")
        elif user_input == "4":
            list_all_entries()
        elif user_input == "5":
            is_running = False
        else:
            print("Please enter a valid choice (1-5)")

main()
