"""
Room service: 
Console chatbot to order room service food from a menu.
enkhriilen and dari 
"""

guests = {'201':'Jay', '202':'Yeonjun','203':'Jimin'}

#Dictionaries with the menu
starters = {'301':"tteokbokki", '302':'Gimbap', '303':'Kimchi'}
maincourses = {'401':'Bibimbap','402':"Kimchi Stew", '403':'Army Stew'}
desserts = {'501':'Songpyeon', '502':'Dasik', '503': 'Sikhye'} 
#Guest name and room
name = None
room = None

#Dictionary with the customer's order
order = {}

#check if the room has been booked
while room not in guests.keys():
    room = input('Please, enter your room number: ')
    #check if room exists
    if room in guests.keys():
        name = input('Please, enter your name: ')
        #Check if the room and guest name match
        if guests[room] != name:
            print ('Your name does not match our records.')
            room = None
    else:
        print (f'Room {room} has not been booked.')


def select_food (food_type, food_dict):
    #Print food
    print ()
    print (f'{food_type} menu')
    print ('------------------------------------')
    for code, food in food_dict.items():
        print (code, '->', food)

    #Add a blank line
    print()

    #Select food
    food_code = None
    #validate the food
    while food_code not in food_dict.keys():
        food_code = input ('Please, enter the starter code: ')
        if food_code not in food_dict:
            print('Wrong starter code.')
        else:
            return {food_code: food_dict[food_code]}
#Print the order:
print ()
print ('Your order')
print ('----------')
for code, food in order.items():
    print (code, '->', food)

print('Delivery time:', delivery_time)

#Confirm the order
place_order = ''

while place_order.lower() not in ('yes', 'no'):
    place_order = input ('Would you like to place your order (yes/no)? ')

print ()
if place_order == 'yes':
    print ('Your order is being processed')
else:
    print ('Your order has been cancelled')

print ('Thank you for choosing us!')