from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta():
        model = Data
        fields = "__all__"