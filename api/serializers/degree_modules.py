from rest_framework import serializers
from api import models


class Degree_modulesSerializers(serializers.Serializer):
    name = serializers.CharField()
    course_img = serializers.CharField()
    course_type = serializers.CharField(source='get_course_type_display')
    brief = serializers.CharField()
    level = serializers.CharField(source='get_level_display')
    pub_date = serializers.DateField()
    period = serializers.IntegerField()
