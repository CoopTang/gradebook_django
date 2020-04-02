from django.db import models

class Course(models.Model):
  name = models.CharField(max_length = 200)

class Test(models.Model):
  title  = models.CharField(max_length = 200)
  course = models.ForeignKey(Course, on_delete = models.CASCADE)
