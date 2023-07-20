from rest_framework import serializers

from users.models import User

#writeonly = quando recebemos dados
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(write_only=True)

    first_name = serializers.CharField(max_length=50)
    last_name= serializers.CharField(max_length=50)
    birthdate=serializers.DateField( default = None)
    is_employee=serializers.BooleanField(default=False)
    is_superuser=serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict)-> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)

     
        return User.objects.create_user(**validated_data)