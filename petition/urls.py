from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petition.index'),
    path('create/', views.create_petition, name='petition.create'),
    path('vote/<int:petition_id>/', views.vote, name='petition.vote'),
    path('unvote/<int:petition_id>/', views.unvote, name='petition.unvote'),

    path("edit/<int:petition_id>/", views.edit_petition, name="petition.edit"),
    path("delete/<int:petition_id>/", views.delete_petition, name="petition.delete"),
]