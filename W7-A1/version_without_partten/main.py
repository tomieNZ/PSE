"""
Version WITHOUT Factory Pattern
All logic in one file, client tightly coupled to all implementations.
"""


def send_email(message: str):
    """Send email notification."""
    print(f"📧 Email sent: {message}")


def send_sms(message: str):
    """Send SMS notification."""
    print(f"📱 SMS sent: {message}")


def send_push(message: str):
    """Send push notification."""
    print(f"🔔 Push notification sent: {message}")


def main():
    """
    Without Factory Pattern:
    - Client must know ALL notification types
    - Selection logic embedded in client code
    - Adding new types requires modifying this file
    """
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    
    # Client handles all selection logic directly (tight coupling)
    if notification_type == "email":
        send_email("Hello! This is a Factory Pattern example.")
    elif notification_type == "sms":
        send_sms("Hello! This is a Factory Pattern example.")
    elif notification_type == "push":
        send_push("Hello! This is a Factory Pattern example.")
    else:
        raise ValueError("Invalid notification type")


if __name__ == "__main__":
    main()
