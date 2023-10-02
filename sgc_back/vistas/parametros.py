from flask import request,jsonify
from flask_restful import Resource
from modelos import db,TipoPersona,TipoDocumento,TipoDocumentoSchema,TipoPersonaSchema,ActividadEconomica,ActividadEconomicaSchema,\
    CategoriaAEconomica,CategoriaAEconomicaSchema,DivisionCEconomica,DivisionCEconomicaSchema

tipo_persona_schema=TipoPersonaSchema()
tipo_documento_schema=TipoDocumentoSchema()
tipo_actividad_schema=ActividadEconomicaSchema()
tipo_categoria_economica_schema=CategoriaAEconomicaSchema()
tipo_division_economica_schema=DivisionCEconomicaSchema()

class VistaTiposPersonas(Resource):
    def get(self):

        tipo_persona=TipoPersona.query.all()
        return tipo_persona_schema.dump(tipo_persona, many=True)
    
    def post(self):

        tipo_persona_val=db.session.query(TipoPersona).filter(TipoPersona.tper_tipo==request.json['tper_tipo']).first()
        
        if tipo_persona_val is not None:
            response=jsonify({"error":"Ya existe un tipo de persona de este tipo"})
            response.status_code=409
            return response
        
        nuevo_tipo_persona=TipoPersona(
            tper_tipo = request.json['tper_tipo'],
            tper_nombre= request.json['tper_nombre'],
            tper_descripcion= request.json['tper_descripcion']            
        )
        db.session.add(nuevo_tipo_persona)
        db.session.commit()
        return tipo_persona_schema.dump(nuevo_tipo_persona)

class VistaTipoPersona(Resource):
    def get(self,tper_tipo):
        return tipo_persona_schema.dump(TipoPersona.get_or_404(tper_tipo))

class VistaTiposDocumentos(Resource):
    def get(self):
        tipos_documento = TipoDocumento.query.all()
        return tipo_documento_schema.dump(tipos_documento, many=True)
    
    def post(self):
        
        tdoc_documento_val = db.session.query(TipoDocumento).filter(TipoDocumento.tdoc_documento == request.json['tdoc_documento']).first()
        
        if tdoc_documento_val:
            response = jsonify({"error": "Ya existe un tipo de documento con este código"})
            response.status_code = 409
            return response

        tper_val= db.session.query(TipoPersona).filter(TipoPersona.tper_tipo == request.json['tdoc_tipopersona']).first()
        if tper_val is None:
            response = jsonify({"error": "Tipo de persona invalido"})
            response.status_code = 409
            return response
        nuevo_tipo_documento = TipoDocumento(
            tdoc_documento=request.json['tdoc_documento'],
            tdoc_descripcion=request.json['tdoc_descripcion'],
            tdoc_tipopersona_id=request.json['tdoc_tipopersona']
        )
        db.session.add(nuevo_tipo_documento)
        db.session.commit()
        return tipo_documento_schema.dump(nuevo_tipo_documento)

class VistaTipoDocumento(Resource):
    def get(self, tdoc_documento):        
        return tipo_documento_schema.dump(TipoDocumento.get_or_404(tdoc_documento))

class VistaActividadEconomica(Resource):
    def get(self):
        actividades_economicas=ActividadEconomica.query.all()
        return tipo_actividad_schema.dump(actividades_economicas, many=True)     

class VistaCategoriaEconomica(Resource):
    def get(self):
        categorias_economicas=CategoriaAEconomica.query.all()
        return tipo_categoria_economica_schema.dump(categorias_economicas, many=True)

class VistaDivisionEconomica(Resource):
    def get(self):
        divisiones_economicas=DivisionCEconomica.query.all()
        return tipo_division_economica_schema.dump(divisiones_economicas, many=True)