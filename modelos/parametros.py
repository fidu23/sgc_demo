from . import db

from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

#CREATE SEQUENCE ge_spais START WITH 1 INCREMENT BY 1;
ge_spais=db.Sequence('ge_spais')
#CREATE SEQUENCE ge_sdepartamento START WITH 1 INCREMENT BY 1;
ge_sdepartamento=db.Sequence('ge_sdepartamento')
#CREATE SEQUENCE ge_sciudad START WITH 1 INCREMENT BY 1;
ge_sciudad=db.Sequence('ge_sciudad')

class TipoPersona(db.Model):
    __tablename__="ge_ttipopersona"
    tper_tipo = db.Column(db.String(3), primary_key=True)
    tper_nombre=db.Column(db.String(32),nullable=False)
    tper_descripcion=db.Column(db.String(100),nullable=False)
    tper_tipos_documentos=db.relationship('TipoDocumento',back_populates='tdoc_tipopersona')


class TipoDocumento(db.Model):
    __tablename__="ge_ttipodocumento"    
    tdoc_documento = db.Column(db.String(30),primary_key=True)    
    tdoc_descripcion = db.Column(db.String(100), nullable=False)
    tdoc_tipopersona_id = db.Column(db.String(3), db.ForeignKey("ge_ttipopersona.tper_tipo"))
    tdoc_tipopersona=db.relationship("TipoPersona",back_populates="tper_tipos_documentos")
    

class Paises(db.Model):
    __tablename__="ge_tpais"
    pais_id=db.Column(db.Integer(),ge_spais,primary_key=True)    
    pais_nombre=db.Column(db.String(52),nullable=False)
    pais_codigo_iso=db.Column(db.String(4))
    pais_codigo_dian=db.Column(db.String(6))
    pais_codigo_telf=db.Column(db.String(10))


class Departamento(db.Model):
    __tablename__="ge_tdepartamento"
    depto_id=db.Column(db.Integer(),ge_sdepartamento, primary_key=True)
    depto_nombre=db.Column(db.String(52),nullable=False)
    depto_pais=db.Column(db.Integer(),db.ForeignKey("ge_tpais.pais_id"))


class Ciudad(db.Model):
    __tablename__="ge_tciudad"
    ciud_id=db.Column(db.Integer(),ge_sciudad,primary_key=True)
    ciud_nombre=db.Column(db.String(52),nullable=False)
    ciud_codigo_dane=db.Column(db.String(10))
    ciud_departamento=db.Column(db.Integer(),db.ForeignKey("ge_tdepartamento.depto_id"))


class ActividadEconomica(db.Model):
    __tablename__="ge_tactividad_economica"    
    acecn_codigo_ciu=db.Column(db.String(20),primary_key=True)    
    acecn_nombre=db.Column(db.String(52),nullable=False)
    acecn_categoria_id=db.Column(db.String(20),db.ForeignKey("ge_tcategoria_acecn.ctecn_codigo_ciu"))
    
    

class CategoriaActividadEconomica(db.Model):
    __tablename__="ge_tcategoria_acecn"    
    ctecn_codigo_ciu=db.Column(db.String(20),primary_key=True)
    ctecn_nombre=db.Column(db.String(52),nullable=False)
    ctecn_division_id=db.Column(db.String(20),db.ForeignKey("ge_tdivison_ctecn.dvecn_codio_ciu"))
    ctecn_division=db.relationship("DivisionEconomica",backref="ge_tcategoria_acecn")
    actividades=db.relationship('ActividadEconomica',cascade="all,delete,delete-orphan")

class DivisionEconomica(db.Model):
    __tablename__="ge_tdivison_ctecn"
    dvecn_codio_ciu = db.Column(db.String(20),primary_key=True)
    dvecn_nombre=db.Column(db.String(52),nullable=False)
    

class DivisionEconomicaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=DivisionEconomica
        load_instance=True


class ActividadEconomicaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=ActividadEconomica
        load_instance=True
    
    
class CategoriaActividadEconomicaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=CategoriaActividadEconomica
        load_instance=True

    ctecn_division=fields.Nested(DivisionEconomicaSchema)
    actividades=fields.List(fields.Nested(ActividadEconomicaSchema()))


class TipoPersonaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=TipoPersona
        load_instance=True
        
class TipoDocumentoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=TipoDocumento
        load_instance=True   
    tdoc_tipopersona=fields.Nested(TipoPersonaSchema)


pais_trigger=db.DDL(
    f'''
    CREATE OR REPLACE TRIGGER pais_trigger
    BEFORE INSERT ON ge_tpais
    FOR EACH ROW
    BEGIN
        SELECT ge_spais.NEXTVAL INTO :new.pais_id FROM dual;
    END;
    '''
)
ciudad_trigger=db.DDL(
    f'''
    CREATE OR REPLACE TRIGGER ciudad_trigger
    BEFORE INSERT ON ge_tciudad
    FOR EACH ROW
    BEGIN
    SELECT ge_sciudad.NEXTVAL INTO :new.ciud_id FROM dual;
    END;
    '''
)
departamento_trigger=db.DDL(
    f'''
    CREATE OR REPLACE TRIGGER departamento_trigger
    BEFORE INSERT ON ge_tdepartamento
    FOR EACH ROW
    BEGIN
    SELECT ge_sdepartamento.NEXTVAL INTO :new.depto_id FROM dual;
    END;
    '''
)

