from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='top_review.index'),
    path('like/<int:review_id>/', views.like_review, name='top_review.like_review'),
]