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
    1. Check In
    2. Check Out

    """
    print(menu)
    user_choice = input("What would you like to do (1 or 2)? ")
    return user_choice

# prompt user for floor number, room number
def prompt_room_info():
    pass
# checking in - ask for num occupants and names
def check_occupied(user_floor, user_room):
    try:
      if hotel[user_floor][user_room] :
        return True
    except KeyError:
      return False

def check_in():
    user_floor = input("Floor number? ")
    user_room = input("Room number? ")
    user_name = input("Please enter name: ")

    if check_occupied(user_floor, user_room):
      print("Room currently occupied.")
    else:
      occupants_num = int(input("How many occupants? "))
      occupants_name = input("Please enter name(s) of occupants: ")
      hotel[user_floor][user_room] = occupants_name
      print(hotel)

def check_out():
    user_floor = input("Floor number? ")
    user_room = input("Room number? ")
    user_name = input("Please enter name: ")

    if check_occupied(user_floor, user_room):
      del hotel[user_floor][user_room]
      print(hotel)
    else:
      print("Room is not occupied. Cannot check out.")

# main
def main():
    user_choice = menu()
    if user_choice == "1":
      check_in()
    elif user_choice == '2':
      check_out()


main()
# for floor in hotel:
#     print(floor)
#     for room in hotel[floor]:
#         print(room)

# hotel['1']['250'] = 'dave'
