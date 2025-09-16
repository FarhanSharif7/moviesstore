from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='hide.index'),
    path('add/<int:movie_id>/', views.hide_movie, name='hide.add'),
    path('remove/<int:movie_id>/', views.unhide_movie, name='hide.remove'),
]