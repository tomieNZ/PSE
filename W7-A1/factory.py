"""
Factory Pattern - Factory Class
Centralizes object creation logic, decoupling client from concrete classes.
"""
from notification import EmailNotification, SMSNotification, PushNotification


class NotificationFactory:
    """
    Factory class: creates notification objects based on type parameter.
    Client only needs to know the factory, not the concrete classes.
    """
    
    @staticmethod
    def create_notification(notification_type: str):
        """
        Factory method: returns appropriate notification object.
        
        Args:
            notification_type: "email", "sms", or "push"
        Returns:
            Notification instance
        Raises:
            ValueError: if invalid type
        """
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Invalid notification type")
