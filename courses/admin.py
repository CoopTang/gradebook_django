from django.contrib import admin

from .models import Course, Test

class TestAdmin(admin.ModelAdmin):
  list_display = ['title']
  fields = ['title']

class TestInline(admin.TabularInline):
  model = Test
class CourseAdmin(admin.ModelAdmin):
  model = Course
  inlines = [
    TestInline,
  ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Test, TestAdmin)
