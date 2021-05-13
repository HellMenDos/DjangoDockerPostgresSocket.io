from .models import Applications,Messages,Review,Location,Commucate,Proposal
from rest_framework import serializers


class ApplicationsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Applications
        fields = '__all__'
    
    def create(self, validated_data):
        return Applications.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Applications.objects.filter(pk=instance).update(**validated_data)


class ApplicationsSerializerStatus(serializers.ModelSerializer):
    
    class Meta: 
        model = Applications
        fields = ('id','status')
    

    def update(self, instance, validated_data):
        return Applications.objects.filter(pk=instance).update(**validated_data)


class ApplicationsSerializerActive(serializers.ModelSerializer):
    
    class Meta: 
        model = Applications
        fields = ('id','active')
    

    def update(self, instance, validated_data):
        return Applications.objects.filter(pk=instance).update(**validated_data)


class MessagesSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Messages
        fields = '__all__'
    
    def create(self, validated_data):
        return Messages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Messages.objects.filter(pk=instance).update(**validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Review
        fields = '__all__'
    
    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Review.objects.filter(pk=instance).update(**validated_data)


class ProposalSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Proposal
        fields = '__all__'
    
    def create(self, validated_data):
        return Proposal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Proposal.objects.filter(pk=instance).update(**validated_data)


class LocationSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Location
        fields = '__all__'

class CommucateSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Commucate
        fields = '__all__'
    
    def create(self, validated_data):
        return Review.objects.create(**validated_data)