from . import views
from django.urls import path


app_name = 'asqapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('project/',views.project,name='project'),
    path('work/',views.work,name='work'),
    path('register/',views.register,name='register'),


]
