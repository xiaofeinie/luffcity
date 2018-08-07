from rest_framework import serializers
from api import models


class SholarshipSerializers(serializers.Serializer):
    name = serializers.CharField()
    prize_fellow = serializers.SerializerMethodField()

    def get_prize_fellow(self, row):
        prize_list = row.scholarship_set.all()
        return [{'time_percent':item.time_percent, 'value':item.value} for item in prize_list]
