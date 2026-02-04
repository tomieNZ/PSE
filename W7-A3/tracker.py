"""
OBSERVER DESIGN PATTERN

This module implements the Observer Pattern for notification handling.

== Understanding ==
The Observer Pattern defines a one-to-many dependency between objects.
When a subject's state changes, all its observers are notified automatically.
Here, Watcher is the observer interface, and Screen/Record are concrete
observers that react to notifications in their own way.

== Advantages ==
1. Loose coupling: Subject doesn't need to know observer details
2. Open/Closed: Can add new observers without modifying existing code
3. Broadcast communication: One event can notify multiple observers
4. Dynamic relationships: Observers can be added/removed at runtime

== Disadvantages ==
1. Unexpected updates: Observers may be notified in unpredictable order
2. Memory leaks: Forgotten observers may prevent garbage collection
3. Performance: Many observers can slow down notification process
4. Complexity: Can be hard to trace notification flow in large systems
"""


# ============================================================================
# OBSERVER INTERFACE - Defines the notification method
# ============================================================================
class Watcher:
    """
    Abstract Observer interface.
    All concrete observers must implement the notice() method.
    """
    
    def notice(self, msg):
        """Called when observer receives a notification."""
        pass


# ============================================================================
# CONCRETE OBSERVERS - Different ways to handle notifications
# ============================================================================
class Screen(Watcher):
    """
    Concrete Observer: Displays notifications on screen.
    Implements notice() to print messages to console.
    """
    
    def notice(self, msg):
        print(f"[Screen] {msg}")


class Record(Watcher):
    """
    Concrete Observer: Records notifications to log.
    In real application, this might write to a file or database.
    """
    
    def notice(self, msg):
        print(f"[Record] {msg}")
