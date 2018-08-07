from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.scholarship import SholarshipSerializers
from api.urlis.response import BaseResponse
from api import models


class Scholarship(APIView):

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        queryset = models.DegreeCourse.objects.all()
        sholarship_list = SholarshipSerializers(instance=queryset, many=True)
        print(sholarship_list,'--------------')
        ret.data = sholarship_list.data
        return Response(ret.dict)
