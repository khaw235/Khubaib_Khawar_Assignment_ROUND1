from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    This class creates a Serializer to serialize the data of a user.

    '''

    Attributes
    ----------
    Meta : user defined type
        a type/class to define the meta-data of this specific 
        Serializer.
    """

    class Meta:
        """
        This class define the meta-data of a Serializer.

        '''

        Attributes
        ----------
        model : User Class's Object
            a variable to attach specific Model with this Serializer.
        fields : tuple
            a tuple that holds the names of fields of User Model to be
            used in this Serializer.
        """

        model = User
        fields = ('username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    """
    This class creates a Serializer to serialize the data of a user
    taken from frontend of the registration page.

    '''

    Attributes
    ----------
    Meta : user defined type
        a type/class to define the meta-data of this specific
        Serializer.
    
    Methods
    -------
    create(validated_data)
        stores the instance of User Class in 'user' variable, after 
        creating the latter, based on the 'validated_data' variable.
    """

    class Meta:
        """
        This class define the meta-data of a Serializer.

        '''

        Attributes
        ----------
        model : User Class's Object
            a variable to attach specific Model with this Serializer.
        fields : tuple
            a tuple to hold the names of fields of User Model to be
            used in this Serializer.
        extra_kwargs : dictionary
            a dictionary to define the 'write-only' attribute of
            'password' field as 'True'.
        """

        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Stores the instance of User Class in 'user' variable, after 
        creating the latter, based on the 'validated_data' variable.

        Returns
        ------
        Instance/Object of User Model/Class
            an instance of the 'User' Model/Class containing all the
            fields/attributes of a 'User Model/Class.
        """

        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user


class LoginSerializer(serializers.Serializer):
    """
    This class creates a Serializer to serialize the data of a user
    taken from frontend of the login page.

    '''

    Attributes
    ----------
    email : Serializers' EmailField Class's Object
        a variable to create an email input field on the frontend.
    password : Serializers' CharField Class's Object
        a variable to create a character input field on the frontend.
    
    Methods
    -------
    validate(data)
        authenticates the data posted from the frontend login page, and
        stores the data in 'user' variable.
    """

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Authenticates the data posted from the frontend login page, and
        stores the data in 'user' variable.

        Raises
        ------
        ValidationError
            if its not the case that user is authenticated and user is 
            active.

        Returns
        -------
        An Instance/Object of User Model/Class (Dictionary)
            a dictinoary holding the values/fields of the data of an
            Instance/Object of User Model/Class.
        """
        user = authenticate(**{
            'username': data['email'],
            'password': data['password']
        })

        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')