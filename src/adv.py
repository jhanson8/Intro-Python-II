from room import Room
from player import Player 
from item import Items
import sys 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#create items 
#outside
items = {
"oldMap" : Items("map", "This could lead you to the legendary treasure chamber"),
#foyer
"hatchet" : Items("hatchet", "A rusty old thing"),
"sword" : Items("sword", "Looks like it could cut through diamond"),
#overlook 
"compass" : Items("compass", "This will show you the way"),
"satchel" : Items("satchel", "Will make it easier for you to carry items"),
#narrow 
"torch" : Items("torch", "You can now see the cobwebs and skeletons of those who came before you..."),
"madallion" : Items("madallion", "a souvenir or a cursed object? "),
#treasure 
"crystal" : Items("crystal", "Est. Value: $100,000,000")
}


#add items to room 
room['outside'].items = [items["oldMap"]]

room['foyer'].items = [items["hatchet"], items['sword']]


room['overlook'].items = [items["compass"], items["satchel"]]

room['narrow'].items = [items["torch"], items["madallion"]]

room['treasure'].items = [items["crystal"]]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#new_player = Player("Jon", "outside").__str__()
#print(new_player)

name = ""
while name == "":
    name = input("\nEnter your name to begin your journey: ").strip()
    
new_player = Player(name, room['outside'])


print(f"Current location: { new_player.current_room.name }")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
room = new_player.current_room
while True:
    print(f"\nCurrent location: { new_player.current_room.name }")
    #room.print_items_room()
    print("\n")
    print("Current room items:")
    for i in new_player.current_room.items:
        print(i)
    
    print(f"\nClue: { new_player.current_room.desc }")
    print("\nPlease enter a cardinal direction to move in: n, s, e, or w.\nn=North, s=South, e=East, w=West")
    input_direction = input().lower().split(" ")
    input_length = len(input_direction)
    #print(input_direction)
    if input_length == 1:
        user_input = input_direction[0]
        
        if user_input == "n":
            new_player.move_to_room(new_player.current_room.n_to)
        elif user_input == "e":
            new_player.move_to_room(new_player.current_room.e_to)
        elif user_input == "s":
            new_player.move_to_room(new_player.current_room.s_to)
        elif user_input == "w":
            new_player.move_to_room(new_player.current_room.w_to)
        elif user_input == "q":
            break
        elif user_input == "i":
            print('FULL INVENTORY')
            for i in new_player.inventory:
                print(i.item_name)

        
    elif input_length == 2:
        action = input_direction[0]
        if action == "get" or action == "take":
            #add items to new_player inventory 
            new_player.add_item_player(items[input_direction[1]])
            new_player.current_room.drop_item_room(items[input_direction[1]])
            new = input_direction[1]
            print(f"You have picked up a {new}")
            print("Your items:")
            for i in new_player.inventory:
                print(i.item_name)
        
        
        elif action == "drop":
            #delete item from new_player inventory\
            new_player.drop_item_player(items[input_direction[1]])
            new_player.current_room.add_item_room(items[input_direction[1]])
            drop = input_direction[1]
            print(f"You have dropped a {drop}")
            print("Your items:")
            for i in new_player.inventory:
                print(i.item_name)


    else:
        print("Please enter a valid command, press '?' for commands")


