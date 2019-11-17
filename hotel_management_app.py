hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}


# create a menu asking whether to check in or out
def menu():
    menu = """
    Hotel Management App
    ====================
    1. Checking In
    2. Checking Out

    """
    print(menu)
    user_choice = input("What would you like to do (1 or 2)? ")
    return user_choice

# prompt user for floor number, room number
def prompt_room_info():
    pass
# checking in - ask for num occupants and names
def check_in():
    user_floor = input("Floor number? ")
    user_room = input("Room number? ")
    user_name = input("Please enter name: ")

    for floor in hotel:
        if user_floor == floor:
            for room in hotel[floor]:
                if user_room == room:
                    print("Room is occupied.")
                    return
                else:
                    hotel[user_floor][user_room] = user_name
        else:
            hotel[user_floor][user_room] = user_name
    
   

# main
def main():
    user_choice = menu()
    if user_choice == "1":
        check_in()

main()
# for floor in hotel:
#     print(floor)
#     for room in hotel[floor]:
#         print(room)

# hotel['1']['250'] = 'dave'

print(hotel)