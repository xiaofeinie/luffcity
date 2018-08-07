from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.degree_course import Degree_courseSerializers
from api.urlis.response import BaseResponse
from api import models


class Degree_courseAPIView(APIView):

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        queryset = models.Course.objects.filter(degree_course__isnull=True)
        degree_list = Degree_courseSerializers(instance=queryset, many=True)
        ret.data = degree_list.data
        return Response(ret.dict)
