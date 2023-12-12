#!usr/bin/pyhton3
"""Define class Place."""1
from models.base_models import BaseModel


class Place(BaseModel):
    """Define class place."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
