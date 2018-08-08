from rest_framework.response import Response
from rest_framework.views import APIView
from api.urlis.response import BaseResponse
from rest_framework.viewsets import ViewSetMixin
import json


class ShoppingCar(ViewSetMixin, APIView):

    def shoppingcar(self, request, *args, **kwargs):
        ret = BaseResponse()
        print(request.body)
        print(request.data)
        title_price_id = json.loads(request.body)
        tiele_id = title_price_id.get('title_id')
        price_id = title_price_id.get('price_id')
        print(tiele_id,price_id)

        return Response(ret.dict)