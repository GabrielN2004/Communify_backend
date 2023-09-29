from ..models.user_model import Users
from flask import request
from flask import jsonify
from flask import json
from flask import session
class UserController:
    """User controller class"""

    @classmethod
    def get(cls, user_id):
        """Get user by ID"""
        user= Users.get_user(user_id)
        if user is not None:
            return jsonify(user),200
        else:
            return {'message':'User Not Found'},404
        
    
    @classmethod
    def get_all(cls):
        """Get all users"""
        users_objects = Users.get_user_all()
        users = []
        for user in users_objects:
            users.append(user.serialize())
        return users, 200
    
    @classmethod
    def create_user(cls):

        user= Users(
            user_name= request.args.get('user_name',''),
            user_lastname= request.args.get('user_lastname', ''),
            user_nickname= request.args.get('user_nickname', ''),
            user_email= request.args.get('user_email', ''),
            user_password= request.args.get('user_password', ''),
            user_birthday= request.args.get('user_birthday', ''),
            user_profile_img= request.args.get('user_profile_img', '')
        )
        Users.user_create(user)
        return  {'message': 'User created successfully'}, 201
        
    @classmethod
    def update_user(cls, user_id):
        datos = request.json
        user_obj = Users(
                        user_id,
                        user_name= datos.get('user_name', ''),
                        user_lastname= datos.get('user_lastname', ''),
                        user_nickname = datos.get('user_nickname', ''),
                        user_email = datos.get('user_email', ''),
                        user_password = datos.get('user_password', ''),
                        user_birthday = datos.get('user_birthday', ''),
                        user_profile_Img = datos.get('user_profile_img', '')
                        )
        Users.user_update(user_obj)
        return {'message': 'User modificado con exito'},201

    @classmethod
    def user_delete(cls, user_id):
         user_obj = Users(user_id=user_id)
         Users.user_delete(user_obj)
         return {'message': 'User deleted successfully'}, 200
    

    @classmethod
    def login(cls):
        data = request.json
        user = Users(
            user_email= data.get('user_email'),
            user_password= data.get('user_password')

        )
        if Users.is_registered(user):
            session['user'] = data.get('user_email')
            return {'message': 'Sesion Iniciada'}, 200
        return {'message': 'Email o contraseña incorrectos'},401
    
    @classmethod
    def show_profile(cls):
        user_email = session.get('user_email')
        user = Users.get(Users(user_email= user_email))
        if user is None:
            return {'message': 'Usuario no encontrado'},404
        else:
            return user.serialize(), 200
        
    @classmethod
    def logout(cls):
        session.pop('user_email', None)
        return {'message':'Sesion Cerrada'}

    
