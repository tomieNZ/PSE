from Animal import Bird
class Penguin(Bird):  # Penguin inherits from Bird
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Call parent class constructor