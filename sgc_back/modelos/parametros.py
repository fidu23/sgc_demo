from . import db

from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

#CREATE SEQUENCE ge_spais START WITH 1 INCREMENT BY 1;
ge_spais=db.Sequence('ge_spais')
#CREATE SEQUENCE ge_sdepartamento START WITH 1 INCREMENT BY 1;
ge_sdepartamento=db.Sequence('ge_sdepartamento')
#CREATE SEQUENCE ge_sciudad START WITH 1 INCREMENT BY 1;
ge_sciudad=db.Sequence('ge_sciudad')
#CREATE SEQUENCE ge_sactividad_economica START WITH 1 INCREMENT BY 1;
ge_sactividad_economica=db.Sequence('ge_sactividad_economica')
#CREATE SEQUENCE ge_scategoria_acecn START WITH 1 INCREMENT BY 1;
ge_scategoria_acecn=db.Sequence('ge_scategoria_acecn')
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
    acecn_id=db.Column(db.Integer(),ge_sactividad_economica,primary_key=True)
    acecn_codigo_ciu=db.Column(db.String(20))
    __table_args__ = (db.UniqueConstraint('acecn_codigo_ciu', name='uq_acecn_codigo_ciu'),)

class CategoriaActividadEconomica(db.Model):
    __tablename__="ge_tcategoria_acecn"
    ctecn_id=db.Column(db.Integer(),primary_key=True)
    ctecn_nombre=db.Column(db.String(52),nullable=False)

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
actividad_trigger=db.DDL(
    f'''
    CREATE OR REPLACE TRIGGER actividadeco_trigger
    BEFORE INSERT ON ge_tactividad_economica
    FOR EACH ROW
    BEGIN
    SELECT ge_sactividad_economica.NEXTVAL INTO :new.acecn_id FROM dual;
    END;
    '''
)
