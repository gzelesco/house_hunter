import smtplib
from email.message import EmailMessage

from scripts.file_utils import read_json_file, write_json_file, clear_screen

email_file = 'json\\email_config.json'
recipients_file = 'json\\recipients.json'

def send_email(apartment):
    """Send an email using Gmail with formatted apartment details."""
    email_config = read_json_file(email_file)
    if not email_config:
        print("Email configuration not found.")
        return
    
    sender_email = email_config.get('email')
    sender_password = email_config.get('password')
    recipients = read_json_file(recipients_file)

    if not sender_email or not sender_password:
        print("Sender email credentials are missing.")
        return

    if not recipients:
        print("No recipients configured.")
        return

    # Format the email subject
    subject = f"New House [{apartment['id']}]: by {apartment['near_by']} - {apartment['title']}"
    
    # Correctly format price and surface area
    price = apartment['price'].replace("\u20ac", "€").replace(",", "").strip()
    surface_area = apartment['surface_area'].replace("\u00b2", "²").strip()

    # Format the email body in a more readable format
    body = f"""
    New Apartment Found near {apartment['near_by']}! 🏠

    ID: {apartment['id']}
    Title: {apartment['title']}
    Address: {apartment['address']}
    City: {apartment['city']}
    Price: {price}
    Surface Area: {surface_area}
    Rooms: {apartment['rooms']}
    URL: {apartment['url']}
    Timestamp: {apartment['timestamp']}

    Query used: {apartment['query']}

    """

    # Create the email message
    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = ', '.join(recipients)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"Email sent successfully.  {apartment['near_by']} at {apartment['timestamp']}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def manage_email_config(email_file):
    """Manage the email configuration (set email and password)."""
    while True:
        clear_screen()
        print("Manage Email Configuration")
        print("--------------------------")
        print("1. View Email Configuration")
        print("2. Set Email and Password")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_email_config(email_file)
        elif choice == '2':
            set_email_config(email_file)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

def view_email_config(email_file):
    """View the current email configuration."""
    email_config = read_json_file(email_file)
    if email_config:
        print(f"Current Email: {email_config.get('email', 'Not set')}")
    else:
        print("No email configuration found.")
    input("Press Enter to return...")

def set_email_config(email_file):
    """Set the email and password for sending emails."""
    email = input("Enter the sender email (Gmail): ")
    password = input("Enter the sender password: ")
    
    email_config = {
        'email': email,
        'password': password
    }
    
    write_json_file(email_file, email_config)
    print("Email configuration has been updated.")

def manage_recipients(recipients_file):
    """Manage email recipients."""
    while True:
        clear_screen()
        print("Manage Recipients")
        print("-----------------")
        print("1. View Recipients")
        print("2. Add Recipients")
        print("3. Remove Recipients")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_recipients(recipients_file)
        elif choice == '2':
            add_recipients(recipients_file)
        elif choice == '3':
            remove_recipients(recipients_file)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

def view_recipients(recipients_file):
    """View the list of email recipients."""
    recipients = read_json_file(recipients_file)
    if recipients:
        print("Current Recipients:")
        for idx, email in enumerate(recipients, 1):
            print(f"{idx}. {email}")
    else:
        print("No recipients configured.")
    input("Press Enter to return...")

def add_recipients(recipients_file):
    """Add new email recipients."""
    recipients = read_json_file(recipients_file)
    while True:
        new_email = input("Enter the new recipient email (or type 'done' to finish): ")
        if new_email.lower() == 'done':
            break
        if new_email and new_email not in recipients:
            recipients.append(new_email)
    write_json_file(recipients_file, recipients)
    print("Recipients have been added.")

def remove_recipients(recipients_file):
    """Remove an email recipient."""
    recipients = read_json_file(recipients_file)
    if not recipients:
        print("No recipients available to remove.")
        return
    view_recipients(recipients_file)
    try:
        idx = int(input("Enter the number of the recipient to remove: ")) - 1
        if 0 <= idx < len(recipients):
            recipients.pop(idx)
            write_json_file(recipients_file, recipients)
            print("Recipient removed successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")
    input("Press Enter to return...")
