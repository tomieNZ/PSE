class Animal:
    def __init__(self, name):
        self.name = name  # Initialize animal name

    def walk(self):
        print(f"{self.name} is walking.")
    
    def fly(self):
        print(f"{self.name} is flying.")

    def swim(self):
        print(f"{self.name} is swimming.")


class Mammal(Animal):  # Mammal inherits from Animal
    def __init__(self, name, feature):
        super().__init__(name)  # Call parent class constructor
        self.feature = feature  # Set mammal-specific feature


class Bird(Animal):  # Bird inherits from Animal
    def __init__(self, name, feature):
        super().__init__(name)  # Call parent class constructor
        self.feature = feature  # Set bird-specific feature


class Fish(Animal):  # Fish inherits from Animal
    def __init__(self, name, feature):
        super().__init__(name)  # Call parent class constructor
        self.feature = feature  # Set fish-specific feature