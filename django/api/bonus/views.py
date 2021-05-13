from django.shortcuts import render
from .models import Info,Questions,Invation
from .serializers import InfoSerializer,QuestionsSerializer,InvationSerializer
from rest_framework import generics, status,permissions
from rest_framework.response import Response
from django.shortcuts import redirect
from index.models import General

class InfoConf(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class QuestionsConf(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class InvationConf(generics.ListAPIView):
    queryset = Invation.objects.all()
    serializer_class = InvationSerializer

    def get(self,request,hashurl):
        inv = Invation.objects.filter(hashurl=hashurl).first()
        url = General.objects.get(pk=1)
        if inv:   
            inv.count += 1
            inv.save()
            return redirect(url.appUrl)
        else:
            return Response(data=['Ошибка токена'])

class InvationConfgetOne(generics.ListAPIView):
    queryset = Invation.objects.all()
    serializer_class = InvationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,num):
        """ Получение данных по реферальной ссылке """
        inv = Invation.objects.filter(user=num).first()
        data = InvationSerializer(inv)
        return Response(data=data.data)
    
