#!/usr/bin/python3
"""module import"""
import unittest
import uuid
import time
import datetime
from datetime import datetime
from models.base_model import BaseModel

"""class test case to tests the class attriputes(public attributes)
setup method creates the object and runs over and over
class method runs only ones
"""

class TestBaseModel(unittest.TestCase):
    """apply setup method to create object"""
    def setUp(self):
        self.base_model = BaseModel()

    """define test method to test save()"""
    def  test_save_(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        #time.sleep()

        self.assertEqual(initial_updated_at, self.base_model.updated_at)

    """test to_dict function"""
    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict ["__class__"], "BaseModel")
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

        self.assertEqual(obj_dict["created_at"], self.base_model.created_at)
        self.assertEqual(obj_dict["updated_at"], self.base_model.updated_at.isoformat())

    @classmethod
    def setUpClass(cls):
        cls.model_data = {
            "id": "2d5530ad-9150-42ce-a71a-6105672b2d66",
            "created_at": "2023-08-10T18:15:45.469858",
            "updated_at": "2023-08-10T18:15:45.469858",
            "name": "My_First_Model",
            "my_number": 89,
            "__class__": "BaseModel"
        }

    def test_recreate_instance(self):
        my_new_model = BaseModel(**self.model_data)

        self.assertEqual(my_new_model.id, self.model_data["id"])
        expected_created_at = datetime.strptime(self.model_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(my_new_model.created_at, expected_created_at)
 
        expected_updated_at = datetime.strptime(self.model_data["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(my_new_model.updated_at, expected_updated_at)

        self.assertEqual(my_new_model.name, self.model_data["name"])
        self.assertEqual(my_new_model.my_number, self.model_data["my_number"])


if __name__ == "__main__":
    unittest.main()
