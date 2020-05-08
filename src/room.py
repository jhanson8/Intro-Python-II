# Implement a class to hold room information. This should have name and
# description attributes.
from item import Items
from player import Player

class Room():
   def __init__(self, name, desc, n_to = None, s_to = None, w_to = None, e_to = None):
       self.name = name
       self.desc = desc
       self.n_to = n_to
       self.s_to = s_to
       self.w_to = w_to 
       self.e_to = e_to 
       #self.items = items
       self.items = []

   def add_item_room(self, item):
        return self.items.append(item)

   def drop_item_room(self, item):
        return self.items.remove(item)


   def print_items_room(self):
        for i in self.items:
            print("Room Items: ", i)

