import json
import os

def initialize_json_file(file_path, default_content=None):
    """Initialize JSON file with default content."""
    default_content = default_content or []
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump(default_content, file, indent=4)

def read_json_file(file_path):
    """Read data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_json_file(file_path, data):
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def view_urls(urls_file):
    """Display the current URLs being monitored."""
    urls = read_json_file(urls_file)
    if urls:
        print("Currently monitored URLs:")
        for idx, url in enumerate(urls, 1):
            print(f"{idx}. {url}")
    else:
        print("No URLs are currently being monitored.")
    input("Press Enter to return to the main menu...")

def add_urls(urls_file):
    """Add new URLs to the monitoring list."""
    urls = read_json_file(urls_file)
    while True:
        new_url = input("Enter the new URL (or type 'done' to finish): ")
        if new_url.lower() == 'done':
            break
        if new_url and new_url not in urls:
            urls.append(new_url)
    write_json_file(urls_file, urls)
    print("URLs have been added.")

def remove_url(urls_file):
    """Remove URLs from the monitoring list."""
    urls = read_json_file(urls_file)
    if not urls:
        print("No URLs available to remove.")
        return
    view_urls(urls_file)
    try:
        idx = int(input("Enter the number of the URL to remove: ")) - 1
        if 0 <= idx < len(urls):
            urls.pop(idx)
            write_json_file(urls_file, urls)
            print("URL removed successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")
    input("Press Enter to return to the main menu...")

import csv

def view_apartment_hrefs(href_file):
    """View stored apartment hrefs and provide options to export to CSV or view in terminal."""
    hrefs = read_json_file(href_file)
    if hrefs:
        clear_screen()
        print("\nOptions:")
        print("1. Export to CSV")
        print("2. View on Terminal")
        print("3. Return to Main Menu")
        

        choice = input("Enter your choice: ")

        if choice == '1':
            export_to_csv(hrefs, 'apartment_listings.csv')
            print("Data exported to 'apartment_listings.csv'.")

        elif choice =='2':
            print("Stored apartment listings:")
            for idx, href in enumerate(hrefs, 1):
                print(f"{idx}. {href}")

        elif choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")
    else:
        print("No apartment listings found.")
    input("Press Enter to return to the main menu...")


def export_to_csv(data, file_path):
    """Export the list of apartment listings to a CSV file."""
    if not data:
        print("No data to export.")
        return

    # Extract headers from the first item
    headers = data[0].keys()
    
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data exported to {file_path}.")
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")
