#!/usr/bin/python3

"""Base Class Module."""
import json


class Base:
    """Serve as the base class of all classes."""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialize the base class."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json format for list of dict."""
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a json of an object to a file."""
        if not list_objs:
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
                f.write("[]")
        else:
            ans = []
            for obj in list_objs:
                ans.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(ans))

    @staticmethod
    def from_json_string(json_string):
        """Return the object representation of the json object."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of base."""
        fake = None
        if cls.__name__ == "Rectangle":
            fake = cls(2, 2)
        else:
            fake = cls(3)
        fake.update(**dictionary)
        return fake
