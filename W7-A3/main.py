"""
MAIN MODULE - Demonstrates Three Design Patterns Working Together

This module shows how Factory, Singleton, and Observer patterns integrate:

1. FACTORY PATTERN (Maker): Creates unit objects without exposing creation logic
2. SINGLETON PATTERN (Keeper): Ensures only one manager instance exists
3. OBSERVER PATTERN (Screen, Record): Multiple observers receive notifications

Pattern Interaction:
- Factory creates products (units)
- Singleton manages all products centrally
- Observers react to product actions
"""
from core import Keeper
from botfactory import Maker
from tracker import Screen, Record


# ============================================================================
# SINGLETON PATTERN IN ACTION
# ============================================================================
# Keeper() always returns the same instance (Singleton)
# Even if called multiple times, only one manager exists
manager = Keeper()


# ============================================================================
# OBSERVER PATTERN IN ACTION
# ============================================================================
# Create multiple observers - each will receive notifications
screen = Screen()  # Observer 1: displays to screen
record = Record()  # Observer 2: records to log


# ============================================================================
# FACTORY PATTERN IN ACTION
# ============================================================================
# Use factory to create units - client doesn't call Helper() or Friend() directly
unit1 = Maker.produce("helper", "AlphaBot")  # Factory creates Helper
unit2 = Maker.produce("friend", "BetaBot")   # Factory creates Friend

# Add units to the singleton manager
manager.add_unit(unit1)
manager.add_unit(unit2)


# ============================================================================
# ALL PATTERNS WORKING TOGETHER
# ============================================================================
for unit in manager.units:
    # Each unit performs its action (polymorphism from Factory pattern)
    unit.action()
    
    # Notify all observers about the action (Observer pattern)
    screen.notice(f"{unit.id} completed an action")
    record.notice(f"{unit.id} completed an action")
