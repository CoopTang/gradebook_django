from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Course, Section, Test, Quiz, Homework

def index(request):
  courses = Course.objects.all()
  context = {'courses': courses}
  return render(request, 'courses/index.html', context)

def show(request, course_id):
  course = get_object_or_404(Course, pk = course_id)
  context = {
    'course': course,
    'course_sections': course.section_set.all(),
  }
  return render(request, 'courses/show.html', context)

def sections(request, course_id, section_id):
  tests = Test.objects.filter(course_id = course_id)
  quizes = Quiz.objects.filter(course_id = course_id)
  homeworks = Homework.objects.filter(course_id = course_id)
  context = {
    'tests': tests,
    'quizes': quizes,
    'homeworks': homeworks
  }
  return render(request, 'courses/sections/show.html', context)
