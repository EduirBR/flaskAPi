from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from .settings import Config
from werkzeug.routing import Map
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(Config)
    db.init_app(app)
    @app.route('/')
    def index():
        links = []
        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append(url)
        response = {
            'endpoints': links
        }
        return response

    from apps.contacts.route import contactBlueprint
    app.register_blueprint(contactBlueprint)

    
    with app.app_context():
        db.create_all()
    return app