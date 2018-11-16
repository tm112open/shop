from flask import Blueprint

from product.api import ProductAPI

product_app = Blueprint('product_app', __name__)


product_app.add_url_rule('/products/', view_func=ProductAPI.as_view('products'))