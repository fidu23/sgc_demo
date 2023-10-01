from . import db

class Cliente(db.Model):
    __tablename__='cl_tcliente'
    cliente_id=db.Column(db.Integer,primary_key=True)
    
