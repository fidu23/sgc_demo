from flask import Flask
from flask_restful import Resource,Api
from vistas import VistaCliente,VistaClientes,VistaTiposPersonas,VistaTipoPersona,\
                   VistaTipoDocumento,VistaTiposDocumentos

from modelos import db,triggers
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="oracle://SGC_DEMO:sgc_dev_2023@localhost:1522/xe"
app_context=app.app_context()
app_context.push()

db.init_app(app)
migrate = Migrate(app, db)


api=Api(app)
db.create_all()

for i in triggers:
    db.session.execute(i)

api.add_resource(VistaTiposPersonas, '/tipopersona')
api.add_resource(VistaTipoPersona,'/tipopersona/<string:tper_tipo>')
api.add_resource(VistaTiposDocumentos, '/tipodocumento')
api.add_resource(VistaTipoDocumento, '/tipodocumento/<string:tdoc_documento>')

api.add_resource(VistaClientes, '/clientes')
api.add_resource(VistaCliente, '/cliente/<int:clnte_id>')


