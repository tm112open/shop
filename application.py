from flask import Flask

def create_app(**config_overrrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides from test
    app.config.update(config_overrrides)

    # import blueprints
    from home.views import home_app
    from product.views import product_app

    # register blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(product_app)

    return app
