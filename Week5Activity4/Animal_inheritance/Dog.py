from Animal import Mammal
class Dog(Mammal):  # Dog inherits from Mammal
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Call parent class constructor