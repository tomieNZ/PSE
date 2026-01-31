"""
Factory Pattern - Client Code
Demonstrates how client uses factory without knowing concrete classes.
"""
from factory import NotificationFactory


def main():
    """
    Factory Pattern workflow:
    1. Get type from user input
    2. Factory creates appropriate object
    3. Use object via interface (polymorphism)
    """
    # Get user input
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    
    # Factory creates object - client doesn't know concrete class
    notification = NotificationFactory.create_notification(notification_type)
    
    # Use via interface - same code works for all types
    notification.send("Hello! This is a Factory Pattern example.")


if __name__ == "__main__":
    main()
