"""
Factory Pattern - Client Code
Demonstrates how client uses factory without knowing concrete classes.
"""
from notification import EmailNotification, SMSNotification, PushNotification


def main():
    notification = None  # Initialize the notification object with None
    # Get user input for notification type and convert to lowercase
    notification_type = input(
        "Enter notification type (email/sms/push): ").lower()
    # Create the appropriate notification object based on user input
    match notification_type:
        case "email":
            notification = EmailNotification()
        case "sms":
            notification = SMSNotification()
        case "push":
            notification = PushNotification()
        case _:
            print("Invalid notification type")

    # If a valid notification object is created, send the message
    if notification is not None:
        notification.send("Hello! This is a Factory Pattern example.")


if __name__ == "__main__":
    main()
