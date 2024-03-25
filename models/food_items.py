#!/usr/bin/python3
"""
This is a class for the food items that
will be passed and retrived from storage
"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Text, DECIMAL
import models


class FoodItems(BaseModel, Base):
    """
    This class defines food items with various attributes
    """
    __tablename__ = 'Food_Items'

    item_name = Column(String(255), nullable=False)
    item_description = Column(Text)
    item_category = Column(String(100))
    item_first_price = Column(DECIMAL(10, 2), nullable=False)
    item_second_price = Column(DECIMAL(10, 2))
    item_image = Column(String(255))
    background_image = Column(String(255))
    icon_1 = Column(String(255))
    icon_2 = Column(String(255))
    icon_3 = Column(String(255))
