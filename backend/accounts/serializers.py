from rest_framework import serializers

from .models import CustomUser


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True, required=True,
#     )
#     password2 = serializers.CharField(write_only=True, required=True)
#     email = serializers.EmailField(
#         required=True,

#     )

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'password', 'password2']

#     def validate(self, attrs):
#         # print(f"Password 1: {attrs['password']}")
#         # print(f"Password 2: {attrs['password2']}")
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match"}
#             )
        
#         return attrs
    
#     def validate_email(self, attrs):
#         if CustomUser.objects.filter(email=attrs).first():
#             raise serializers.ValidationError(
#                 {"email": "This email already exists"}
#             )
    
#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#         )

#         user.set_password(validated_data['password'])
#         user.save()

#         return user


# your_app_name/serializers.py

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)  # Ensure email is required

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
