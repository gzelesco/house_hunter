import requests
from bs4 import BeautifulSoup
import threading
import time
import keyboard
from datetime import datetime

from scripts.apartment import Apartment
from scripts.file_utils import read_json_file, write_json_file
from scripts.email_utils import send_email

base_url = 'https://www.pararius.com'
href_file = 'json\\apartment_hrefs.json'

def get_all_apartment_data(url):
    """Fetch all apartment data from the URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all listings with the specific class
        listings = soup.find_all('div', class_='listing-search-item__content')
        apartments = []
        
        for listing in listings:
            link_tag = listing.find('a', class_='listing-search-item__link--title')
            href = link_tag['href'] if link_tag else None
            title = link_tag.text.strip() if link_tag else "N/A"
            
            sub_title = listing.find('div', class_='listing-search-item__sub-title')
            address_city = sub_title.text.strip().split('(') if sub_title else ["N/A", "N/A"]
            address = address_city[0].strip()
            city = address_city[1][:-1] if len(address_city) > 1 else "N/A"  # Remove closing parenthesis

            price_tag = listing.find('div', class_='listing-search-item__price')
            price = price_tag.text.strip() if price_tag else "N/A"
            
            features_tag = listing.find('ul', class_='illustrated-features--compact')
            surface_area = features_tag.find_all('li')[0].text.strip() if features_tag else "N/A"
            rooms = features_tag.find_all('li')[1].text.strip() if features_tag else "N/A"
            #construction_year = features_tag.find_all('li')[2].text.strip() if features_tag else "N/A"

            final_url = format_href(base_url, href)

            apartment = Apartment(
                title=title,
                address=address,
                city=city,
                price=price,
                surface_area=surface_area,
                rooms=rooms,
                construction_year="XXXX",
                url=final_url,
                query=url
            )
            apartments.append(apartment)
        return apartments

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []


def format_href(base_url, href):
    """Format the href to a full URL."""
    return href if href.startswith('https') else base_url + href

def monitor_url(url, results):
    """Monitor a single URL for changes."""
    apartments = get_all_apartment_data(url)
    
    # Find the maximum existing ID
    max_id = max((entry['id'] for entry in results if 'id' in entry), default=0)
    
    new_listings_detected = False  # Flag to check if any new apartments were found

    for apartment in apartments:
        apartment_dict = apartment.to_dict()
        if not any(apartment_dict['url'] == entry['url'] for entry in results):
            # Apartment is new, assign a new unique ID
            max_id += 1
            apartment.id = max_id
            
            # Update the apartment_dict with the new ID
            apartment_dict['id'] = apartment.id
            
            # Append new apartment and update JSON file
            results.append(apartment_dict)
            write_json_file(href_file, results)
            
            # Send email notification
            send_email(apartment_dict)
            
            # Set the flag to True since a new listing was found
            new_listings_detected = True

    # Print the message only if no new apartments were detected
    if not new_listings_detected:
        print(f"No new listings detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def monitor_apartment_changes(urls, check_interval):
    """Monitor multiple apartment URLs for changes."""

    try:
        print("Press 'ctrl + C' to stop monitoring.")
        while True:
            results = read_json_file(href_file)

            while True:

                threads = []
                for url in urls:
                    thread = threading.Thread(target=monitor_url, args=(url, results))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

                print("End of scraping. It will start again soon...\n")
                time.sleep(check_interval)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
