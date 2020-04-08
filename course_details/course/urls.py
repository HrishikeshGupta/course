from django.urls import path

from .views import GenericAPIViewCourse,get_course_data,about
from django.urls import path


urlpatterns = [
    path('insert_data',GenericAPIViewCourse.as_view()),
    path('get_course_data',get_course_data),
    path('about',about),
    ]