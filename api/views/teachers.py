from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.teachers import TeachersSerializers
from api.urlis.response import BaseResponse
from api import models


class TeacherView(APIView):

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            quertset = models.DegreeCourse.objects.all()
            ret_obj = TeachersSerializers(instance=quertset, many=True)
            print(ret_obj)
            ret.data = ret_obj.data
        except Exception as e:
            ret.error = '查询失败'
            ret.code = 500
        return Response(ret.dict)