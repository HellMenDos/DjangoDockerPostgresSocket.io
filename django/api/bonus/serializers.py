from .models import Info, Questions, Invation, Bonus, BonusGeneral, RelationBonus
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


class InvationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invation
        fields = '__all__'
        depth = 1


class RelationBonusSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelationBonus
        fields = '__all__'

    def create(self, validated_data):
        return RelationBonus.objects.create(**validated_data)


class RelationBonusListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelationBonus
        fields = '__all__'
        depth = 1


class BonusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bonus
        fields = '__all__'
        depth = 1


class BonusGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = BonusGeneral
        fields = '__all__'
