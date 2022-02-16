import os
from typing import Dict

from flask import Flask

def print_routes(app: Flask) -> None:
    for rule in app.url_map.iter_rules():
        print(rule)

def create_app(test_config: Dict[str, str] | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "db.sqlite"), 
        SECRET_KEY="dev"
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from .routes import auth_bp, view_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(view_bp)

    # print_routes(app)

    return app
