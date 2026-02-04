"""
SINGLETON DESIGN PATTERN

This module implements the Singleton Pattern using Python metaclass.

== Understanding ==
The Singleton Pattern ensures a class has only one instance and provides a
global point of access to it. Here, KeeperMeta is a metaclass that intercepts
object creation. When Keeper() is called, it checks if an instance already
exists - if yes, returns the existing one; if no, creates a new one.

== Advantages ==
1. Single instance: Guarantees only one instance exists in the application
2. Global access: Provides a single point of access to shared resources
3. Lazy initialization: Instance is created only when first needed
4. Memory efficient: Avoids creating multiple instances of resource-heavy objects

== Disadvantages ==
1. Global state: Can introduce hidden dependencies between classes
2. Testing difficulty: Hard to mock or replace in unit tests
3. Violates Single Responsibility: Class manages its own lifecycle
4. Concurrency issues: May need extra care in multi-threaded environments
"""


# ============================================================================
# SINGLETON METACLASS - Controls instance creation
# ============================================================================
class KeeperMeta(type):
    """
    Metaclass that implements Singleton pattern.
    Intercepts __call__ to control object instantiation.
    """
    
    # Class-level dictionary to store single instances
    _holders = {}
    
    def __call__(cls, *args, **kwargs):
        """
        Called when Keeper() is invoked.
        Returns existing instance if available, otherwise creates new one.
        """
        # Check if instance already exists for this class
        if cls not in cls._holders:
            # First call: create new instance and store it
            instance = super().__call__(*args, **kwargs)
            cls._holders[cls] = instance
        # Return the single instance (new or existing)
        return cls._holders[cls]


# ============================================================================
# SINGLETON CLASS - Only one instance can exist
# ============================================================================
class Keeper(metaclass=KeeperMeta):
    """
    Singleton class that manages all units.
    No matter how many times Keeper() is called, same instance is returned.
    
    Example:
        k1 = Keeper()
        k2 = Keeper()
        k1 is k2  # True - same instance
    """
    
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        """Add a unit to the managed list."""
        self.units.append(unit)
