from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_author_name = models.CharField(max_length=200)
    price = models.FloatField()
    in_use = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
