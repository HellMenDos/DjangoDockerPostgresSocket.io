from .models import Info,Questions,Invation
from rest_framework import serializers


class InfoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Info
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Questions
        fields = '__all__'

class InvationSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Invation
        fields = '__all__'

    def create(self, validated_data):
        return Invation.objects.create(**validated_data)