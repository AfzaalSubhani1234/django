from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        models=User
        fields=["email",
               "full_name",
               "password",
                "role"]

        
    def create(self,validate_data):
        user=User.objects.create_user(
            email=validate_data['email'],
            full_name=validate_data['full_name'],
            password=validate_data['password'],
            role=validate_data['role']


        )
        return user