from rest_framework.response import Response
from rest_framework.views import APIView
from api.urlis.response import BaseResponse
from rest_framework.viewsets import ViewSetMixin
from api import models
from rest_framework.parsers import JSONParser
import json
import redis

CONN = redis.Redis(host='192.168.11.99', port=6379)
USER = 1


class ShoppingCar(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        '''

        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # CONN.hset('xoxoxx','ss','456')
        # print(CONN.hget('xx','k1').decode('utf-8'),'k1')
        # print(CONN.hget('xoxoxx','ss').decode('utf-8'),'xoxoxx')
        # print(CONN.hget('xx','k2').decode('utf-8'),'k2')
        # print(CONN.get('xiaofei_name').decode('utf-8'))
        # print(CONN.get('xiazhen_name').decode('utf-8'))
        # print(CONN.get('caiyunfeng_name').decode('utf-8'))
        try:
            ret = BaseResponse()
            key = 'shopping_car_%s_*'%USER
            shopping_car_course_list = []
            user_key_list = CONN.keys(key)
            for key in user_key_list:
                tmp = {
                    'id':CONN.hget(key,'id').decode('utf8'),
                    'name':CONN.hget(key,'name').decode('utf8'),
                    'img':CONN.hget(key,'img').decode('utf8'),
                    'price':CONN.hget(key,'price').decode('utf8'),
                    'defaut_price_id':CONN.hget(key,'defaut_price_id').decode('utf8'),
                    'defaut_price':json.loads(CONN.hget(key,'defaut_price').decode('utf8')),
                }
                shopping_car_course_list.append(tmp)

            ret.code = 200
            ret.data = shopping_car_course_list
        except Exception as e:
            ret.code = 106
            ret.error = '获取购物车失败！'
        return Response(ret.dict)

    def shoppingcar(self, request, *args, **kwargs):
        ret = BaseResponse()
        # 获取用户发来的课程id和价格id
        try:
            courier_id = request.data.get('title_id')
            price_id = request.data.get('price_id')
            print(courier_id)
            if courier_id is None or price_id is None:
                ret.code = 100
                ret.error = '购物车空空如也！赶紧添加购物车吧'
                return Response(ret.dict)
            course_obj = models.Course.objects.filter(pk=courier_id).first()
            price_obj = models.PricePolicy.objects.filter(pk=price_id).first()
            # 判断课程id是否合法
            if not course_obj:
                ret.code = 101
                ret.error = '请选择正确的商品！'
                return Response(ret.dict)
            # 判断价格id是否合法
            price_polocy_list = course_obj.price_policy.all()
            polocy_price_dict = {}
            for price in price_polocy_list:
                emp = {
                    'id':price.id,
                    'valid_period': price.valid_period,
                    'price':price.price,
                    'valid_period_choices':price.get_valid_period_display()
                }
                polocy_price_dict[str(price.id)] = emp



            if price_id not in polocy_price_dict:
                ret.code = 102
                ret.error = '请选择正确的价格策略！'
                return Response(ret.dict)

            key = 'shopping_car_%s_%s' % (USER, courier_id)
            CONN.hset(key, 'id', courier_id)
            CONN.hset(key, 'name', course_obj.name)
            CONN.hset(key, 'img', course_obj.course_img)
            CONN.hset(key, 'price', price_obj.price)
            CONN.hset(key, 'defaut_price_id', price_id)
            CONN.hset(key, 'defaut_price', json.dumps(polocy_price_dict))
            # expire--->等待多长时间后在redis中删除这个键值
            CONN.expire(key, 20*60)
            ret.code = 200
            ret.data = '添加购物车成功！'
        except Exception as e:
            ret.code = 105
            ret.error = '添加购物车失败！'
        return Response(ret.dict)

    def destroy(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            del_shopping_id = request.GET.get('delete_shopping_id')
            key = 'shopping_car_%s_%s' % (USER,del_shopping_id)
            CONN.delete(key)
            ret.code = 200
            ret.data = '删除成功！'
        except Exception as e:
            ret.code = 107
            ret.error = '删除失败！'

        return Response(ret.dict)

    def updata(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            course_id = request.data.get('tetle_id')
            policy_id = str(request.data.get('price_id')) if request.data.get('price_id') else None
            key = 'shopping_car_%s_%s'%(USER,course_id)
            print(request.data)
            if not CONN.exists(key):
                ret.code = 107
                ret.error = '课程不存在！'
                return Response(ret.dict)
            price_policy_dict = json.loads(CONN.hget(key, 'defaut_price').decode('utf-8'))
            if policy_id not in price_policy_dict:
                ret.code = 10008
                ret.error = '价格策略不存在'
                return Response(ret.dict)
            CONN.hset(key, 'defaut_price_id', policy_id)
            CONN.hset(key, 'price', price_policy_dict[policy_id]['price'])
            ret.data = '修改成功'
            ret.code = 200
        except Exception as e:
            ret.code = 102
            ret.error = '修改失败'
        return Response(ret.dict)