from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import DB_URL
from models import db
from flask_migrate import Migrate
from routes.index import index_bp
from routes.home import home_bp
from routes.comefly import comefly
from routes.gofly import gofly
from routes.flystatus import flystatus
from routes.about import about


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(index_bp)
app.register_blueprint(home_bp)
app.register_blueprint(comefly)
app.register_blueprint(flystatus)
app.register_blueprint(gofly)
app.register_blueprint(about)

if __name__ == '__main__':
    app.run(debug=True)