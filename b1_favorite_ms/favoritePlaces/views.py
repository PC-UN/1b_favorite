from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Favourite
from .serializers import FavouriteSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin


class ListFavorite(generics.ListCreateAPIView):
    serializer_class = FavouriteSerializer
    
    def get_queryset(self):
        return Favourite.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.save()

class FavoriteView(generics.ListAPIView):

    serializer_class = FavouriteSerializer
    def get_queryset(self):
        user_id= self.kwargs['user_id']
        return Favourite.objects.filter(user_id=user_id)



class DetailFavourite(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
