from django.db import models

class Course(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

class Section(models.Model):
  section_id = models.CharField(max_length = 5, default = '')
  course     = models.ForeignKey('Course', on_delete = models.CASCADE)
  students   = models.ManyToManyField('Student')

  def __str__(self):
    return '%s-%s' % (self.course.name, self.section_id)

class Student(models.Model):
  first_name = models.CharField(max_length=200)
  last_name  = models.CharField(max_length=200)

  def __str__(self):
    return '%s, %s' % (self.last_name, self.first_name)


class Test(models.Model):
  title        = models.CharField(max_length = 200)
  total_points = models.PositiveIntegerField(default = 1)
  course       = models.ForeignKey('Course', on_delete = models.CASCADE)
  students = models.ManyToManyField('Student', through = "TestStudent")

  def __str__(self):
    return self.title

class Quiz(models.Model):
  title  = models.CharField(max_length = 200)
  total_points = models.PositiveIntegerField(default = 1)
  course = models.ForeignKey('Course', on_delete = models.CASCADE)
  students = models.ManyToManyField('Student', through = "QuizStudent")

  def __str__(self):
    return self.title

class Homework(models.Model):
  title  = models.CharField(max_length = 200)
  total_points = models.PositiveIntegerField(default = 1)
  course = models.ForeignKey('Course', on_delete = models.CASCADE)
  students = models.ManyToManyField('Student', through = "HomeworkStudent")

  def __str__(self):
    return self.title

class TestStudent(models.Model):
  student_id = models.ForeignKey('Student', on_delete = models.CASCADE)
  test_id    = models.ForeignKey('Test', on_delete = models.CASCADE)
  score      = models.PositiveIntegerField(default = 0)
  
class QuizStudent(models.Model):
  student_id = models.ForeignKey('Student', on_delete = models.CASCADE)
  quiz_id    = models.ForeignKey('Quiz', on_delete = models.CASCADE)
  score      = models.PositiveIntegerField(default = 0)
  
class HomeworkStudent(models.Model):
  student_id  = models.ForeignKey('Student', on_delete = models.CASCADE)
  homework_id = models.ForeignKey('Homework', on_delete = models.CASCADE)
  score       = models.PositiveIntegerField(default = 0)