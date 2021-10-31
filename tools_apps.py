from database import *
def MissingTools():
    for tool in tools:
        if tool['wanted'] == True:
            if tool['owned'] != True:
                id = (tool['id'])
                print(f'Te numery katalogowe trzeba dokupić: {id}' )
def MissingItems():
    for tool in tools:
        if tool['wanted'] == True:
            if tool['owned'] != True:
                id = (tool['id'])
                print(f'Te numery katalogowe trzeba dokupić: {id}' )
    for battery in batteries:
        if battery['wanted'] == True:
            if battery['owned'] != True:
                id = (battery['id'])
                print(f'Te numery katalogowe trzeba dokupić: {id}' )
    for charger in chargers:
        if charger['wanted'] == True:
            if charger['owned'] != True:
                id = (charger['id'])
                print(f'Te numery katalogowe trzeba dokupić: {id}' )


