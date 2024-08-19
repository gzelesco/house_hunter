# House Hunter

This is an apartment monitoring program that periodically scrapes apartment listings from pararious.nl, checks for new apartments, and sends email notifications if any new listings are found.

## Features

- Monitor multiple URLs for new apartment listings.
- Manage apartment listing URLs.
- Manage email recipients and email configuration.
- View stored apartment listings.
- Export apartment listings to a CSV file.

## Prerequisites

Before running the program, ensure you have the following:

- Python 3.x installed on your system.
- The required Python libraries (see the `requirements.txt` section).
- An active Gmail account to send email notifications.

## Installation

1. Clone or download the repository.
2. Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the program using:
```bash
python main.py
```
2. The main menu will be displayed, allowing you to:
* Start monitoring apartment listings.
* Manage URLs (add, view, and remove URLs).
* Manage email recipients.
* View apartment listings.

## Main Menu Options
1. __Start Monitoring Apartments__: Starts monitoring the URLs stored in urls.json for any new apartment listings. If a new listing is found, an email notification will be sent to the recipients.
2. __Manage URLs__: Add, view, or remove URLs of apartment listings to be monitored.
3. __Manage Email Recipients__: Add, view, or remove email recipients for notifications.
4. __Manage Email Configuration__: Set up or view the sender email and password.
5. __View Apartment Listings__: View the stored apartment listings or export them to a CSV file.
6. __Exit__: Exits the program.

## Example Email Notification
```bash
New Apartment Found near Amsterdam! 🏠

ID: 101
Title: Spacious Apartment in the City Center
Address: 123 Main St, Amsterdam
City: Amsterdam
Price: €1200/month
Surface Area: 75 m²
Rooms: 2
URL: https://www.pararius.com/apartment/amsterdam/12345
Timestamp: 2023-08-20 14:30:00
```

## Important Notes
* __Email Notifications__: Make sure to use a Gmail account for sending email notifications. For security reasons, it's recommended to use an app password instead of your regular Gmail password. You can generate an app password from your Google Account settings.
* __Query__: There is no user interface to prepare the URLs for queries. This is because websites like Pararius already provide this functionality. Once you find a query that fits your search criteria, simply save it in this program. The program will handle the monitoring for you.

## File Structure
```bash
.
├── json/
│   ├── urls.json
│   ├── apartment_hrefs.json
│   ├── recipients.json
│   └── email_config.json
├── scripts/
│   ├── apartment.py
│   ├── email_utils.py
│   ├── file_utils.py
│   ├── monitoring.py
│   └── url_utils.py
├── main.py
└── README.md
```

## Dependencies
The program relies on the following libraries:
* __requests__: For sending HTTP requests to the apartment listing websites.
* __beautifulsoup4__: For parsing HTML pages and extracting apartment information.
* __smtplib__: For sending email notifications.
* __email__: For formatting email messages.
* __json__: For handling JSON file operations.
* __csv__: For exporting apartment listings to CSV format.

To install these dependencies, use:
```bash
pip install -r requirements.txt
```

## Customization
* __Monitoring Interval__:
The default monitoring interval is set to 5 minutes (__'CHECK_INTERVAL = 300'__ seconds). You can change this value in the __main.py__ file.
* __Supported Websites__:
Unfortunately, this scraper only works with __Pararius__. If you have the know-how to adapt this scraper to work with other real estate websites, such as __Funda__, please feel free to fork the repository and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License.