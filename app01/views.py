from django.shortcuts import render, HttpResponse

# Create your views here.
from api import models


def tezt_index(request):
    # a. 查看所有学位课并打印学位课名称以及授课老师
    # obj_list = models.DegreeCourse.objects.all()
    # for item in obj_list:
    #     for j in item.teachers.all():
    #         print(item.name,j.name)


    # b. 查看所有学位课并打印学位课名称以及学位课的奖学金
    # obj_list = models.DegreeCourse.objects.all()
    # for item in obj_list:
    #     for it in item.scholarship_set.all():
    #         print(item.name,it.value)

    # c. 展示所有的专题课
    # 				models.Course.objects.filter(degree_course__isnull=True)
    # ret = models.Course.objects.filter(degree_course__isnull=True)
    # for i in ret:
    #     print(i.name)
    # d.查看id = 1的学位课对应的所有模块名称
    # obj = models.DegreeCourse.objects.filter(pk=1).first()
    # mod_obj = obj.course_set.all().first()

    # print(mod_obj.name)
    # e. 获取id=1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    ret = models.Course.objects.filter(id=1).first()
    print(ret.name, ret.get_level_display(),ret.coursedetail.why_study,
          ret.coursedetail.what_to_study_brief,
          ret.coursedetail.recommend_courses.all())




    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    # ret = models.Course.objects.filter(id=1,).first()
    # for i in ret.asked_question.all():
    #     print(i.question)

    # g. 获取id=1的专题课，并打印该课程相关的课程大纲

    # ret = models.CourseOutline.objects.filter(course_detail__course__id=1)
    # for i in ret:
    #     print(i.title, i.content)


    # h. 获取id=1的专题课，并打印该课程相关的所有章节
    # ret = models.CourseChapter.objects.filter(course__id=1)
    # for i in ret:
    #     print(i.name)


    # i. 获取id=1的专题课，并打印该课程相关的所有课时
    # 				第1章·Python 介绍、基础语法、流程控制
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 				第1章·Python 介绍、基础语法、流程控制
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # 					01-课程介绍（一）
    # ret = models.CourseChapter.objects.filter(course__id=1)
    # for i in ret:
    #     re = models.CourseSection.objects.filter(chapter__id=i.pk)
    #     print(i.name)
    #     for j in re:
    #         print(j.name)




    # i.  获取id=1的专题课，并打印该课程相关的所有的价格策略
    # ret = models.Course.objects.filter(id=1).first()
    # for i in ret.price_policy.all():
    #     print(i.price)


    return HttpResponse('ok')


