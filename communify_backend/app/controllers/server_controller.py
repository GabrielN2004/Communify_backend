from ..models.server_model import Servers 
from flask import request, jsonify, sessions

class ServerController :

    @classmethod
    def get_all(cls):
        server_objects = Servers.get_servers()
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200
    
    @classmethod
    def get_user_servers(cls):
        from..models.user_model import Users

        user= Users(user_id= sessions['user_id'])
        servers=[]
        for server in Servers.get(user):
            servers.append(server.serialize())
        return servers, 200
    
    @classmethod
    def get(cls, server_id):
        server = Servers.get_server(server_id)
        if server is not None:
            return jsonify(server),200
        else:
            return {'message':'Server Not Found'},404
        
    @classmethod
    def create_server(cls):
        server = Servers(
            server_name= request.args.get('sever_name', ''),
            server_description= request.args.get('server_description','')
        )
        Servers.create_server(server)
        return {'message': 'Server created successfully'},200
    
    @classmethod
    def update_server(cls, server_id):
        pass

    @classmethod
    def server_delete(cls, server_id):
        server_obj = Servers(server_id=server_id)
        Servers.server_delete(server_obj)
        return {'message': 'Server deleted successfully'},200
    
    @classmethod
    def get_users_servers(cls, server):
         server_objects = Servers.get_users_servers(server)
         servers = []
         for server in server_objects:
            servers.append(server.serialize())
         return servers, 200
    