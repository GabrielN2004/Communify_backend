from flask import Blueprint
from..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/servers', methods = ['GET'])(ServerController.get_all)
server_bp.route('/servers/<int:server_id>', methods = ['GET'])(ServerController.get)
server_bp.route('/servers', methods = ['POST'])(ServerController.create_server)
server_bp.route('/servers/<int:server_id>', methods = ['PUT'])(ServerController.update_server)
server_bp.route('/servers/<int:server_id>', methods = ['DELETE'])(ServerController.server_delete)
server_bp.route('/user_servers/<int:server_id>', methods = ['GET'])(ServerController.get_users_servers)
