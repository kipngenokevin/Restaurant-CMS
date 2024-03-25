#!/usr/bin/python3
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This performs tests on the BaseModel class"""
    
    def test_init(self):
        """This tests the init method of the BaseModel class"""
        with patch('models.base_model.uuid.uuid4') as mock_uuid:
            mock_uuid.return_value = '1234'
            obj = BaseModel()
            self.assertEqual(obj.id, '1234')
            self.assertIsInstance(obj.created_at, datetime)
            self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Tests the init method using key word arguments"""
        with patch('models.base_model.uuid.uuid4') as mock_uuid:
            mock_uuid.return_value = '1234'
            created_at = updated_at = datetime.now()
            obj = BaseModel(id='5678', created_at=created_at, updated_at=updated_at)
            self.assertEqual(obj.id, '5678')
            self.assertEqual(obj.created_at, created_at)
            self.assertEqual(obj.updated_at, updated_at)

    def test_str(self):
        """Test the str method"""
        obj = BaseModel()
        self.assertEqual(str(obj), "[BaseModel] ({}) {}".format(obj.id, obj.__dict__))

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method in the BaseModel class"""
        obj = BaseModel()
        obj.save()
        self.assertIsInstance(obj.updated_at, datetime)
        mock_storage.new.assert_called_once_with(obj)
        mock_storage.save.assert_called_once()

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """This method tests the to_dict method from the BaseModel class"""
        created_at = updated_at = datetime.now()
        obj = BaseModel(id='1234', created_at=created_at, updated_at=updated_at)
        expected_dict = {
                'id': '1234',
                'created_at': created_at.isoformat(),
                'updated_at': updated_at.isoformat(),
                '__class__': 'BaseModel'
                }
        self.assertDictEqual(obj.to_dict(), expected_dict)

    @patch('models.storage')
    def test_delete(self, mock_storage):
        """This tests the delete method of the BaseModel class"""
        obj = BaseModel()
        obj.delete()
        mock_storage.delete.assert_called_once_with(obj)
        mock_storage.save.assert_called_once()

if __name__ == '__main__':
    """Run the unittests without importing"""
    unittest.main()
