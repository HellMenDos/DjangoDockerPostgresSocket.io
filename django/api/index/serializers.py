from .models import UserData, Support, Push, General
from rest_framework import serializers
from django.contrib.auth.admin import User
from djoser.serializers import UserCreateSerializer, TokenCreateSerializer


class MoreDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'

    def create(self, validated_data):
        return UserData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return UserData.objects.filter(pk=instance).update(**validated_data)


class MoreDataUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ('id', 'avatar')

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class MoreDataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'
        depth = 2


class NumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ('id', 'number')

    def create(self, validated_data):
        return UserData.objects.create(**validated_data)


class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = General
        fields = '__all__'


class SupportListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = '__all__'
        depth = 1


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = '__all__'

    def create(self, validated_data):
        return Support.objects.create(**validated_data)


class PushSerializer(serializers.ModelSerializer):

    class Meta:
        model = Push
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    moreData = MoreDataListSerializer()

    class Meta:
        model = User
        fields = ('id','moreData')
        depth = 2

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name')
