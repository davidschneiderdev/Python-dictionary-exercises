

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

def countFriends(dictionary):
    num_friends = len(dictionary['friends'])
    # print(num_friends)
    new_dictionary = dictionary
    new_dictionary.update(friends_count = num_friends)
    return new_dictionary

print(countFriends(ramit))