from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

products = Blueprint('products', 'products')

#INDEX ROUTE url http://localhost:8000/api/v1/products/<idnumber>
@products.route('/', methods=["GET"])
@login_required
def get_all_products():
    try:
        products = [model_to_dict(product) for product in models.Product.select().where(models.Product.owner_id == current_user.id)]
        print(products)
        for product in products:
            product['owner_id'].pop('password')
        return jsonify(data=products, status={"code ": 200, "message": "Success indexing resource"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code ": 400, "message": "Error getting the resources"})


# CREATE ROUTE url http://localhost:8000/api/v1/products/
@products.route('/', methods=["POST"])
@login_required
def create_product():
    try:
        payload = request.get_json()
        payload['owner_id'] = current_user.id
        product = models.Product.create(**payload)
        
        product_dict = model_to_dict(product)
        print(product_dict)
        return jsonify(data=product_dict, status={"code ": 201, "message ": "Successfully Created Resource"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code ": 400, "message ": "Error created the resources"})   

#SHOW ROUTE url http://localhost:8000/api/v1/products/<idnumber>
@products.route('/<id>', methods=["GET"])
def get_one_product(id):
    try:
        product = models.Product.get_by_id(id)
        print(product)
        product_dict = model_to_dict(product)
        return jsonify(data= product_dict, status={"code": 200, "message": f"Found product with id {product.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code:": 400, "message:": "Error getting one resource"})
    
#UPDATE ROUTE url http://localhost:8000/api/v1/products/<idnumber>
@products.route('/<id>', methods=["PUT"])
def update_city(id):
    try:
        payload = request.get_json()
        payload['owner'] = current_user.id
        
        query = models.Product.update(**payload).where(models.Product.id == id)
        query.execute()
        updated_product = model_to_dict(models.Product.get_by_id(id))
        return jsonify(data=updated_product, status={"code ": 200, "message ": f"Resources updated successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code ": 400, "message ": "Error Updating Resource"})
        
#DELETE ROUTE
@products.route('/<id>', methods=["DELETE"])
def delete_product(id):
    try:
        query = models.Product.delete().where(models.Product.id == id)
        query.execute()
        return jsonify(data="Resource Successfully Deleted", status={"code ": 200, "message ": "Successful Deleting Resource"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code ": 400, "message ": "Error Deleting Resource"})