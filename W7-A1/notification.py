"""
Factory Pattern - Product Classes
Defines abstract interface and concrete notification implementations.
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract Product: defines common interface for all notification types."""
    
    @abstractmethod
    def send(self, message: str):
        """All subclasses must implement this method."""
        pass


class EmailNotification(Notification):
    """Concrete Product: Email implementation."""
    
    def send(self, message: str):
        print(f"📧 Email sent: {message}")


class SMSNotification(Notification):
    """Concrete Product: SMS implementation."""
    
    def send(self, message: str):
        print(f"📱 SMS sent: {message}")


class PushNotification(Notification):
    """Concrete Product: Push notification implementation."""
    
    def send(self, message: str):
        print(f"🔔 Push notification sent: {message}")
