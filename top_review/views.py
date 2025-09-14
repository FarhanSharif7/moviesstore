from django.shortcuts import render
from movies.models import Review

def index(request):
    # Get all reviews ordered by likes descending
    top_reviews = Review.objects.select_related('user').order_by('-likes')[:20]
    