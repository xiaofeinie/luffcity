from rest_framework import serializers
from api import models


class CourseSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    hours = serializers.CharField(source='coursedetail.hours')
    level = serializers.CharField(source='get_level_display')
    # price_list = serializers.CharField(source='price_policy.all.price')
    price_list = serializers.SerializerMethodField()


    def get_price_list(self, row):
        price_list = row.price_policy.all()
        return [{'price':item.price,'id':item.id} for item in price_list]

    # recommend_courses = serializers.SerializerMethodField()
    #
    #
    # def get_recommend_courses(self, row):
    #     # print('row', row)
    #     # print(123)
    #
    #     print(row,type(row),'2222222222222')
    #     print(row.coursedetail,'______-------')
    #     recommend_list = row.coursedetail.all().recommend_courses.all()
    #     # print(321)
    #     # print(recommend_list)
    #     print([{'id': item.id, 'name': item.name} for item in recommend_list])
    #     return [{'id': item.id, 'name': item.name} for item in recommend_list]


class CourseModelSerializer(serializers.ModelSerializer):
    # 查询学习的级别，数据存的是数字，这样就可以查到中文了
    level_now = serializers.CharField(source='get_level_display')
    # 夸表查询
    hours = serializers.CharField(source='coursedetail.hours')
    recommend_courses = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'level_now', 'hours', 'recommend_courses']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]

