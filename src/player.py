# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Items


class Player:
    def __init__(self, name, current_room):
        #super().__init__(room_name)
        self.current_room = current_room
        self.name = name
        self.inventory = []
       
    def __str__(self):
        return 'current_room: %s' % (self.current_room)

    def move_to_room(self, room):
        if room is None:
            print("You cannot move in that direction from your current room")
        else:
            self.current_room = room

    def add_item_player(self, item):
        return self.inventory.append(item)

    def drop_item_player(self, item):
        return self.inventory.remove(item)


    def print_items_player(self):
        for i in self.inventory:
            print("Player Items: ", i)





