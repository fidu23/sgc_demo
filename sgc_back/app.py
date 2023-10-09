from flask import Flask
from flask_restful import Resource,Api
from vistas import VistaCliente,VistaClientes,VistaTiposPersonas,VistaTipoPersona,\
                   VistaTipoDocumento,VistaTiposDocumentos,\
                   VistaActividadEconomica,VistaCategoriaEconomica,VistaDivisionEconomica

from modelos import db,triggers
from flask_migrate import Migrate
from enviroment import user,password,port,host,sid
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"]="oracle://{0}:{1}@{2}:{3}/{4}".format(user,password,host,port,sid)
app_context=app.app_context()
app_context.push()

db.init_app(app)
migrate = Migrate(app, db)


api=Api(app)
db.create_all()

for i in triggers:
    db.session.execute(i)

api.add_resource(VistaTiposPersonas, '/parametros/tipopersona')
api.add_resource(VistaTipoPersona,'/parametros/tipopersona/<string:tper_tipo>')
api.add_resource(VistaTiposDocumentos, '/parametros/tipodocumento')
api.add_resource(VistaTipoDocumento, '/parametros/tipodocumento/<string:tdoc_documento>')
api.add_resource(VistaActividadEconomica,'/parametros/actividad_economica')
api.add_resource(VistaCategoriaEconomica, '/parametros/categoria_economica') 
api.add_resource(VistaDivisionEconomica, '/parametros/division_economica')

api.add_resource(VistaClientes, '/clientes')
api.add_resource(VistaCliente, '/cliente/<int:clnte_id>')




