from random import randrange
items = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

for item in items:
    print(item)



for char in "Hello new world !!":
    print(char)

class Pet():
    boredom_decremaent = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10

    def __init__(self, name = "Kity", pet_type = "dog"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_decremaent)
        self.sounds = self.sounds[:]

    
    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1
    
    def funcname(self, parameter_list):
        raise NotImplementedError