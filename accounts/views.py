from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class RegisterAPI(generics.GenericAPIView):
    """
    This class creates the API for Registration of a user.

    '''

    Attributes
    ----------
    serializer_class : RegisterSerializer Class's Object
        a variable to attach a specific Serialezer with this API.
    
    Methods
    -------
    post(request, *args, **kwargs)
        creates a token using AUthToekn of the for the user's data, 
        after serializing and valdating it.
    """

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Step 1:
            Gets the serialzed data of the user, entered in frontend 
            of API.
        Step 2:
            Stores that data in 'serialzer' variable and validate it.
        Step 3:
            Saves the 'data' Object (a dictionary) in the variable 
            'user'.
        Step 4:
            Creates a token using 'AuthToken' Model for the data Object
            stored in variable 'user'.

        Parameters
        ----------
        request : DRF HTTP POST Request Object
            data entered by the user on the frontend of the DRF
            REST API.
        *args : Any type, optional
            represents any additional arguments passed of any type.
        **kwargs : Any type, optional
            represents any additional keyword-arguments passed of any
            type.

        Returns
        ------
        Dictionary
            a dictionary holding the values of the keys 'user' and 
            'token'.
        """

        # get_serializer() method uses the keyword argument 'data'
        # which holds the value of 'data' attribute of 'request', a DRF
        # HTTP POST Request Object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "user": user.email,
            "token": token[1]
        })


class LoginAPI(generics.GenericAPIView):
    """
    This class creates the API for Login of a user.

    '''

    Attributes
    ----------
    serializer_class : LoginSerializer Class's Object
        a variable to attach a specific Serialezer with this API.
    
    Methods
    -------
    post(request, *args, **kwargs)
        stores the user's data after serializing and validating it.
    """

    serializer_class = LoginSerializer

    def post(self, request):
        """
        Step 1:
            Gets the serialzed data of the user, entered in frontend 
            of API.
        Step 2:
            Stores that data in 'serialzer' variable and validate it.
        Step 3:
            Saves the validated 'data' Object (a dictionary) in the 
            variable 'user'.

        Parameters
        ----------
        request : DRF HTTP POST Request Object
            data entered by the user on the frontend of the DRF
            REST API.

        Returns
        ------
        Dictionary
            a dictionary holding the values of the keys 'token' and 
            'user_id'.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "token": AuthToken.objects.create(user)[1],
            "user_id": user.id
        })


class UserAPI(generics.RetrieveAPIView):
    """
    This class creates the API for User.

    '''

    Attributes
    ----------
    permission_classes : list
        a list to define who should have access to this API
    serializer_class : UserSerializer Class's Object
        a variable to attach a specific Serialezer with this API
    
    Methods
    -------
    get_object()
        returns value stored in 'user' key of 'request', a DRF HTTP
        POST Object (a dictionary).
    """

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        """
        Returns value stored in 'user' key of 'request', a DRF HTTP
        POST Object (a dictionary).

        Returns
        ------
        Dictionary
            a dictionary holding the values of the details of a user.
        """

        return self.request.user