from ..database import DatabaseConnection

class Servers:
    def __init__(self, server_id = None, server_name = None, server_description = None):
        self.server_id = server_id
        self.server_name = server_name
        self.server_description = server_description

    def serialize(self):
        return {
            'server_id': self.server_id,
            'server_name': self.server_name,
            'server_description': self.server_description
        }
    
    @classmethod
    def get_servers(cls):
        query = """SELECT * FROM communify.servers ;"""
        results = DatabaseConnection.fetch_all(query)
        server_all = []
        if results is not None:
            for result in results:
                server_all.append(cls(*result))
        return server_all
    
    @classmethod
    def get_server(cls, server_id):
        query = """SELECT * FROM communify.servers WHERE server_id = %s ;"""
        params = (server_id, )
        result = DatabaseConnection.fetch_one(query, params)
        return result
    
    @classmethod
    def create_server(cls, server):
        query = """INSERT INTO communify.servers (server_name, server_description) VALUES (%s, %s) ;"""
        params = (server.server_name, server.server_description)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def server_update(cls, server_id):
        pass

    @classmethod
    def server_delete(cls, server):
        query = """DELETE FROM communify.servers WHERE server_id = %s ;"""
        params = (server.server_id,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Server eliminado'},204
    
    @classmethod
    def get_users_servers(cls, server):
        query = """SELECT users.user_id, users.user_name, users.user_lastname, users.user_nickname, users.user_email, users.user_birthday, users.user_profile_img, servers.server_id, servers.server_name
        FROM servers
        INNER JOIN users ON users.user_id = servers.user_id
        WHERE servers.server_id = %s"""
        params = (server.__dict__)
        results = DatabaseConnection.fetch_all(query, params=params)
        users = []
        from .user_model import Users
        for result in results:
            users.append(Users(*result))
        return users
    
    