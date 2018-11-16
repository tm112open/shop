from flask import Blueprint
from flask import jsonify, request, abort

home_app = Blueprint('home_app', __name__)

@home_app.route('/')
def home():
    return jsonify({"products": request.host_url + "products/"})