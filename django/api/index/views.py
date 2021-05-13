from rest_framework import generics, status,permissions
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import MoreDataSerializer,NumberSerializer,SupportSerializer,PushSerializer,GeneralSerializer
from bonus.serializers import InvationSerializer
from .models import UserData,Support,Push,General
from django.contrib.auth.admin import User
from django.contrib.auth.models import Group
from twilio.rest import Client
import random
import string
import requests
from django.conf import settings
import random
import string

class MoreData(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self,request):
        """ 
        Здесь можно обновить любые данные, самое главное в теле запроса иметь id, 
        а остальноное можно компоновать как захочется, то есть {id:1,location:'Livia'} или {id:1,vk:'token'}
        """
        data = MoreDataSerializer(UserData.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        if data.is_valid():
            data.save()
        return Response(data=data.save())

    def post(self,request):
        """
        Создание допольнительных полей для пользователя (обязательный номер телефона)
        ! Надо создавать сразу же после регстрации !
        """
        hashurl = ''.join(random.choice(string.ascii_uppercase) for i in range(7))
        data = MoreDataSerializer(data=request.data)
        invite = InvationSerializer(data={'user':request.data['user'],'hashurl':hashurl})
        if data.is_valid():
            if invite.is_valid():
                invite.save()
                data.save()
        return Response(status=201)

class GetDataFromVk(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,token):
        user = UserData.objects.filter(vk=token).first()
        if user:
            data = {"username":user.user.username,"password":user.user.password}
        else:
            data = {'status':'empty'}
        return Response(data=data)

class GetDataFromGoogle(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,token):
        user = UserData.objects.filter(google=token).first()
        if user:
            data = {"username":user.user.username,"password":user.user.password}
        else:
            data = {'status':'empty'}
        return Response(data=data)

class GetDataFromApple(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,token):
        user = UserData.objects.filter(appleId=token).first()
        if user:
            data = {"username":user.user.username,"password":user.user.password}
        else:
            data = {'status':'empty'}
        return Response(data=data)
        

class GetDataFromFacebook(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,token):
        user = UserData.objects.filter(facebook=token).first()
        if user:
            data = {"username":user.user.username,"password":user.user.password}
        else:
            data = {'status':'empty'}
        return Response(data=data)

class OneUserData(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,num):
        user = UserData.objects.get(pk=num)
        data = MoreDataSerializer(user)
        return Response(data=data.data)


class ChangeGroup(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def get(self,request,name,userId):
        """
        Добавление группы для пользователя, можно добавить группу компания к любому зарегестрированному пользователю
        """
        res = Group.objects.filter(name=name)[0]
        user = User.objects.get(id=userId)
        user.groups.add(res)
        return Response(status=["success"])

class ChangePassword(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = NumberSerializer

    def post(self,request):
        """ Изменение пароля по номеру телефонв единственный параметр номер телефона """
        userData = UserData.objects.filter(number=request.data['number']).first()
        password  = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        userData.user.set_password(password)
        userData.user.save()

        account_sid = settings.ACCOUNT_ID
        auth_token  = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Your new password - '+password,
            to=request.data['number'],
            from_="+18043312662")
        return Response(status=201)

# Activate your account
def activate(request,uid,token):
    res = requests.post('http://127.0.0.1:8080/auth/users/activation/', data={'uid':uid,'token':token})
    return HttpResponse('ok')


class SupportConf(generics.ListCreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        """ Здесь можно обновить любые данные, самое главное в теле запроса иметь id, 
        а остальноное можно компоновать как захочется"""
        data = SupportSerializer(Support.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = 'success'
        else:
            status = 'fail'
        return Response(data=[status])
    
    def delete(self,request):
        """ Едиственный параметр id """
        deal = Support.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=['success'])

class PushConf(generics.ListAPIView):
    queryset = Push.objects.all()
    serializer_class = PushSerializer

class GeneralConf(generics.ListAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    permission_classes = [permissions.IsAuthenticated]
