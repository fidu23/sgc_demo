from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

from .parametros import *
from .cliente import *


triggers=[
    pais_trigger,
    ciudad_trigger,
    departamento_trigger,
    trigger_cliente,
]