from rest_framework import serializers
from .models import Course

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields= ['course_name','course_author_name','price']
