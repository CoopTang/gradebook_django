from django.contrib import admin

from .models import Course, Test, Quiz, Homework, Student, Section

class TestAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points', 'course']
  fields = ['title', 'total_points', 'course']

class TestInline(admin.TabularInline):
  model = Test
  
class QuizAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points', 'course']
  fields = ['title', 'total_points', 'course']

class QuizInline(admin.TabularInline):
  model = Quiz

class HomeworkAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points', 'course']
  fields = ['title', 'total_points', 'course']

class HomeworkInline(admin.TabularInline):
  model = Homework

class SectionAdmin(admin.ModelAdmin):
  list_display = ['section_id', 'course']
  fields = ['section_id', 'course']

class SectionInline(admin.TabularInline):
  model = Section

class StudentAdmin(admin.ModelAdmin):
  model = Student

class CourseAdmin(admin.ModelAdmin):
  model = Course
  inlines = [
    TestInline,
    QuizInline,
    HomeworkInline,
    SectionInline,
  ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Section, SectionAdmin)
