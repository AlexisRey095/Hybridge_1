
#? exercise_1 Deli 

'''sandwich_orders = ['hawaiano', 'original', 'chees', 'vegetable']
finished_sandwiches = []

while sandwich_orders:
    made_sandwiches = sandwich_orders.pop()

    print (f'I made {made_sandwiches.title()} sandwich ')
    finished_sandwiches.append(made_sandwiches)

print('\n These sandwiches have been made: ')
for A in finished_sandwiches:
    print(f'{A.title()}')'''


#? exercise_2 No Pastrani 

'''sandwich_orders = ['hawaiano','pastrami', 'original', 'pastrami', 'chees', 'vegetable']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)'''

#? Exercise3 _ Dream Vacation

responses = {}

polling_active = True

while polling_active:
    city = input('Which city would you like to visit as a dream? ')
    country = input('Wich coutry belong your dream city? ')

    responses[country] = city

    repeat = input('Do you want add other response? (y/n)')
    repeat=repeat.lower()
    if repeat=='n':
        polling_active = False

for country,city in responses.items():
    print(f'The country is {country} and the city is {city}')