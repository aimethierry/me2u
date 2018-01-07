from rest_framework import serializers
from .models import compony, users
from django.contrib.auth.models import User

class ComponylistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = users
        fields = ('id', 'first_name', 'last_name', 'amount','compony', )
       

class UserlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    first_name = serializers.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = serializers.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = serializers.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id','username', 'first_name', 'last_name',
                  'email', 'password',  )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ClientSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = compony
        fields = ('id', 'name_of_compony', 'adress', 'location', )
