from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework import filters
from rest_framework import generics

from .models import UserProfile

from .serializers import UserProfileSerializer

from truecaller import permissions


class HomeApiView(APIView):
    serializer_class= UserProfileSerializer
    authentication_classes= (TokenAuthentication,)
    
    #filter_backends= (filters.SearchFilter,)
    #filter_fields=('name','contact')
    #search_fields= ('name','contact',)
    
    def get(self,request,format=None):
        profile= UserProfile.objects.all()
        serializer= UserProfileSerializer(profile, many=True) 
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer= self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            contact= serializer.validated_data.get('contact')
            email= serializer.validated_data.get('email')
            #spam= serializer.validated_data.get('spam')
        
            message= {
                'Name':name,
                'Contact':contact,
                'E-mail':email
            }
            serializer.save(user=self.request.user)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserHome(generics.ListAPIView):
    authentication_classes=(TokenAuthentication,)
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends= (filters.SearchFilter,)
    search_fields= ('name','contact',)

class SearchList(generics.RetrieveAPIView):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()

    

    
    
    
    










