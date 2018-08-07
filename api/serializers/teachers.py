from rest_framework import serializers
from api import models


class TeachersSerializers(serializers.Serializer):
    name = serializers.CharField()
    teacher_name = serializers.SerializerMethodField()

    def get_teacher_name(self, row):
        teacher_list = row.teachers.all()
        return [{'teacher_name':item.name} for item in teacher_list]
