# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        #super().__init__(room_name)
        self.current_room = current_room
        self.name = name
       
    def __str__(self):
        return 'current_room: %s' % (self.current_room)

    def move_to_room(self, room):
        if room is None:
            print("You cannot move in that direction from your current room")
        else:
            self.current_room = room





