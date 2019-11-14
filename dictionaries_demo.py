
bars = {
    'Lloyds': 'Cheap bourbon',
    'Manuels': 'The Dogzilla',
    'The Imperial': 'Best staff ever'
}

favorite_bars = [
    'Lloyds',
    'Manuels',
    'The Imperial'
]

best_item_at_bars = [
    'Cheap bourbon',
    'The Dogzilla',
    'Best staff ever'
]

day_least_crowded = [
    'Tuesday',
    'Wednesday',
    'Whenever'
]
print(f"At {favorite_bars[0]}, they have a good {best_item_at_bars[0]} ")

print(bars.get("Lloyds"))

# How do I store multiple values for a single key?
bars = {
    'Lloyds': ['Cheap bourbon', 'Tuesday'],
    'Manuels': ['The Dogzilla', 'Wednesday']
}

# How do I store more complicated data for a single key?
bars = {
    'Lloyds': {
        'item':'Cheap bourbon', 
        'day': 'Tuesday'
    },
    'Manuels': {
        'item': 'The Dogzilla'
        'day': 'Wednesday'
    },
    'The Imperial': {
        'item': 'Philly'
        'day': ['Tuesday', 'Friday']
        #using a list because you don't need individual labels
    }
}

places = {
    'US': {
        'Georgia': {
            'Atlanta': {
                'work': 'DigitalCrafts'
            },
            'Savannah': {
                'coffee': 'That place that time'
            }
        },
        'Tennessee': {
            'Nashville': {
                'lunch': 'Hattie B'
            }
        }
    },
    'Europe': {
        'Germany': {
            'Berlin': {
                'lunch': 'The Reichstag'
            }
        }
    }
}
# How do I store new values to an existing dictionary?

##### How do I access information in useful dictionaries?
# How do I access nested information?

# How do I move through information in a nested dictionary?

# How do I access an item in a dictionary in a list?
movies = [
    {
        'title': 'Avengers: End Game',
        'release date': '2018'
    },
    {
        'title': 'Avengers: Infinity War',
        'release date': '2019'
    }
]

movies[1]['release date']

# How do I loop through list of dictionaries?
charges = [
    {
        'vendor': 'Kula',
        'amount': 3.49
    },
    {
        'vendor': 'Barnes and Noble',
        'amount': 16.21
    },
    {
        'vendor': 'Kula',
        'amount': 5.40
    }
]

total = 0
for charge in charges:
    total += charge['amount']

##### How do I modify a dictionary?

