from file_utils import read_json_file, write_json_file, clear_screen

def manage_urls(urls_file):
    """Manage the URLs (add, view, remove)."""
    while True:
        clear_screen()
        print("Manage URLs")
        print("-----------")
        print("1. View URLs")
        print("2. Add URL")
        print("3. Remove URL")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_urls(urls_file)
        elif choice == '2':
            add_urls(urls_file)
        elif choice == '3':
            remove_url(urls_file)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

def view_urls(urls_file):
    """View the list of URLs."""
    urls = read_json_file(urls_file)
    if urls:
        print("Currently monitored URLs:")
        for idx, url in enumerate(urls, 1):
            print(f"{idx}. {url}")
    else:
        print("No URLs are currently being monitored.")
    input("Press Enter to return...")

def add_urls(urls_file):
    """Add a new URL."""
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
    """Remove a URL."""
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
    input("Press Enter to return...")
