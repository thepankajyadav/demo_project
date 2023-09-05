from rest_framework import serializers
from .models import User, UserMeta
from django.contrib.auth import get_user_model

class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMeta
        fields = ('dob', 'country', 'zip_code')

class UserSerializer(serializers.ModelSerializer):
    usermeta = UserMetaSerializer()
    # We are writing this because we need confirm password field in our Registratin Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields=('email', 'name', 'password', 'password2', 'usermeta')
        # fields = ('name', 'email', 'usermeta')
        extra_kwargs={
            'password':{'write_only':True}
        }

    # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        print('password1', password)
        print('password1', password2)
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        usermeta_data = validated_data.pop('usermeta')
        # user = User.objects.create(**validated_data)
        user = User.objects.create_user(**validated_data)
        UserMeta.objects.create(user=user, **usermeta_data)
        return user