#!/usr/bin/python3


"""The super class that others will inherit from"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all attributes for the classes"""

    def __init__(self, *args, **kwargs):
        """initialize all attributes"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            format = "%Y-%m-%d T%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in {'created_at', 'udated_at'}:
                    value = datetime.strptime(value, format)
                if key != '__class__':
                    setattr(self, key, value)
	def __str__(self)
		"""print class name id and attributes of the dictionary"""
		class_name = self.__class__.__name__
		return "[{}] [{}] [{}]" .format(class_name, self.id, sel.__dict__)

	def save(self)
		"""updates the attribute updated_at to the current time"""
		self.updated_at = datetime.now()
		storage.save()

	def to_dict(self)
		"""create a dictionary representaion of the base model instances
		convert datetime attributes to ISO format
		"""
		result = self.__dict__.copy()
		result['crated_at'] = self.created_at.isoformat()
		result['updated_at'] = self.updated_at.isoformat()
		result['__class__'] = self.__class__.__name__
		return result
