from flask import jsonify
from database.models import *
from playhouse.shortcuts import model_to_dict

def create_item(model, data):
    try:
        item = model.create(**data)
        return jsonify(model_to_dict(item)), 201
    except IntegrityError:
        return jsonify({'error': f'{model.__name__} with the same data already exists'}), 400

def get_all_items(model):
    item_list = [model_to_dict(item) for item in model.select()]
    return jsonify({f'{model.__name__.lower()}s': item_list})

def get_item_by_id(model, item_id):
    try:
        item = model.get(model.id == item_id)
        return jsonify(model_to_dict(item))
    except DoesNotExist:
        return jsonify({'error': f'{model.__name__} not found'}), 404

def delete_item(model, item_id):
    try:
        item = model.get(model.id == item_id)
        item.delete_instance()
        return jsonify({'message': f'{model.__name__} deleted successfully'}), 200
    except DoesNotExist:
        return jsonify({'error': f'{model.__name__} not found'}), 404