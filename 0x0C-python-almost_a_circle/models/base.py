#!/usr/bin/python3
"""module that define Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for Base class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        
        sorted_dicts = []
        for d in list_dictionaries:
            sorted_dict = {
                'x': d['x'],
                'width': d['width'],
                'id': d['id'],
                'height': d['height'],
                'y': d['y']
            }
            sorted_dicts.append(sorted_dict)
    
        return json.dumps(sorted_dicts)

    @classmethod
    def from_json_string(cls, json_string):
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(obj_list))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []
