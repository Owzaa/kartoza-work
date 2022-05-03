from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """ 
    User Authenticatiion using e-mail account instead of username
    """
    def authenticateobject (self,username=None,password=None) :
        try:
            user = user.object.get(email=username)
            if user.check_password(password) :
                return user
            return None
        except User.DoesNotExist:
            return None 
        
        
    def get_user(self,user_id) :
        try:
            return User.object.get(pk=user_id)
        except User.DoesNotExist:
            return None
               