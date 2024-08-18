from datetime import datetime

class Apartment:
    """Class representing an apartment and its features."""
    
    def __init__(self, title, address, city, price, surface_area, rooms, construction_year, url, id=None):
        self.id = id
        self.title = title
        self.address = address
        self.city = city
        self.price = price
        self.surface_area = surface_area
        self.rooms = rooms
        self.construction_year = construction_year
        self.url = url
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.href = url  # Use href as a unique identifier

    def to_dict(self):
        """Convert the apartment object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "address": self.address,
            "city": self.city,
            "price": self.price,
            "surface_area": self.surface_area,
            "rooms": self.rooms,
            "construction_year": self.construction_year,
            "url": self.url,
            "timestamp": self.timestamp,
            "href": self.href  # Include href in the dictionary
        }

