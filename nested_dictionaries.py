
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

ramit_email = ramit['email']
print(ramit_email)

first_interest = ramit["interests"][0]
print(first_interest)

jasmine_email = ramit['friends'][0]['email']
print(jasmine_email)

jan_second_interest = ramit['friends'][1]['interests'][1]
print(jan_second_interest)






