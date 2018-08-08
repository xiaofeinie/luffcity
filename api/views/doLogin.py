from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin


class doLogin(ViewSetMixin, APIView):

    def login(self, request, *args, **kwargs):
        print('用户发来了POST请求了，',request)
        return Response({'code':1111})