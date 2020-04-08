from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import CourseSerializers
from .models import Course
from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import render
import random


class GenericAPIViewCourse(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    
    def post(self, request):
        self.create(request)
        #html = "<html><script>window.location = 'http://127.0.0.1:8000/course/get_course_data';</script></html>"
        html = "<html><script>alert('DATA SAVED');window.location = 'http://127.0.0.1:8000/course/get_course_data';</script></html>"

        return HttpResponse(html) 
    
def get_course_data(request):
    course_list = []
    course_obj = Course.objects.all()
    if course_obj:
        for each in course_obj:
            context = {}
            context = {
                        'course_name': each.course_name,
                        'course_author_name':each.course_author_name,
                        'price':each.price,
                        'image': get_image()
                        }
            course_list.append(context)
        return render(request, 'course/details.html', {'details': course_list})
    else:
        return render(request, 'course/details.html', {'details1': course_list})
        
        
def get_image():
    image_num = random.choice(range(1,6))
    image = '/G0'+str(image_num)+'.jpg'
    return(image)

def about(request):
    context = {}
    return render(request, 'course/about.html', context)
    