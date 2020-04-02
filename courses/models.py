from django.db import models

class Course(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

class Test(models.Model):
  title  = models.CharField(max_length = 200)
  course = models.ForeignKey(Course, on_delete = models.CASCADE)

  def __str__(self):
    return self.title
