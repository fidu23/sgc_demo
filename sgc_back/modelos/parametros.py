from . import db



class TipoPersona(db.Model):
    __tablename__="ge_ttipopersona"
    tper_tipo = db.Column(db.String(3), primary_key=True)
    tper_nombre=db.Column(db.String(32),nullable=False)
    tper_descripcion=db.Column(db.String(100),nullable=False)

class TipoDocumento(db.Model):
    __tablename__="ge_ttipodocumento"    
    tdoc_documento = db.Column(db.String(30),primary_key=True)    
    tdoc_descripcion = db.Column(db.String(100), nullable=False)
    tdoc_tipopersona = db.Column(db.String(3), db.ForeignKey("ge_ttipopersona.tper_tipo"))

class Paises(db.Model):
    __tablename__="ge_tpais"
    pais_id=db.Column(db.Integer(),primary_key=True)    
    pais_nombre=db.Column(db.String(52),nullable=False)
    pais_codigo_iso=db.Column(db.String(4))
    pais_codigo_dian=db.Column(db.String(6))
    pais_codigo_telf=db.Column(db.String(10))
