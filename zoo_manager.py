class Animal:

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        
    def speak(self):
        print(f" The {self.species} goes {self.sound}")

class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name, "Mammal", sound) # Initialize parent attributes
        
    def give_birth(self):
        print (f" The {self.species} has given birth!")

Whale1 = Mammal("Willy", "Squak Squak")
Whale1.speak()
Whale1.give_birth()

class Reptile(Animal):
    def __init__(self, name, sound):
        super().__init__(name, "Reptile", sound)
    
    def bask_in_sun(self):
        print("The Reptile is basking in the sun.")

Rep1 = Reptile("lizzie", "pss pss")
Rep1.bask_in_sun()

class Primate(Mammal):

    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.species = "Primate" 

    def climp_trees(self):
        print("The primate is climbing trees ehhh!")

PriOne = Primate("GloRilla", "Woo Oo Oo")
PriOne.climp_trees()

class Marsupial(Mammal):

    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.species = "Marsupial" 
    
    def carry_baby(self):
        print("The Marsupial is carrying a baby")

Mar1 = Marsupial("John", "Ooo Wha Ahh Ahh, Come on, come on, Get down with the Sickness, You musint you to get down with the sickness")
Mar1.carry_baby()
Mar1.speak()

class Bird(Animal):
    def __init__(self, name, sound, wingspan):
        super().__init__(name, "Bird", sound)
        self.wingspan = wingspan

class Aviary:

    def __init__(self):
        self.birds = []

    def add_bird(self, bird):
        self.birds.append(bird)
    
    def __str__(self):
       return f"Birdie {bird1} is in the {Aviary} room."

bird1 = Bird("Polly", "KaKaaa", 5.5)
Aviary1 = Aviary()
Aviary1.add_bird(bird1)
print(Aviary1)

