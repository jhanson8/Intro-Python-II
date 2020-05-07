from room import Room
from player import Player 

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

while True:
    print(f"\nCurrent location: { new_player.current_room.name }")
    print(f"\nClue: { new_player.current_room.desc }")
    print("\nPlease enter a cardinal direction to move in: n, s, e, or w.\nn=North, s=South, e=East, w=West")
    input_direction = input().strip().lower().split(" ")
    input_length = len(input_direction)
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
        else:
            print("Please enter a valid command, press '?' for commands")


