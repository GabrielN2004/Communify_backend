from flask import Blueprint

from..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp',__name__)

channel_bp.route('/channels', methods = ['GET'])(ChannelController.get_all)
channel_bp.route('/channels/<int:channel_id>', methods = ['GET'])(ChannelController.get)
channel_bp.route('/channels', methods = ['POST'])(ChannelController.create_channel)
channel_bp.route('/channels/<int:channel_id>', methods = ['PUT'])(ChannelController.channel_update)
channel_bp.route('/channels/<int:channel_id>', methods = ['DELETE'])(ChannelController.channel_delete)

