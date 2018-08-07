from rest_framework import serializers
from api import models


class Degree_courseSerializers(serializers.Serializer):
    name = serializers.CharField()