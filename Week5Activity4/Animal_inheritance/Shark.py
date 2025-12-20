from Animal import Fish
class Shark(Fish):  # Shark inherits from Fish
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Call parent class constructor