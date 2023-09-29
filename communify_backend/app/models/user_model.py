from ..database import DatabaseConnection

class Users:
    """User model class"""

    def __init__(self, user_id = None, 
                 user_name = None, 
                 user_lastname = None,
                 user_nickname = None, 
                 user_email = None,
                 user_password = None,
                 user_birthday = None,
                 user_profile_img = None):
        
        """Contructor Metodo"""
        self.user_id = user_id
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_nickname = user_nickname
        self.user_email = user_email
        self.user_password = user_password
        self.user_birthday = user_birthday
        self.user_profile_img = user_profile_img
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_lastname": self.user_lastname,
            "user_nickname": self.user_nickname,
            "user_email": self.user_email,
            "user_password": self.user_password,
            "user_birthday": self.user_birthday,
            "user_profile_Img" : self.user_profile_img
        }

    @classmethod
    def get_user_all(cls):
        """Obtiene todo los usuarios de la Databases"""
        query = """SELECT * FROM communify.users """
        results = DatabaseConnection.fetch_all(query)

        users = []

        if results is not None:
                for result in results:
                    users.append(cls(*result))
        return users


    @classmethod
    def get_user(cls, user_id):
        """Obtiene todos los datos del usuario filtrandolo por si ID"""
        query = """SELECT * FROM communify.users where user_id = %s;"""
        params = (user_id, )
        result = DatabaseConnection.fetch_one(query,params)
        return result

    @classmethod
    def user_create (cls, user):
        query = "INSERT INTO communify.users (user_name, user_lastname, user_nickname, user_email, user_password, user_birthday, user_profile_img) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        params = (user.user_name, user.user_lastname, user.user_nickname, user.user_email, user.user_password, user.user_birthday, user.user_profile_img)
        DatabaseConnection.execute_query(query, params=params)
            
    @classmethod
    def user_update(cls, user):
        query = "UPDATE communify.users SET user_name = %s, user_lastname = %s, user_nickname = %s, user_email = %s, user_password = %s, user_birthday = %s, user_profile_img = %s WHERE user_id = %s ;"
        params = (user.user_name, user.user_lastname, user.user_nickname, user.user_email, user.user_password, user.user_birthday, user.user_profile_img)
        DatabaseConnection.execute_query(query, params)
        return None
    
    @classmethod
    def user_delete(cls, user):
        query = "DELETE FROM communify.users WHERE user_id = %s;"
        params = (user.user_id,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Usuario borrado con exito'},204


    @classmethod
    def is_registered(cls, user):
        query = """SELECT user_id FROM communify.users WHERE user_email = %s and user_password =%s;"""
        params = (user.user_email, user.user_password)
        result = DatabaseConnection.fetch_one(query, params= params)

        if result is not None:
            return True
        return False

