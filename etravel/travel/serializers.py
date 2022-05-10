from rest_framework.serializers import ModelSerializer
from .models import Ride, Port, User


class PortSerializer(ModelSerializer):
    class Meta:
        model = Port
        fields = ['id', 'name', 'address']


class RideSerializer(ModelSerializer):
    ports = PortSerializer(many=True)

    class Meta:
        model = Ride
        fields = '__all__'


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
