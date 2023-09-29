from..models.message_model import Messages
from flask import request, jsonify

class MessageController:
    @classmethod
    def get_all(cls):
        messsage_obj = Messages.get_messages()
        messages = []
        for message in messsage_obj:
            messages.append(message.serialize())
        return messages, 200
    
    @classmethod
    def get(cls, message_id):
        message = Messages.get_message(message_id)
        if message is not None:
            return jsonify(message),200
        else:
            return {'message':'Message Not Found'},404
        
    @classmethod
    def create_message(cls):
        message = Messages(
            message_content= request.args.get('message_content', ''),
            message_history= request.args.get('message_history', ''),
            user_id= request.args.get('user_id', ''),
            channel_id= request.args.get('channel_id', '')
        )
        Messages.create_message(message)
        return {'message': 'Message created successfuly'},200
    
    @classmethod
    def update_message(cls, message_id, user_id):
        pass


    @classmethod
    def delete_message(cls, message_id, user_id):
        message_obj = Messages(message_id=message_id, user_id=user_id)
        Messages.delete_message(message_obj)
        return {'message': 'Message deleted successfuly'},200
    
