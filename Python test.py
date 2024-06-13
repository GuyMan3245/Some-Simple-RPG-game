rooms = {  
    'Grassy opening' : {'name': 'Grassy opening',
               'north': 'wolf_encounter', 
               'east': 'Heavy fog', 
               'south': 'Empty village', 
               'west': 'test4'},
    'Empty village' : {'name' : 'Empty village',
                      'Open door': 'Ghoul'}
}
death_rooms = {
    'wolf_encounter': {'name': 'wolf_encounter',
               'south': 'Grassy opening'},
    'Heavy fog': {'name': 'Heavy fog',
               'south': 'Grassy opening'}
}
inside = {'Grassy opening': "The feel of soft grass surrounds you. You don't know where you are.\n North, South, East or West?",
   'wolf_encounter': "You come face to face with a menacing wolf! It lunges at you, and you are torn to shreds.\n\n YOU DIE.",
   'Heavy fog': "You enter the heavy fog. It feels like your lungs are on fire. You can't breathe.\n\n YOU DIE.",
   'Empty village' : "You enter the village. It is empty. You look around, and see a door.\n Door or North?"
         }

current_loc = rooms['Grassy opening']
direction = ['north', 'east', 'south', 'west']
while True:
  print("You are in a " + current_loc['name'])
  print(inside[current_loc['name']])
  
  direction = input("> ").lower()
  if direction in current_loc:
    next_room = current_loc[direction]
    if next_room in death_rooms:
      print(inside[next_room])
      break
    else:
      current_loc = rooms[next_room]
      print("You can go: ")
      for i in current_loc:
        if i in direction:
          print(i)
  else:
    print("You walk into a tree, Ouch!")