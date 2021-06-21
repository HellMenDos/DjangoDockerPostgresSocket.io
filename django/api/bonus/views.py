from django.shortcuts import render
from .models import Info, Questions, Invation, Bonus, RelationBonus, BonusGeneral
from .serializers import InfoSerializer, InvationListSerializer, QuestionsSerializer, InvationSerializer, BonusGeneralSerializer, BonusSerializer, RelationBonusListSerializer, RelationBonusSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import redirect,render
from index.models import General
from conversation.models import Location
from conversation.serializers import LocationSerializer


class InfoConf(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class QuestionsConf(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

# For google play


class Play(generics.ListAPIView):
    queryset = Invation.objects.all()
    serializer_class = InvationSerializer

    def get(self, request, hashurl):
        inv = Invation.objects.filter(hashurl=hashurl).first()
        url = General.objects.all()[0]
        if inv:
            inv.count += 1
            inv.save()
            return redirect(url.PlayMarket)
        else:
            return Response(data=["Ошибка токена"])

# For app store
class Inv(generics.ListAPIView):
    queryset = Invation.objects.all()
    serializer_class = InvationSerializer

    def get(self, request, hashurl):
        inv = Invation.objects.filter(hashurl=hashurl).first()
        url = General.objects.all()[0] 
        if inv:
            inv.count += 1
            inv.save()
            data = {'android': url.PlayMarket, 'ios': url.AppStore}
            return render(request, "index.html", context=data)
        else:
            return Response(data=["Ошибка токена"])

class Appst(generics.ListAPIView):
    queryset = Invation.objects.all()
    serializer_class = InvationSerializer

    def get(self, request, hashurl):
        inv = Invation.objects.filter(hashurl=hashurl).first()
        url = General.objects.all()[0]
        if inv:
            inv.count += 1
            inv.save()
            return redirect(url.AppStore)
        else:
            return Response(data=["Ошибка токена"])


class InvationConfgetOne(generics.ListAPIView):
    queryset = Invation.objects.all()
    serializer_class = InvationListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        """ 
        НУЖЕН ТОКЕН
        Получение данных по реферальной ссылке """
        inv = Invation.objects.filter(user=num).first()
        data = InvationListSerializer(inv)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class BonusRelationInsert(generics.ListCreateAPIView):
    queryset = RelationBonus.objects.all()
    serializer_class = RelationBonusSerializer
    permission_classes = [permissions.IsAuthenticated]


class BonusRelation(generics.ListAPIView):
    queryset = RelationBonus.objects.all()
    serializer_class = RelationBonusListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение всех бонусов по id пользователя '''
        bonus = RelationBonus.objects.filter(user=num)
        data = RelationBonusListSerializer(bonus, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class BonusGetRelation(generics.ListAPIView):
    queryset = RelationBonus.objects.all()
    serializer_class = RelationBonusListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение пользователей с указанным бонусом'''
        bonus = RelationBonus.objects.filter(bonus=num)
        data = RelationBonusListSerializer(bonus, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class BonusGet(generics.ListAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

    def get(self, request, slug, us):
        ''' 
        Получение бонусов по местоположению us=True/False'''
        bonus = Bonus.objects.filter(
            location__title__startswith=slug, forUser=us)
        data = BonusSerializer(bonus, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class BonusGetWithLevel(generics.ListAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

    def get(self, request, num, us):
        ''' Получение бонуса по уровню бонусной системы us=True/False '''
        bonus = Bonus.objects.filter(level=num, forUser=us)
        data = BonusSerializer(bonus, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class BonusGeneralWithLevel(generics.ListAPIView):
    queryset = BonusGeneral.objects.all()
    serializer_class = BonusGeneralSerializer

    def get(self, request, num, us):
        ''' Получение Уровня бонусной системы по индетификатору us=True/False '''
        bonus = BonusGeneral.objects.filter(level=num, forUser=us)
        data = BonusGeneralSerializer(bonus, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class BonusGeneralGet(generics.ListAPIView):
    queryset = BonusGeneral.objects.all()
    serializer_class = BonusGeneralSerializer

    def get(self, request, us):
        ''' Получение Уровня бонусной системы по индетификатору для пользователя us=True/Fals'''
        bonus = BonusGeneral.objects.filter(forUser=us)
        data = BonusGeneralSerializer(bonus, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)
