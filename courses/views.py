from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Course

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
