from django.contrib.auth.models import Group
from rest_framework import serializers
from user.models import NewsLetter,CustomUser,Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        #fields = '__all__' 
        fields = ['username', 'email', 'groups','kode','number','last_name', 'first_name','password']
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__' 
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__' 


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']