from..controllers.message_controller import MessageController
from flask import Blueprint

message_bp = Blueprint('message_bp', __name__)

message_bp.route('/messages', methods = ['GET'])(MessageController.get_all)
message_bp.route('/messages/<int:message_id>', methods = ['GET'])(MessageController.get)
message_bp.route('/messages', methods = ['POST'])(MessageController.create_message)
message_bp.route('/messages/<int:message_id>/<int:user_id>', methods = ['PUT'])(MessageController.update_message)
message_bp.route('/messages/<int:message_id>/<int:user_id>', methods = ['DELETE'])(MessageController.update_message)