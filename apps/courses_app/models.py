# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
errors = {}
class CourseManager(models.Manager):
    def namelen(self,postdata):
        if len(postdata['name']) < 5: 
            errors['name'] = "Course name should be at least five characters"
        else: 
            errors['name'] = ""
        if len(postdata['desc']) < 15: 
            errors['desc'] = "Description should be at least fifteen characters"
        else:
            errors['desc'] = ""
        if postdata['name'] in [course.name for course in Courses.objects.all()]:
            errors['name'] = "Course name already exists"
        return errors 

class Courses(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager() 