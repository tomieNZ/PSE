"""
FACTORY DESIGN PATTERN

This module implements the Factory Pattern for creating Unit objects.

== Understanding ==
The Factory Pattern is a creational design pattern that provides an interface
for creating objects without specifying their exact classes. The Maker class
acts as a factory that produces different types of Unit objects (Helper, Friend)
based on a type parameter.

== Advantages ==
1. Decoupling: Client code doesn't need to know concrete class names
2. Centralized creation: All object creation logic is in one place
3. Easy to extend: Adding new unit types only requires modifying the factory
4. Single Responsibility: Separates object creation from object usage

== Disadvantages ==
1. Factory modification: Adding new types requires changing factory code
2. Complexity: For simple cases, factory may be overkill
3. Single point of failure: Factory errors affect all object creation
"""
from abc import ABC, abstractmethod


# ============================================================================
# ABSTRACT PRODUCT - Defines the interface for all products
# ============================================================================
class Unit(ABC):
    """Abstract base class that all concrete products must inherit from."""
    
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def action(self):
        """Abstract method - each unit type implements its own behavior."""
        pass


# ============================================================================
# CONCRETE PRODUCTS - Specific implementations of the Unit interface
# ============================================================================
class Helper(Unit):
    """Concrete Product: A unit that assists humans."""
    
    def action(self):
        print(f"{self.id} is assisting humans")


class Friend(Unit):
    """Concrete Product: A unit that provides companionship."""
    
    def action(self):
        print(f"{self.id} is keeping company")


# ============================================================================
# FACTORY CLASS - Creates products based on type parameter
# ============================================================================
class Maker:
    """
    Factory class that creates Unit objects.
    Client calls Maker.produce() instead of directly instantiating classes.
    """
    
    @staticmethod
    def produce(unit_type, id):
        """
        Factory method: Creates and returns appropriate Unit object.
        
        Args:
            unit_type: "helper" or "friend"
            id: Unique identifier for the unit
        Returns:
            Unit instance (Helper or Friend)
        """
        # Factory decides which concrete class to instantiate
        if unit_type == "helper":
            return Helper(id)
        elif unit_type == "friend":
            return Friend(id)
        else:
            raise ValueError("Unknown type")
