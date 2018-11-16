from flask.views import MethodView
from flask import jsonify, request, abort


class ProductAPI(MethodView):

    products = [
        {"id": 1, "name": "Carrots"},
        {"id": 2, "name": "Potatoes"},
    ]

    def get(self):
        return jsonify({"products": self.products})