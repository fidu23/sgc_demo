from flask_restful import Resource, Api

class VistaCliente(Resource):
    def get(self):
        return "hello world"
