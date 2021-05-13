from .models import UserData,Support,Push,General
from rest_framework import serializers

class MoreDataSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = UserData
        fields = '__all__'
    
    def create(self, validated_data):
        return UserData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return UserData.objects.filter(pk=instance).update(**validated_data)

class NumberSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = UserData
        fields = ('id','number')

    def create(self, validated_data):
        return UserData.objects.create(**validated_data)

class GeneralSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = General
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Support
        fields = '__all__'
    
    def create(self, validated_data):
        return UserData.objects.create(**validated_data)


class PushSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Push
        fields = '__all__'
    