from django.contrib import admin

from .models import Course, Test, Quiz, Homework

class TestAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points']
  fields = ['title', 'total_points', 'course']

class TestInline(admin.TabularInline):
  model = Test
  
class QuizAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points']
  fields = ['title', 'total_points', 'course']

class QuizInline(admin.TabularInline):
  model = Quiz

class HomeworkAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points']
  fields = ['title', 'total_points', 'course']

class HomeworkInline(admin.TabularInline):
  model = Homework

class CourseAdmin(admin.ModelAdmin):
  model = Course
  inlines = [
    TestInline,
    QuizInline,
    HomeworkInline
  ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Homework, HomeworkAdmin)
