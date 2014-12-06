__author__ = 'Chengyu'

from django.forms import widgets
from rest_framework import serializers
from user_manage.models import User


class RegisterResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'ukey')
