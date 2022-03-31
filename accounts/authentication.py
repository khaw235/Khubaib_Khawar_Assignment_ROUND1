from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CustomEmailBackend(ModelBackend):
    """
    This class creates a custom backend model for user authentication.

    '''

    Methods
    -------
    authenticate(username=None, password=None, **kwargs)
        authenticates the user based on both email and username.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        """
        Authenticates the 'User' Class/Model Object, based on both
        fields email and username.

        Parameters
        ----------
        username : str, optional
            a string holding the value of the username/email of a user.
        password : str, optional
            a string holding the value of the password of a user.

        Returns
        ------
        An Instance/Object of User Class/Model (Dictionary)
            returns an Instance/Object of User Model/Class (Dictionary),
            holding the values of user's data, if it exists.
        None
            returns None otherwise.
        """

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None