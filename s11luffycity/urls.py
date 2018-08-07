"""s11luffycity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/(?P<version>\w+)', include('api.api_url')),
]

# from rest_framework.routers import DefaultRouter
# routery = DefaultRouter()
# routery.register(r'degree_course', api_views.Degree_Course)      #专题课列表
# routery.register(r'course', api_views.Course)                    #学位课列表
# routery.register(r'all_course', api_views.All_Course)           #全部课列表
# urlpatterns += routery.urls