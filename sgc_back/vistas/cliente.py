from flask import request,jsonify
from flask_restful import Resource, Api
from modelos import db,Cliente,ClienteSchema,TipoDocumento

cliente_schema = ClienteSchema()

class VistaCliente(Resource):
    def get(self,clnte_id):
        return cliente_schema.dump(Cliente.query_or_404(clnte_id))
    
class VistaClientes(Resource):

    def get(self):
        clientes=Cliente.query.all()
        return cliente_schema.dump(clientes,many=True)
    
    def post(self):
        tdoc=request.json['clnte_tpidentif']
        nroident=request.json['clnte_nroident']
        tipo_documento=db.session.query(TipoDocumento).filter(TipoDocumento.tdoc_documento==tdoc).first()
        cliente_validacion=Cliente.query.filter(Cliente.clnte_tpidentif_id==tdoc,Cliente.clnte_nroident==nroident).first()
        
        if tipo_documento is None:
            response = jsonify({"error": "Tipo de documento invalido"})
            response.status_code = 409
            return response
        
        if cliente_validacion:
            response = jsonify({"error": "Ya existe un cliente con esta cedula"})
            response.status_code = 409
            return response  
         
        nuevo_cliente=Cliente(
            clnte_tpidentif_id=tdoc,
            clnte_nroident=request.json['clnte_nroident'],
            clnte_estado=request.json['clnte_estado'],
            clnte_act_econo_id=request.json['clnte_act_econo'] if 'clnte_act_econo' in request.json else ""
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return cliente_schema.dump(nuevo_cliente)