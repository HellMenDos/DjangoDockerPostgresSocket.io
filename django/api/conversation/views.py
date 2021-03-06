from django.shortcuts import render
from .models import Applications, Messages, Review, Location, Commucate, Proposal
from .serializers import ApplicationsListSerializer, ApplicationsSerializer, CommucateListSerializer, MessagesListSerializer, MessagesSerializer, ProposalListSerializer, ReviewListSerializer, ReviewSerializer, LocationSerializer, CommucateSerializer, ApplicationsSerializerStatus, ApplicationsSerializerActive, ProposalSerializer, UpdatePhotoSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, QueryDict

# Insert/Read/Update/Delete proposal for company

# Proposals-------------------------------


class InsertProposal(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        """
        НУЖЕН ТОКЕН
        Здесь можно обновить любые данные, самое главное в теле запроса иметь id,
        а остальноное можно компоновать как захочется"""
        data = ProposalSerializer(Proposal.objects.get(
            pk=request.data['id']).id, data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = {'status': 'success'}
        else:
            status = {'status': 'error'}
        return Response(data=[status])

    def delete(self, request):
        """ 
        НУЖЕН ТОКЕН
        Едиственный параметр id """
        deal = Proposal.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=[{'status': 'success'}])

# Get Proposals with with number of application


class getProposals(generics.ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение предложений по номеру заявки '''
        proposal = Proposal.objects.filter(application=num)
        data = ProposalListSerializer(proposal, many=True)
        if data:
            response = data.data
        return Response(data=response)

# Get Proposals with with number of company


class getProposalsCompany(generics.ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение предложений по номеру компаниие '''
        proposal = Proposal.objects.filter(company=num)
        data = ProposalListSerializer(proposal, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)
# -------------------------------


# Applications -------------------------------

# Insert/Read/Update/Delete proposal for applications
class UpdatePhoto(generics.UpdateAPIView):
    queryset = Applications.objects.all()
    serializer_class = UpdatePhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        data = UpdatePhotoSerializer(Applications.objects.get(
            pk=request.data['id']), data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = {'status': 'success'}
        else:
            status = {'status': 'Ошибка при введении данных'}
        return Response(data=[status])


class GetAllAppl(generics.ListCreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """НУЖЕН ТОКЕН"""
        loc = Location.objects.filter(title=request.data['location']).first()

        if loc:
            request.data.update(
                {'location': LocationSerializer(loc).data['id']})
        else:
            locactionSerial = LocationSerializer(
                data={'title': request.data['location']})
            if locactionSerial.is_valid():
                locactionSerial.save()
                request.data.update({'location': locactionSerial.data['id']})

        data = ApplicationsSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data=data.data)
        else:
            return Response(data=data.errors)

    def put(self, request):
        """ 
        НУЖЕН ТОКЕН
        Здесь можно обновить любые данные, самое главное в теле запроса иметь id, а остальноное можно компоновать как захочется"""

        if 'location' in request.data:
            loc = Location.objects.filter(
                title=request.data['location']).first()

            if loc:
                request.data.update(
                    {'location': LocationSerializer(loc).data['id']})
            else:
                locactionSerial = LocationSerializer(
                    data={'title': request.data['location']})
                if locactionSerial.is_valid():
                    locactionSerial.save()
                    request.data.update(
                        {'location': locactionSerial.data['id']})

        data = ApplicationsSerializer(Applications.objects.filter(
            pk=request.data['id']), data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = {'status': 'success'}
        else:
            status = {'status': 'Ошибка при введении данных'}
        return Response(data=[status])

    def delete(self, request):
        """ 
        НУЖЕН ТОКЕН
        Едиственный параметр id """
        deal = Applications.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=[{'status': 'success'}])

# Get one application with id


class GetOneAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение одной заявки '''
        user = Applications.objects.get(pk=num)
        data = ApplicationsListSerializer(user)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get one application with user id


class GetOneApplUser(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение одной заявки '''
        user = Applications.objects.filter(user=num)
        data = ApplicationsListSerializer(user, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get one application with company id


class GetOneApplCompany(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num):
        ''' 
        НУЖЕН ТОКЕН
        Получение одной заявки '''
        user = Applications.objects.filter(company=num)
        data = ApplicationsListSerializer(user, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get one application with user id and active


class GetUserActiveAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num, active):
        ''' 
        НУЖЕН ТОКЕН
        получение по полю активности записей от пользователей '''
        user = Applications.objects.filter(user=num, active=active)
        data = ApplicationsListSerializer(user, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get one application with comapny id and active


class GetCompanyActiveAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num, active):
        ''' 
        НУЖЕН ТОКЕН
        получение по полю активности записей от компаний '''
        user = Applications.objects.filter(company=num, active=active)
        data = ApplicationsListSerializer(user, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get one application with comapny id and status


class GetCompanyStatusAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num, status):
        ''' 
        НУЖЕН ТОКЕН
        получение по статусу записей от компаний '''
        user = Applications.objects.filter(company=num, status=status)
        data = ApplicationsListSerializer(user, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get one application with user id and status


class GetUserStatusAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, num, status):
        ''' 
        НУЖЕН ТОКЕН
        получение по статусу записей от пользователей '''
        user = Applications.objects.filter(user=num, status=status)
        data = ApplicationsListSerializer(user, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Change status


class ChangeStatusAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializerStatus
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        """ 
        НУЖЕН ТОКЕН
        Изменение статуса, два обязательных параметра id и status"""
        apl = Applications.objects.get(pk=request.data['id'])
        apl.status = request.data['status']
        apl.save()
        return Response(data=[{'status': 'success'}])

# Change active


class ChangeActiveAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializerActive
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        """ 
        НУЖЕН ТОКЕН
        Изменение акстивности, два обязательных параметра id и active"""
        apl = Applications.objects.get(pk=request.data['id'])
        apl.active = request.data['active']
        apl.save()
        return Response(data=[{'status': 'success'}])
# -------------------------------


# Rooms -------------------------------

# insert room


class InsertRoom(generics.ListCreateAPIView):
    queryset = Commucate.objects.all()
    serializer_class = CommucateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        """ 
        НУЖЕН ТОКЕН
        Обязательный парметр id"""
        deal = Commucate.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=[{'status': 'success'}])

# Get all rooms for user


class getRooms(generics.ListAPIView):
    queryset = Commucate.objects.all()
    serializer_class = CommucateListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        """ 
        НУЖЕН ТОКЕН
        Получение всех комнат по индетификатору пользователя  """
        userFrom = Commucate.objects.filter(userFrom=id)
        userTo = Commucate.objects.filter(userTo=id)
        new_query_set = userFrom | userTo
        data = CommucateListSerializer(new_query_set, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get room for user


class getRoom(generics.ListAPIView):
    queryset = Commucate.objects.all()
    serializer_class = CommucateListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, companyId, userId):
        """ 
        НУЖЕН ТОКЕН
        userFrom - userId, userTo - companyId"""
        data = Commucate.objects.filter(userFrom=userId, userTo=companyId)
        data = CommucateListSerializer(data, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# -------------------------------


# Message -------------------------------

class InsertMessage(generics.CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class getMessage(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesListSerializer

    def get(self, request, id):
        mess = Messages.objects.filter(room=id)
        data = MessagesListSerializer(mess, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)
# -------------------------------


# Review -------------------------------
# Insert/Update

class InsertReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        """ 
        НУЖЕН ТОКЕН
        Здесь можно обновить любые данные, самое главное в теле запроса иметь id, 
        а остальноное можно компоновать как захочется"""
        data = ReviewSerializer(Review.objects.get(
            pk=request.data['id']).id, data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = {'status': 'success'}
        else:
            status = {'status': 'Проверьте правильность введенных данных'}
        return Response(data=[status])

# Get review with userFrom id


class getReviewFrom(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        """НУЖЕН ТОКЕН"""
        rev = Review.objects.filter(userFrom=id)
        data = ReviewListSerializer(rev, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)

# Get review with userTo id


class getReviewTo(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        """НУЖЕН ТОКЕН"""
        rev = Review.objects.filter(userTo=id)
        data = ReviewListSerializer(rev, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)
# -------------------------------

# Get adress


class getAdress(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, title):
        loc = Location.objects.filter(title__startswith=title)
        data = LocationSerializer(loc, many=True)
        response = []
        if data:
            response = data.data
        return Response(data=response)


class getAllAdress(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
