from .models import Applications, Messages, Review, Location, Commucate, Proposal, Typeof
from rest_framework import serializers
from index.serializers import MoreDataSerializer


class TypeofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeof
        fields = '__all__'

    def create(self, validated_data):
        return Typeof.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Typeof.objects.filter(pk=instance).update(**validated_data)


class ApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = '__all__'

    def create(self, validated_data):
        types = validated_data.pop('typeOf')
        appl = Applications.objects.create(**validated_data)
        appl.typeOf.add(*types)
        return appl

    def update(self, instance, validated_data):
        if 'typeOf' in validated_data:
            types = validated_data.pop('typeOf')
            instance[0].typeOf.set(types)

        return instance.update(**validated_data)


class UpdatePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = ('id', 'photo')

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


class ApplicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'
        depth = 1


class ApplicationsSerializerStatus(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = ('id', 'status')

    def update(self, instance, validated_data):
        return Applications.objects.filter(pk=instance).update(**validated_data)


class ApplicationsSerializerActive(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = ('id', 'active')

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


class MessagesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = '__all__'
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Review.objects.filter(pk=instance).update(**validated_data)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        depth = 1


class ProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = '__all__'

    def create(self, validated_data):
        return Proposal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Proposal.objects.filter(pk=instance).update(**validated_data)


class ProposalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = '__all__'
        depth = 1


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

    def create(self, validated_data):
        return Location.objects.create(**validated_data)


class CommucateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commucate
        fields = '__all__'

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


class CommucateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commucate
        fields = '__all__'
        depth = 1
