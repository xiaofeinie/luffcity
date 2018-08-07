from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.degree_modules import Degree_modulesSerializers
from api.urlis.response import BaseResponse
from api import models


class Degree_modulesAPIView(APIView):

    def get(self, request, id, *args, **kwargs):
        ret = BaseResponse()
        queryser = models.Course.objects.filter(degree_course__id=id)
        modes_obj = Degree_modulesSerializers(instance=queryser, many=True)
        ret.data = modes_obj.data
        return Response(ret.dict)