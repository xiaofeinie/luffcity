from rest_framework import serializers
from api import models

class ESerializers(serializers.Serializer):
    name = serializers.CharField()
    level_now = serializers.CharField(source='get_level_display')
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommend_courses = serializers.SerializerMethodField()

    def get_recommend_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]


class FSerializers(serializers.Serializer):
    question = serializers.SerializerMethodField()

    def get_question(self, row):
        question_list = row.asked_question.all()
        print([{'question':item.question} for item in question_list])
        return [{'question':item.question} for item in question_list]


class GSerializers(serializers.Serializer):
    outline = serializers.SerializerMethodField()

    def get_outline(self, row):
        outline_list = row.coursedetail.courseoutline_set.all()
        return [{'content':item.content} for item in outline_list]

class HSerializers(serializers.Serializer):
    chapter = serializers.SerializerMethodField()

    def get_chapter(self, row):
        chapter_list = row.coursechapters.all()
        return [{'chapter':item.chapter} for item in chapter_list]
