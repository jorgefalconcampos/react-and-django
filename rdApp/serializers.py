# un serializer sirve para transformar las instacias de cliente y Query sets desde y hacia JSON

from rest_framework import serializers as s
from . models import Customer


class CustomerSerializer(s.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'first_name', 'last_name', 'email', 'phone', 'address', 'description')