from scripts.monitoring import monitor_apartment_changes
from scripts.file_utils import read_json_file, clear_screen, view_apartment_hrefs
from scripts.email_utils import manage_recipients, manage_email_config
from scripts.url_utils import manage_urls
from time import sleep

# Constants
CHECK_INTERVAL = 300  # 5 minutes
urls_file = 'json\\urls.json'
href_file = 'json\\apartment_hrefs.json'
recipients_file = 'json\\recipients.json'
email_file = 'json\\email_config.json'

def main_menu():
    """Main menu to navigate the program."""
    while True:
        clear_screen()
        print("Apartment Monitoring Program")
        print("----------------------------")
        print("1. Start Monitoring Apartments")
        print("2. Manage URLs")
        print("3. Manage Email Recipients")
        print("4. Manage Email Configuration")
        print("5. View Apartment Listings")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            urls = read_json_file(urls_file)
            if urls:
                monitor_apartment_changes(urls, CHECK_INTERVAL)
            else:
                print("No URLs to monitor. Please add URLs first.")
                sleep(1)
        elif choice == '2':
            manage_urls(urls_file)
        elif choice == '3':
            manage_recipients(recipients_file)
        elif choice == '4':
            manage_email_config(email_file)
        elif choice == '5':
            view_apartment_hrefs(href_file)
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
            sleep(1)

# Entry point for the program
if __name__ == "__main__":
    main_menu()
