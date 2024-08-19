from datetime import datetime

class Apartment:
    """Class representing an apartment and its features."""
    
    def __init__(self, title, address, city, price, surface_area, rooms, construction_year, url, query, id=None):
        self.id = id
        self.title = title
        self.address = address
        self.city = city
        self.price = price
        self.surface_area = surface_area
        self.rooms = rooms
        self.construction_year = construction_year
        self.url = url
        self.query = query
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.href = url  # Use href as a unique identifier
        self.near_by = self._getcity_near_by(self.query)

    def _getcity_near_by(self, query):
        # Split the query by '/' and retrieve the part corresponding to the city
        parts = query.split('/')
        
        # The city is always in the 5th position (index 4), assuming the URL structure is consistent
        if len(parts) > 4:
            city = parts[4]
            return city
        return None

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
            "href": self.href,  # Include href in the dictionary
            "near_by": self.near_by,
            "query": self.query
        }

