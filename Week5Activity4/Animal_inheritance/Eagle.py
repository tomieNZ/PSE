from Animal import Bird
class Eagle(Bird):  # Eagle inherits from Bird
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Call parent class constructor