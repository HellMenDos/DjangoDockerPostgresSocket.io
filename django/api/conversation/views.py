from django.shortcuts import render
from .models import Applications,Messages,Review,Location,Commucate,Proposal
from .serializers import ApplicationsSerializer,MessagesSerializer,ReviewSerializer,LocationSerializer,CommucateSerializer,ApplicationsSerializerStatus,ApplicationsSerializerActive,ProposalSerializer
from rest_framework import generics, status,permissions
from rest_framework.response import Response


class InsertProposal(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        """ Здесь можно обновить любые данные, самое главное в теле запроса иметь id, 
        а остальноное можно компоновать как захочется"""
        data = ProposalSerializer(Proposal.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = 'success'
        else:
            status = 'fail'
        return Response(data=[status])
    
    def delete(self,request):
        """ Едиственный параметр id """
        deal = Proposal.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=['success'])

class getProposals(generics.ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    
    def get(self,request,num):
        proposal = Proposal.objects.filter(application=num)
        data = ProposalSerializer(proposal)
        return Response(data=data.data)

class getProposalsCompany(generics.ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    
    def get(self,request,num):
        proposal = Proposal.objects.filter(company=num)
        data = ProposalSerializer(proposal)
        return Response(data=data.data)


class GetAllAppl(generics.ListCreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        """ Здесь можно обновить любые данные, самое главное в теле запроса иметь id, а остальноное можно компоновать как захочется"""
        data = ApplicationsSerializer(Applications.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = 'success'
        else:
            status = 'fail'
        return Response(data=[status])

    def delete(self,request):
        """ Едиственный параметр id """
        deal = Applications.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=['success'])

class GetOneAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def get(self,request,num):
        user = Applications.objects.get(pk=num)
        data = ApplicationsSerializer(user)
        return Response(data=data.data)


class GetUserActiveAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def get(self,request,num,active):
        user = Applications.objects.filter(user=num,active=active)
        data = ApplicationsSerializer(user, many=True)
        return Response(data=data.data)

class GetCompanyActiveAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def get(self,request,num,active):
        user = Applications.objects.filter(company=num,active=active)
        data = ApplicationsSerializer(user, many=True)
        return Response(data=data.data)


class GetCompanyStatusAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def get(self,request,num,status):
        user = Applications.objects.filter(company=num,status=status)
        data = ApplicationsSerializer(user, many=True)
        return Response(data=data.data)

class GetUserStatusAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def get(self,request,num,status):
        user = Applications.objects.filter(user=num,status=status)
        data = ApplicationsSerializer(user, many=True)
        return Response(data=data.data)

class ChangeStatusAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializerStatus
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        """ Изменение статуса, два обязательных параметра id и статус"""
        apl = Applications.objects.get(pk=request.data['id'])
        apl.status = request.data['status']
        apl.save()
        return Response(data=['success'])

class ChangeActiveAppl(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializerActive
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        """ Изменение акстивности, два обязательных параметра id и кстивный или нет"""
        apl = Applications.objects.get(pk=request.data['id'])
        apl.active = request.data['active']
        apl.save()
        return Response(data=['success'])

class InsertRoom(generics.ListAPIView):
    queryset = Commucate.objects.all()
    serializer_class = CommucateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self,request):
        """ Обязательный парметр id"""
        deal = Commucate.objects.get(pk=request.data['id'])
        deal.delete()
        return Response(data=['success'])

class getRooms(generics.ListAPIView):
    queryset = Commucate.objects.all()
    serializer_class = CommucateSerializer
    
    def get(self,request,id):
        userFrom = Commucate.objects.filter(userFrom=id)
        userTo = Commucate.objects.filter(userTo=id)
        new_query_set = userFrom | userTo
        data = CommucateSerializer(new_query_set, many=True)
        return Response(data=data.data)


class InsertMessage(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    
class getMessage(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

    def get(self,request,id):
        mess = Messages.objects.filter(room=id)
        data = MessagesSerializer(mess, many=True)
        return Response(data=data.data)



class InsertReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        """ Здесь можно обновить любые данные, самое главное в теле запроса иметь id, а остальноное можно компоновать как захочется"""
        data = ReviewSerializer(Review.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        status = ''
        if data.is_valid():
            data.save()
            status = 'success'
        else:
            status = 'fail'
        return Response(data=[status])

class getReviewFrom(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self,request,id):
        rev = Review.objects.filter(userFrom=id)
        data = ReviewSerializer(rev, many=True)
        return Response(data=data.data)

class getReviewTo(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self,request,id):
        rev = Review.objects.filter(userTo=id)
        data = ReviewSerializer(rev, many=True)
        return Response(data=data.data)

class getAdress(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self,request,title):
        loc = Location.objects.filter(title__startswith=title)
        data = LocationSerializer(loc, many=True)
        return Response(data=data.data)

