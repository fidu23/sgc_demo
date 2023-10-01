from flask import Flask
from flask_restful import Resource,Api
from vistas import VistaCliente
from modelos import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="oracle://SGC_DEMO:sgc_dev_2023@localhost:1521/xe"
app_context=app.app_context()
app_context.push()

db.init_app(app)
migrate = Migrate(app, db)


api=Api(app)
db.create_all()

api.add_resource(VistaCliente, '/clientes')
