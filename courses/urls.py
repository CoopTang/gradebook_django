from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
  path('', views.index, name = 'index'),
  path('<int:course_id>/', views.show, name = 'show'),
  path('<int:course_id>/sections/<int:section_id>/', views.sections, name = 'sections'),
]