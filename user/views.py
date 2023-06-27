from django.shortcuts import render

from django.contrib.auth.models import User, Group
from user.models import NewsLetter
from rest_framework import viewsets
from rest_framework import permissions
from user.serializers import UserSerializer, GroupSerializer,NewsSerializer
from user.models import CustomUser,Message

class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class  NewsSet(viewsets.ModelViewSet):

    queryset= NewsLetter.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]


class  MessagesSet(viewsets.ModelViewSet):
    
    queryset= Message.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]