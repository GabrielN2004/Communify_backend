from ..models.channel_model import Channels
from flask import request, jsonify

class ChannelController:

    @classmethod
    def get_all(cls):
        channel_objects = Channels.get_channels()
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200
    
    @classmethod
    def get(cls, channel_id):
        channel = Channels.get_channel(channel_id)
        if channel is not None:
            return jsonify(channel),200
        else:
            return {'message':'Channel Not Found'},404
        
    @classmethod
    def create_channel(cls):
        channel = Channels(
            channel_name= request.args.get('channel_name', ''),
            channel_description= request.args.get('channel_description', ''),
            server_id= request.args.get('server_id', '')
        )
        Channels.create_channel(channel)
        return {'message': 'Channel created successfully'},200
    
    @classmethod
    def channel_update(cls, channel_id):
        channel_instance = Channels.channel_update(channel_id)
        if channel_instance:
            response_data = {
                'channel_id': channel_instance.channel_id,
                'channel_name': channel_instance.channel_name,
                'channel_description': channel_instance.channel_description,
                'server_id':channel_instance.server_id
            }
            return jsonify(response_data),200
        else:
         return {'message': 'Channel  Not updated successfully'}, 200
    
    @classmethod
    def channel_delete(cls, channel_id):
        channel_obj = Channels(channel_id=channel_id)
        Channels.channel_delete(channel_obj)
        return {'message': 'Channel deleted successfully'}, 200
