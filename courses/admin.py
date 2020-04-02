from django.contrib import admin

from .models import Course, Test, Quiz, Homework, Student, Section, TestStudent, QuizStudent, HomeworkStudent

class TestInline(admin.TabularInline):
  model = Test

class TestStudentAdmin(admin.ModelAdmin):
  list_display = ['student', 'test', 'score']
  fields = ['student', 'test', 'score']
  inlines = [
    
  ]

class TestStudentInline(admin.TabularInline):
  model = TestStudent

class TestAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points', 'course']
  fields = ['title', 'total_points', 'course']
  inlines = [
    TestStudentInline
  ]

class QuizInline(admin.TabularInline):
  model = Quiz

class QuizStudentAdmin(admin.ModelAdmin):
  list_display = ['student', 'quiz', 'score']
  fields = ['student', 'quiz', 'score']

class QuizStudentInline(admin.TabularInline):
  model = QuizStudent

class QuizAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points', 'course']
  fields = ['title', 'total_points', 'course']
  inlines = [
    QuizStudentInline
  ]

class HomeworkInline(admin.TabularInline):
  model = Homework

class HomeworkStudentAdmin(admin.ModelAdmin):
  list_display = ['student', 'homework', 'score']
  fields = ['student', 'homework', 'score']

class HomeworkStudentInline(admin.TabularInline):
  model = HomeworkStudent

class HomeworkAdmin(admin.ModelAdmin):
  list_display = ['title', 'total_points', 'course']
  fields = ['title', 'total_points', 'course']
  inlines = [
    HomeworkStudentInline
  ]

class SectionAdmin(admin.ModelAdmin):
  list_display = ['section_id', 'course']
  fields = ['section_id', 'course', 'students']

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
