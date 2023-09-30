from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Cliente(db.Model):
    __tablename__='CL_TCLIENTE'
    cliente_id=db.Column(db.Integer,primary_key=True)
