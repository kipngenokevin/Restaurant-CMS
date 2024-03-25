#!/usr/bin/python3
"""
This module is meant to test the db_storage class
"""
import unittest
from models.engine.db_storage import DBStorage
from models.food_items import FoodItems


class TestDBStorage(unittest.TestCase):
    """
    This is a class to test the DBStorage class methods
    """
    def setUp(self):
        """creates an instance of DBStorage used during the testing phase"""
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """Method to destroy the instance of the DBStorage class"""
        self.storage.close()

    def test_all(self):
        """Test the method that displays all the items in the Food items
        table"""
        food_item = FoodItems(item_name="Test Food", item_first_price=10.99)
        self.storage.new(food_item)
        self.storage.save()

        all_data = self.storage.all(FoodItems)
        self.assertIsInstance(all_data, dict)
        self.assertIn(f"FoodItems.{food_item.id}", all_data)

    def test_new_and_save(self):
        """Test the new and save method from the DBstorage class"""
        initial_count = self.storage.count(FoodItems)

        food_item = FoodItems(item_name="New Food", item_first_price=5.99)
        self.storage.new(food_item)
        self.storage.save()

        new_count = self.storage.count(FoodItems)
        self.assertEqual(new_count, initial_count)

    def test_delete(self):
        """Tests the delete method"""
        food_item = FoodItems(item_name="Item to Delete", item_first_price=15.99)
        self.storage.new(food_item)
        self.storage.save()

        initial_count = self.storage.count(FoodItems)

        self.storage.delete(food_item)
        self.storage.save()

        new_count = self.storage.count(FoodItems)
        self.assertEqual(new_count, initial_count)

    def test_reload(self):
        """This tests the instance method reload in the DBStorage Method"""
        old_session_id = id(self.storage._DBStorage__session)
        self.storage.reload()
        new_session_id = id(self.storage._DBStorage__session)
        self.assertNotEqual(old_session_id, new_session_id)

    def test_count(self):
        """Tests the count method in the DBStorage class"""
        initial_count = self.storage.count(FoodItems)
        for _ in range(3):
            food_item = FoodItems(item_name="Test Food", item_first_price=9.99)
            self.storage.new(food_item)
            self.storage.save()

        self.storage.reload()
        count = self.storage.count(FoodItems)
        self.assertEqual(count, initial_count)

if __name__ == "__main__":
    unittest.main()
