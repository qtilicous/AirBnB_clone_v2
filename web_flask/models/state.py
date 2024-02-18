#!/usr/bin/python3
"""This module defines the State class."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This class defines a state by various attributes."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan"
            )

    if models.storage_type != "db":
        @property
        def cities(self):
            """Return the list of City objects linked to the current State"""
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
