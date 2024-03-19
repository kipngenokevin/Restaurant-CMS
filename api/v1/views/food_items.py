#!/usr/bin/python3
"""
Objects that haldle all default RESTFul API actions for FoodItems
"""
from models.food_items import FoodItems
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/food_items', methods=['GET'], strict_slashes=False)
def get_food_items():
    """
    Retrieves the list of all food items
    """
    all_food_items = storage.all(FoodItems).values()
    list_food_items = [food_item.to_dict() for food_item in all_food_items]
    return jsonify(list_food_items)


@app_views.route('/food_items/<food_item_id>', methods=['GET'],
                 strict_slashes=False)
def get_food_item(food_item_id):
    """
    Retrieves a single food item
    """
    food_item = storage.get(FoodItems, food_item_id)
    if not food_item:
        abort(404)
    return jsonify(food_item.to_dict())


@app_views.route('/food_items/<food_item_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_food_item(food_item_id):
    """
    Deletes a food item object
    """
    food_item = storage.get(FoodItems, food_item_id)
    if not food_item:
        abort(404)

    storage.delete(food_item)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/food_items', methods=['POST'], strict_slashes=False)
def post_food_item():
    """
    Creates a new food item
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'item_name' not in request.get_json():
        abort(400, description="Missing item_name")
    if 'item_first_price' not in request.get_json():
        abort(400, description="Missing item_first_price")

    data = request.get_json()
    instance = FoodItems(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/food_items/<food_item_id>', methods=['PUT'],
                 strict_slashes=False)
def put_food_item(food_item_id):
    """
    Updates a food item
    """
    food_item = storage.get(FoodItems, food_item_id)

    if not food_item:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(food_item, key, value)
    storage.save()
    return make_response(jsonify(food_item.to_dict()), 200)
