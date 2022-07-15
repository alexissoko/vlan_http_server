from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vlan
# import PhoneNumberField

# Create your models here.
class VlanSerializer(serializers.ModelSerializer):
    # Todo creator as readonly
    # creator = serializers.ReadOnlyField(source='creator.name')


    class Meta:
        model = Vlan
        fields = ['id', 'name', 'description', 'location', 'created']

    def __str__ (self):
        return self.name
