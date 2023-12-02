import os

adventurerName = input("What is your name? ").capitalize()
print(f"hello {adventurerName}")

rooms = {
    'Small room': {
        'name': 'Small room',
        'east': 'Hallway',
        'Item': ['Map'],
        'description':
        'gloomy looking place with chairs and on ground u see map'
    },
    'Hallway': {
        'name': 'Hallway',
        'north': 'Smithy',
        'south': 'Great hall',
        'Item': ['Lockpicking Tools']
    },
    'Smithy': {
        'name': 'Smithy',
        'south': 'Hallway',
        'Item': ['']
    },
    'Great Hall': {
        'name': 'Great Hall',
        'west': 'Treasury',
        'Item': ['']
    },
    'Treasury': {
        'name': 'Treasury',
        'sast': 'Great Hall',
        'Item': ['']
    }
}
directions = ['north', 'south', 'east', 'west']

current_room = rooms['Small room']

Item = ['Map', 'lockpicking Tools']

Inventory = {}

description = ['gloomy looking place with chairs and on ground u see map']

while True:
  #os.system("clear")
  print('-' * 30)
  print('Youy are in the {}'.format(current_room['name']))
  inventory_items = [', '.join(items) for items in Inventory.values()]
  print('Your current inventory: {}'.format(', '.join(inventory_items)))
  if current_room['Item']:
    print('Item in room:{}'.format(' '.join(current_room['Item'])))
    print('')

  command = input('Enter your move: \n').lower()
  if command == 'look around':
    print(''.join(description))
    if command in directions:
      if command in current_room:
        current_room = rooms[current_room[command]]
        if current_room['name'] == 'Observation Tower':
          print('''Congratulations! You have reached the 
              Observation Tower and defeated the Evil Wizard!''')
          break
      else:
        print('\nChoose another path.')
    elif command == 'get item':
      if current_room['Item']:  #!= 'none':
        Inventory['Item' + str(len(Inventory.keys()) + 1)] = current_room['Item']

        print("You aquired : ", ''.join(current_room['Item']))
        current_room['Item'] = 'none'
      else:
        print("No items to collect in this room")

    elif 'Map' in inventory_items:
      available_directions = [
        direction for direction in directions if direction in current_room
    ]
      print('Available Directions: {}'.format(', '.join(available_directions)))

    elif command == 'quit':
      print('Thanks for playing!')
      break

    else:
      print('Invalid input')
