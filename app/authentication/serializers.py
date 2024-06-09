from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from app.authentication.models import User
from django.contrib.auth import authenticate

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'picture', 'password']

    def create(self, validated_data):
        hashed_password = make_password(validated_data['password'])
        validated_data['username'] = validated_data['email']
        validated_data['password'] = hashed_password
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'picture', 'phone']

class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance