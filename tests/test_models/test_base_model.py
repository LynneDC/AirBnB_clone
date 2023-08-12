#!/usr/bin/python3
import unittest
import datetime
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define test data for the BaseModel instance
        cls.model_data = {
            "id": "2d5530ad-9150-42ce-a71a-6105672b2d66",
            "created_at": "2023-08-10T18:15:45.469858",
            "updated_at": "2023-08-10T18:15:45.469858",
            "name": "My_First_Model",
            "my_number": 89,
            "__class__": "BaseModel"
        }

    def setUp(self):
        # Create an instance of the BaseModel class for each test
        self.base_model = BaseModel()

    def test_save_(self):
        # Test the save method of the BaseModel class
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()

        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Test the to_dict method of the BaseModel class
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

        expected_created_at = datetime.strptime(
            obj_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(expected_created_at, self.base_model.created_at)

        expected_updated_at = datetime.strptime(
            obj_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(expected_updated_at, self.base_model.updated_at)

    def test_recreate_instance(self):
        # Test recreating an instance of the BaseModel class with test data
        my_new_model = BaseModel(**TestBaseModel.model_data)

        self.assertEqual(my_new_model.id, TestBaseModel.model_data["id"])

        expected_created_at = datetime.strptime(
            TestBaseModel.model_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(expected_created_at, my_new_model.created_at)

        expected_updated_at = datetime.strptime(
            TestBaseModel.model_data["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(expected_updated_at, my_new_model.updated_at)

        self.assertEqual(my_new_model.name, TestBaseModel.model_data["name"])
        self.assertEqual(
            my_new_model.my_number, TestBaseModel.model_data["my_number"])


if __name__ == "__main__":
    # Run the tests
    unittest.main()
