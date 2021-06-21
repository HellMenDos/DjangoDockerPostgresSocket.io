from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, QueryDict
from .serializers import MoreDataListSerializer, MoreDataSerializer, MoreDataUpdateSerializer, NumberSerializer, SupportSerializer, PushSerializer, GeneralSerializer, UserSerializer
from bonus.serializers import InvationSerializer
from conversation.models import Location
from conversation.serializers import LocationSerializer
from .models import UserData, Support, Push, General
from django.contrib.auth.admin import User
from django.contrib.auth.models import Group
from twilio.rest import Client
import random
import string
import requests
from django.conf import settings
import random
import string
from django.shortcuts import redirect, render

# Login with number


class LoginWithNumber(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def post(self, request):
        """ Передача двух значений number и password и
        возвращением jwt токена """
        data = UserData.objects.filter(
            number=request.data['number']).first().user.email

        user = requests.post('http://127.0.0.1:8080/auth/token/login/', data={
            'email': data,
            'password': request.data['password']
        })
        json = user.json()

        return Response(data=json)

# Update additional fields


class MoreDataUpdatePhoto(generics.UpdateAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        data = MoreDataUpdateSerializer(UserData.objects.get(
            pk=request.data['id']), data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = {'status': 'success'}
        else:
            status = {'status': 'Ошибка при введении данных'}
        return Response(data=[status])


class MoreDataUpdate(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        """
        НУЖЕН ТОКЕН
        Здесь можно обновить любые данные, самое главное в теле запроса иметь id,
        а остальноное можно компоновать как захочется, то есть {id:1,location:'Livia'} или {id:1,vk:'token'}
        """
        req = QueryDict('', mutable=True)
        req.update(request.data)

        if req.__contains__('location'):
            loc = Location.objects.filter(
                title=request.data['location']).first()

            if loc:
                req.update({'location': LocationSerializer(loc).data['id']})
            else:
                locactionSerial = LocationSerializer(
                    data={'title': req.get('location')})
                if locactionSerial.is_valid():
                    locactionSerial.save()
                    req.update({'location': locactionSerial.data['id']})

        data = MoreDataSerializer(UserData.objects.get(
            pk=request.data['id']).id, data=req, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = {'status': 'success'}
        else:
            status = {'status': 'Ошибка при введении данных'}
        return Response(data=status)

# Creating additional fields for the
# user with the creation of an invitation link


class MoreData(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def post(self, request):
        """
        Создание допольнительных полей для пользователя (обязательный номер телефона)
        ! Надо создавать сразу же после регстрации !
        """
        hashurl = ''.join(random.choice(string.ascii_uppercase)
                          for i in range(7))
        req = QueryDict('', mutable=True)
        req.update(request.data)

        if 'location' in request.data:
            loc = Location.objects.filter(
                title=request.data['location']).first()
            if loc:
                req.update({'location': LocationSerializer(loc).data['id']})
            else:
                locactionSerial = LocationSerializer(
                    data={'title': req.get('location')})
                if locactionSerial.is_valid():
                    locactionSerial.save()
                    req.update({'location': locactionSerial.data['id']})

        data = MoreDataSerializer(data=req)
        invite = InvationSerializer(
            data={'user': req.get('user'), 'hashurl': hashurl})
        if data.is_valid():
            if invite.is_valid():
                invite.save()
                data.save()
        return Response(data=data.data)

# Get all additional fields for user


class OneUserData(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        '''
        НУЖЕН ТОКЕН
        Получение допольнительных полей по номеру пользователя'''
        user = UserData.objects.filter(user=num).first()
        data = MoreDataListSerializer(user)
        if data:
            response = data.data
        return Response(data=response)

# Change user group


class ChangeGroup(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name, userId):
        """
        НУЖЕН ТОКЕН
        Добавление группы для пользователя, можно добавить группу компания к любому зарегестрированному пользователю
        """
        res = Group.objects.filter(name=name)[0]
        user = User.objects.get(id=userId)
        if user:
            user.groups.add(res)
        return Response(status=201)

# Get With name of company, username and location


class GetCompanyWithLocation(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name, username, location):
        '''
        НУЖЕН ТОКЕН
        Получение компаний по имени и по локации '''
        users = Group.objects.get(name=name).user_set.filter(
            username__startswith=username, moreData__location__title__startswith=location, is_staff=True)
        data = UserSerializer(users, many=True)
        if data:
            response = data.data
        return Response(data=response)

# Get company with name of group and
# name what is similar to name


class GetCompany(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name, username):
        '''
        НУЖЕН ТОКЕН
        Получение компений по имени '''
        users = Group.objects.get(name=name).user_set.filter(
            username__startswith=username, is_staff=True)
        data = UserSerializer(users, many=True)
        if data:
            response = data.data
        return Response(data=response)


# Get comapny with location
class GetCompanyLocationId(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name, location):
        '''
        НУЖЕН ТОКЕН
        Получение компений по имени '''
        users = Group.objects.get(name=name).user_set.filter(
            moreData__location=location, is_staff=True)
        data = UserSerializer(users, many=True)
        if data:
            response = data.data
        return Response(data=response)


# Get All companys with name of group
# Only Get method


class GetAllCompanys(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        '''
        НУЖЕН ТОКЕН
        Получение компений по имени '''
        users = Group.objects.get(name=name).user_set.filter(is_staff=True)
        data = UserSerializer(users, many=True)
        if data:
            response = data.data
        return Response(data=response)


# Change password with sms
# Only post method, what change user password
class ChangePassword(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = NumberSerializer

    def post(self, request):
        """ Изменение пароля по номеру телефонв единственный параметр номер телефона """
        userData = UserData.objects.filter(
            number=request.data['number']).first()
        if userData:
            password = ''.join(random.choice(string.ascii_letters)
                               for _ in range(6))
            userData.user.set_password(password)
            userData.user.save()

            account_sid = getattr(settings, "ACCOUNT_ID", None)
            auth_token = getattr(settings, "AUTH_TOKEN", None)
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body='Your new password - '+password,
                to=request.data['number'],
                from_="+18043312662")
            return Response(status=201)
        else:
            return Response(data={'error': 'Такого пользователя не существует'})

# Activate your account


def activate(request, uid, token):
    res = requests.post(
        'http://127.0.0.1:8080/auth/users/activation/', data={'uid': uid, 'token': token})
    if res.status_code == 400:
        return HttpResponse('Ошибка, неверный токен')
    else:
        links = General.objects.all()[0]
        data = {'android': links.PlayMarket, 'ios': links.AppStore}
        return render(request, "index.html", context=data)

# Send request to create support ticket


class SupportConf(generics.CreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer


# Get Push rows
class PushConf(generics.ListAPIView):
    queryset = Push.objects.all()
    serializer_class = PushSerializer


class PushSend(generics.ListAPIView):
    queryset = Push.objects.all()
    serializer_class = PushSerializer

    def get(self, request):
        allPush = Push.objects.all()
        serilizerData = PushSerializer(allPush, many=True)
        for i in range(len(serilizerData.data)):
            print(i)
        return Response(data=[len(serilizerData.data)])

# Get general information about app


class GeneralConf(generics.ListAPIView):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    permission_classes = [permissions.IsAuthenticated]

#
# Social registration
# 1. VK
# 2. Google
# 3. appleID
# 4. Facebook
#


class GetDataFromVk(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def post(self, request):
        ''' Вход по токену соцсети с придумыванием пароля, если токен есть возвращаются данные, если нет создается пользователь
        с введенными данными которые сопровождают запрос (так же нужно указывать пароль) '''
        userData = UserData.objects.filter(vk=request.data['token']).first()
        if userData:
            moreData = userData.user.email
            user = requests.post('http://127.0.0.1:8080/auth/token/login/', data={
                'email': moreData,
                'password': request.data['password']
            })
            data = user.json()

        else:
            user = requests.post('http://127.0.0.1:8080/auth/users/', data={
                'username': request.data['email'].split('@')[0],
                'email': request.data['email'],
                'password': request.data['password'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name']
            })

            if user.status_code == 201:
                moreData = requests.post('http://127.0.0.1:8080/auth/get/more/', data={
                    'user': user.json()['id'],
                    'number': request.data['number'],
                    'location': request.data['location'],
                    'vk': request.data['token']
                })
                data = moreData.json()
            else:
                data = user.json()

        return Response(data=data)


class GetDataFromGoogle(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def post(self, request):
        ''' Вход по токену соцсети с придумыванием пароля, если токен есть возвращаются данные, если нет создается пользователь
        с введенными данными которые сопровождают запрос (так же нужно указывать пароль) '''
        userData = UserData.objects.filter(
            google=request.data['token']).first()
        if userData:
            moreData = userData.user.email
            user = requests.post('http://127.0.0.1:8080/auth/token/login/', data={
                'email': moreData,
                'password': request.data['password']
            })
            data = user.json()
        else:
            user = requests.post('http://127.0.0.1:8080/auth/users/', data={
                'username': request.data['email'].split('@')[0],
                'email': request.data['email'],
                'password': request.data['password'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name']
            })

            if user.status_code == 201:
                moreData = requests.post('http://127.0.0.1:8080/auth/get/more/', data={
                    'user': user.json()['id'],
                    'number': request.data['number'],
                    'location': request.data['location'],
                    'google': request.data['token']
                })
                data = moreData.json()
            else:
                data = user.json()

        return Response(data=data)


class GetDataFromAppleId(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def post(self, request):
        ''' Вход по токену соцсети с придумыванием пароля, если токен есть возвращаются данные, если нет создается пользователь
        с введенными данными которые сопровождают запрос (так же нужно указывать пароль) '''
        userData = UserData.objects.filter(
            appleId=request.data['token']).first()
        if userData:
            moreData = userData.user.email
            user = requests.post('http://127.0.0.1:8080/auth/token/login/', data={
                'email': moreData,
                'password': request.data['password']
            })
            data = user.json()
        else:
            user = requests.post('http://127.0.0.1:8080/auth/users/', data={
                'username': request.data['email'].split('@')[0],
                'email': request.data['email'],
                'password': request.data['password'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name']
            })

            if user.status_code == 201:
                moreData = requests.post('http://127.0.0.1:8080/auth/get/more/', data={
                    'user': user.json()['id'],
                    'number': request.data['number'],
                    'location': request.data['location'],
                    'appleId': request.data['token']
                })
                data = moreData.json()
            else:
                data = user.json()

        return Response(data=data)


class GetDataFromFacebook(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = MoreDataSerializer

    def post(self, request):
        ''' Вход по токену соцсети с придумыванием пароля, если токен есть возвращаются данные, если нет создается пользователь
        с введенными данными которые сопровождают запрос (так же нужно указывать пароль) '''
        userData = UserData.objects.filter(
            facebook=request.data['token']).first()
        if userData:
            moreData = userData.user.email
            user = requests.post('http://127.0.0.1:8080/auth/token/login/', data={
                'email': moreData,
                'password': request.data['password']
            })
            data = user.json()
        else:
            user = requests.post('http://127.0.0.1:8080/auth/users/', data={
                'username': request.data['email'].split('@')[0],
                'email': request.data['email'],
                'password': request.data['password'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name']
            })

            if user.status_code == 201:
                moreData = requests.post('http://127.0.0.1:8080/auth/get/more/', data={
                    'user': user.json()['id'],
                    'number': request.data['number'],
                    'location': request.data['location'],
                    'facebook': request.data['token']
                })
                data = moreData.json()
            else:
                data = user.json()

        return Response(data=data)
