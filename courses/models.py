from django.db import models

class Course(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

class Test(models.Model):
  title        = models.CharField(max_length = 200)
  total_points = models.PositiveIntegerField(default = 1)
  course       = models.ForeignKey(Course, on_delete = models.CASCADE)

  def __str__(self):
    return self.title

class Quiz(models.Model):
  title  = models.CharField(max_length = 200)
  total_points = models.PositiveIntegerField(default = 1)
  course = models.ForeignKey(Course, on_delete = models.CASCADE)

  def __str__(self):
    return self.title

class Homework(models.Model):
  title  = models.CharField(max_length = 200)
  total_points = models.PositiveIntegerField(default = 1)
  course = models.ForeignKey(Course, on_delete = models.CASCADE)

  def __str__(self):
    return self.title

    from django.db import models

class Student(models.Model):
  first_name = models.CharField(max_length=200)
  last_name  = models.CharField(max_length=200)

  def __str__(self):
    return '%s, %s' % (self.last_name, self.first_name)

class Section(models.Model):
  section_id = models.CharField(max_length = 5, default = '001')
  course     = models.ForeignKey(Course, on_delete = models.CASCADE)

  def __str__(self):
    return '%s-%s' % (self.course.name, self.section_id)