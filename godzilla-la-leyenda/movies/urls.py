from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_movie/', views.add_movie, name="add_movie"),
    path('upload_movie/', views.upload_movie, name="upload_movie")
]
