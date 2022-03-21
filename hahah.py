starters = {'101': 'Tuna Salad', '102': 'Ceaser Salad', '103': 'French Fries' }

print('Starters munu')
print('-------------')
for code, food in starters:
    print(code, '->', food)

user_choice = input ("Select an item from the menu")

match user_choice:
 case '101'| '102':
     print('Healthy choice!')
 case '103' : 
     print("You have selected", starters[user_choice])
     print("Confort food!")
 case _: 
     print("Wrong starter code")

