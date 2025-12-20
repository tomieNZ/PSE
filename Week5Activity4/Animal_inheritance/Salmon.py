from Animal import Fish
class Salmon(Fish):  # Salmon inherits from Fish
    def __init__(self, name, feature):
        super().__init__(name, feature)  # Call parent class constructor