from django.conf.urls import url, include
from django.contrib import admin
from api.views import course, teachers, scholarship,\
    degree_course, degree_modules, efgh, doLogin, shoppingcar
urlpatterns = [
    url(r'courses$',  course.CourseView.as_view()),
    url(r'login',doLogin.doLogin.as_view({'post': 'login'})),
    url(r'teachers', teachers.TeacherView.as_view()),                           # a.查看所有学位课并打印学位课名称以及授课老师
    url(r'scholarship', scholarship.Scholarship.as_view()),                     # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    url(r'course_zhuan', degree_course.Degree_courseAPIView.as_view()),        # c.展示所有的专题课
    url(r'degree_modules/(?P<id>\d+)/$', degree_modules.Degree_modulesAPIView.as_view()),        # d. 查看id=1的学位课对应的所有模块名称
    url(r'shoppingcar/$', shoppingcar.ShoppingCar.as_view({'post':'shoppingcar','get':'list','delete':'destroy','put':'updata'})),        # d. 查看id=1的学位课对应的所有模块名称



    url(r'courses/(?P<path>\w)/(?P<id>\d+)/$',efgh.EFGHAPIView.as_view()),
]