from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.course import CourseSerializers, CourseModelSerializer
from api.urlis.response import BaseResponse
from api import models


class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        # try:
        quertset = models.Course.objects.all()
        ret_obj = CourseSerializers(instance=quertset, many=True)
        # for i in ret_obj.price_list:
        #     print(i)
        ret.data = ret_obj.data
        # except Exception as e:
        #     ret.error = '查询失败'
        #     ret.code = 500
        return Response(ret.dict)