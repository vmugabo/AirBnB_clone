#!/usr/bin/python3
"""Create base class for AirBnB clone console
    """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for base model of object."""
    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "update_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)
            
    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""
        return f"{type(self).__name__} ({self.id} {self.__dict__})"
    
    
    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""
        self.update_at = datetime.now()
        storage.save()
        
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        """
        bnb_dict = self.__dict__
        bnb_dict["__class__"] = type(self).__name__
        bnb_dict["created_at"] = bnb_dict["created_at"].isoformat()
        bnb_dict["updated_at"] = bnb_dict["updated_at"].isoformat()
        return bnb_dict
