class Items:
    def __init__(self, item_name, desc):
        self.item_name = item_name
        self.desc = desc 

    def __str__(self):
        return f"{self.item_name}: ${self.desc}"

    def on_take(self, item_name):
        print(f"You have picked up {item_name}")
