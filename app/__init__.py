__all__ = ["create_app"]

import os
from flask import Flask


def create_app(test_config: dict[str, str | bool] | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "db.sqlite"),
        SECRET_KEY="dev"
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    if not os.path.exists(app.instance_path):
        os.mkdir(app.instance_path)

    from . import db
    db.init_app(app)

    from .routes import auth_bp, view_bp, create_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(view_bp)
    app.register_blueprint(create_bp)

    return app
