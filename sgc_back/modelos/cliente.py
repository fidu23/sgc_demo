from . import db
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .parametros import TipoDocumentoSchema,TipoDocumento,ActividadEconomicaSchema

#CREATE SEQUENCE cl_scliente START WITH 1 INCREMENT BY 1;
cl_scliente=db.Sequence('cl_scliente')
class Cliente(db.Model):
    __tablename__='cl_tcliente'
    clnte_id=db.Column(db.Integer,cl_scliente,primary_key=True)
    clnte_tpidentif_id=db.Column(db.String(30),db.ForeignKey("ge_ttipodocumento.tdoc_documento"),nullable=False)
    clnte_tpidentif=db.relationship('TipoDocumento',backref='cl_tcliente')
    clnte_nroident=db.Column(db.String(50),nullable=False)
    clnte_estado=db.Column(db.String(10),nullable=False)
    clnte_act_econo_id=db.Column(db.String(20),db.ForeignKey('ge_tactividad_economica.acecn_codigo_ciu'))
    clnte_act_econo=db.relationship('ActividadEconomica',backref='cl_tcliente')
    __table_args__ = (db.UniqueConstraint('clnte_tpidentif_id', 'clnte_nroident', name='uq_clnte_tpidentif_nroident'),)



class ClienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Cliente
        load_instance=True

    clnte_id=fields.String()
    clnte_tpidentif=fields.Nested(TipoDocumentoSchema)
    clnte_act_econo=fields.Nested(ActividadEconomicaSchema)
    
