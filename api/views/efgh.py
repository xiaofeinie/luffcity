from rest_framework.views import APIView
from rest_framework.response import Response
from api.urlis.response import BaseResponse
from api.serializers import efgh
from api import models


class EFGHAPIView(APIView):

    def get(self, request, path, id, *args, **kwargs):
        ret = BaseResponse()
        queryset = models.Course.objects.filter(id=id)
        if path == 'e':
            e_obj = efgh.ESerializers(instance=queryset, many=True)
            ret.data = e_obj.data

        elif path == 'f':
            f_obj = efgh.FSerializers(instance=queryset, many=True)
            ret.data = f_obj.data
        elif path == 'g':
            g_obj = efgh.GSerializers(instance=queryset, many=True)
            ret.data = g_obj.data
        elif path == 'h':
            h_obj = efgh.HSerializers(instance=queryset, many=True)
            ret.data = h_obj.data
        else:
            ret.code = 502
            ret.error = '路径错误'
        return Response(ret.dict)