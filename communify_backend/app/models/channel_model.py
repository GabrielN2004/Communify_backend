from ..database import DatabaseConnection

class Channels:
    def __init__(self, channel_id = None, channel_name = None, channel_description = None, server_id = None):
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.channel_description = channel_description
        self.server_id = server_id

    def serialize(self):
            return{
                'channel_id': self.channel_id,
                'channel_name': self.channel_name,
                'channel_description': self.channel_description,
                'server_id': self.server_id
            }
    @classmethod
    def get_channels(cls):
         query = """SELECT * FROM communify.channels ;"""
         results = DatabaseConnection.fetch_all(query)
         channel_all = []
         if results is not None:
              for result in results:
                   channel_all.append(cls(*result))
         return channel_all
    
    @classmethod
    def get_channel(cls, channel_id):
         query = """SELECT * FROM communify.channels WHERE channel_id = %s ; """
         params = (channel_id, )
         result = DatabaseConnection.fetch_one(query, params)
         return result
    
    @classmethod
    def create_channel(cls, channel):
         query = """INSERT INTO communify.channels (channel_name, channel_description, server_id) VALUES (%s, %s, %s);"""
         params = (channel.channel_name, channel.channel_description, channel.server_id)
         DatabaseConnection.execute_query(query, params)
     
    @classmethod
    def channel_update(cls, channel_id):
        query = """UPDATE communify.channels SET channel_name = %s, channel_description = %s, server_id = %s, WHERE channel_id = %s ;"""
        params = (channel_id,)
        result = DatabaseConnection.execute_query(query, params=params)
        if result is not None:
             return Channels(
                  channel_id= channel_id,
                  channel_name= result[0],
                  channel_description=result[1],
                  server_id= result[2]
             )
        else:
             return None
    
    @classmethod
    def channel_delete(cls, channel):
        query = "DELETE FROM communify.channels WHERE channel_id = %s"
        params = (channel.channel_id,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Canal borrado con exito'},204

     

         
         
         
         
