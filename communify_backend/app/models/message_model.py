from..database import DatabaseConnection

class Messages:
    def __init__(self, message_id = None, message_content = None, message_history = None, user_id = None, channel_id = None):
        self.message_id = message_id
        self.message_content = message_content
        self.message_history = message_history
        self.user_id = user_id
        self.channel_id = channel_id

    def serialize(self):
        return {
            'message_id': self.message_id,
            'message_content': self.message_content,
            'message_history': self.message_history,
            'user_id': self.user_id,
            'server_id': self.channel_id
        }
    
    @classmethod
    def get_messages(cls):
        query = """SELECT * FROM communify.messages ;"""
        results = DatabaseConnection.fetch_all(query)
        message_all = []
        if results is not None:
            for result in results:
                message_all.append(cls(*result))
        return message_all
    
    @classmethod
    def get_message(cls, message_id):
         query = """SELECT * FROM communify.messages WHERE message_id = %s ;"""
         params = (message_id, )
         result = DatabaseConnection.fetch_one(query, params)
         return result
    
    @classmethod
    def create_message(cls, message):
        query = """INSERT INTO communify.messages (message_content, message_history, user_id, channel_id) VALUES (%s, %s, %s, %s)"""
        params = (message.message_content, message.message_history, message.user_id, message.channel_id)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update_message(cls, user_id):
        pass

    @classmethod
    def delete_message(cls, message_id, user_id):
        query = "DELETE FROM communify.messages WHERE message_id = %s and user_id = %s ;"
        params = (message_id, user_id)
        DatabaseConnection.execute_query(query,params)
        return {'message': 'Mensaje borrado con exito'},204





