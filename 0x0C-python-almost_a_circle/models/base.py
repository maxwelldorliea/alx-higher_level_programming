#!/usr/bin/python3

"""Base Class Module."""
import json
import csv
import turtle


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
            return "[]"
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

    @classmethod
    def load_from_file(cls):
        """Convert json file to list of instances."""
        instances = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                items = cls.from_json_string(f.read())
                for its in items:
                    instances.append(cls.create(**its))
            return instances
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Create csv file from list of objects."""
        with open(cls.__name__ + ".csv", "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Convert csv file to list of objects."""
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the tkle module."""
        tk = turtle.Turtle()
        tk.screen.bgcolor("#de912c")
        tk.pensize(3)
        tk.shape("turtle")

        tk.color("#f129f2")
        for rect in list_rectangles:
            tk.showturtle()
            tk.up()
            tk.goto(rect.x, rect.y)
            tk.down()
            for _ in range(2):
                tk.forward(rect.width)
                tk.left(90)
                tk.forward(rect.height)
                tk.left(90)
            tk.hideturtle()

        tk.color("#b7e328")
        for sq in list_squares:
            tk.showturtle()
            tk.up()
            tk.goto(sq.x, sq.y)
            tk.down()
            for _ in range(2):
                tk.forward(sq.width)
                tk.left(90)
                tk.forward(sq.height)
                tk.left(90)
            tk.hideturtle()

        turtle.exitonclick()
